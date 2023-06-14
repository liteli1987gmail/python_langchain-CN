问题回答在文档中



> 概念指南](https://docs.langchain.com/docs/use-cases/qa-docs)



在此背景下，问题回答指的是在您的文档数据上进行的问题回答。

对于其他类型的数据的问题回答，请参阅其他源的文档，如SQL数据库问题回答](./tabular.md)或与API交互](./apis.md)。



对于多文档的问题回答，您几乎总是希望在数据上创建索引。

这可以用于智能地访问与给定问题相关联的最相关文档，使您无需将所有文档传递给LLM（节省时间和金钱）。



有关更详细的介绍，请参阅此笔记本](../modules/indexes/getting_started.ipynb)，但对于超快速入门，所涉及的步骤是：



**加载您的文档**



```python

from langchain.document_loaders import TextLoader

loader = TextLoader('../state_of_the_union.txt')

```



请参阅此处](../modules/indexes/document_loaders.rst)以获取有关如何开始加载文档的更多信息。



**创建您的索引**



```python

from langchain.indexes import VectorstoreIndexCreator

index = VectorstoreIndexCreator().from_loaders([loader])

```



目前最好、最流行的索引是VectorStore索引。



**查询您的索引**



```python

query = "What did the president say about Ketanji Brown Jackson"

index.query(query)

```



或使用`query_with_sources`也可以返回涉及的源



```python

query = "What did the president say about Ketanji Brown Jackson"

index.query_with_sources(query)

```



同样，这些高级接口隐藏了许多底层操作，请参阅此笔记本](../modules/indexes/getting_started.ipynb)以获取较低级别的逐步说明。



## 文档问题回答



问题回答涉及获取多个文档，然后对其进行提问。

LLM的响应将根据文档的内容包含您的问题的答案。



使用问题回答链的推荐方法是：



```python

from langchain.chains.question_answering import load_qa_chain

chain = load_qa_chain(llm, chain_type="stuff")

chain.run(input_documents=docs, question=query)

```



以下资源可用：



- 问题回答笔记本](../modules/chains/index_examples/question_answering.ipynb)：这是一个通过如何完成此任务的示例。

- VectorDB问题回答笔记本](../modules/chains/index_examples/vector_db_qa.ipynb)：这是一个通过向量数据库进行问题回答的示例。当您有大量文档需要处理，而且不想将它们全部传递给LLM，而是首先想要对嵌入进行一些语义搜索时，这通常非常有用。



## 添加来源



还有一种变体，除了回答问题外，语言模型还会引用其来源（例如，它使用了传递给它的哪些文档）。



使用带有来源的问题回答链的推荐方法是：



```python

from langchain.chains.qa_with_sources import load_qa_with_sources_chain

chain = load_qa_with_sources_chain(llm, chain_type="stuff")

chain({"input_documents": docs, "question": query}, return_only_outputs=True)

```



以下资源可用：



- 带有来源的问题回答笔记本](../modules/chains/index_examples/qa_with_sources.ipynb)：这是一个通过如何完成此任务的示例。

- VectorDB带来源的问题回答笔记本](../modules/chains/index_examples/vector_db_qa_with_sources.ipynb)：这是一个通过向量数据库进行带来源的问题回答的示例。当您有大量文档需要处理，而且不想将它们全部传递给LLM，而是首先想要对嵌入进行一些语义搜索时，这通常非常有用。



## 其他相关资源



其他相关资源包括：



- 用于处理文档的实用程序](/modules/utils/how_to_guides.rst)：介绍如何使用几种对于此任务非常有用的实用程序，包括文本分割器（用于拆分长文档）和嵌入和向量存储（对于上述向量数据库示例非常有用）。

- CombineDocuments链](/modules/indexes/combine_docs.md)：介绍了一些特定类型的链的概念概述，您可以使用这些链来完成此任务。



## 端到端示例



有关以端到端方式完成此任务的示例，请参阅以下资源：



- 在群聊中进行语义搜索的笔记本](question_answering/semantic-search-over-chat.ipynb)：这是一个对群聊对话进行语义搜索的示例。

