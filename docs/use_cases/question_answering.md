# 在文档中进行问答



> [概念指南](https://docs.langchain.com/docs/use-cases/qa-docs)



在这个背景下，问答是指对您的文档数据进行问答。

对于其他类型的数据的问答，请参阅其他来源的文档，比如[SQL数据库的问答](./tabular.md)或[与API交互](./apis.md)。



对于多文档的问答，您几乎总是想要创建一个索引来管理数据。

这可以智能地访问与给定问题相关的最相关文档，使您避免需要将所有文档传递给LLM（节省时间和金钱）。



请查看[此笔记本](../modules/indexes/getting_started.ipynb)以获得更详细的介绍，但是对于快速入门，涉及的步骤如下：



**加载您的文档**



```python

from langchain.document_loaders import TextLoader

loader = TextLoader('../state_of_the_union.txt')

```



请参阅[此处](../modules/indexes/document_loaders.rst)以获取有关如何开始加载文档的更多信息。



**创建您的索引**



```python

from langchain.indexes import VectorstoreIndexCreator

index = VectorstoreIndexCreator().from_loaders([loader])

```



目前，最好、最受欢迎的索引是VectorStore索引。



**查询您的索引**



```python

query = "关于Ketanji Brown Jackson，总统说了什么"

index.query(query)

```



或者，使用`query_with_sources`也可以返回涉及的来源



```python

query = "关于Ketanji Brown Jackson，总统说了什么"

index.query_with_sources(query)

```



同样，这些高级接口混淆了许多底层操作，因此请查看[此笔记本](../modules/indexes/getting_started.ipynb)以获得更低级的操作步骤。



## 文档问答



问答涉及获取多个文档，然后根据文档的内容提出问题。

LLM的响应将根据文档的内容包含对您问题的回答。



使用问答链的推荐方法是：



```python

from langchain.chains.question_answering import load_qa_chain

chain = load_qa_chain(llm, chain_type="stuff")

chain.run(input_documents=docs, question=query)

```



以下资源可用：



- [问答笔记本](../modules/chains/index_examples/question_answering.ipynb)：演示如何完成此任务的笔记本。

- [VectorDB问答笔记本](../modules/chains/index_examples/vector_db_qa.ipynb)：演示如何对向量数据库进行问答。当您有大量文档，并且不想全部传递给LLM，而是首先对嵌入进行一些语义搜索时，这通常很有用。



## 添加来源



还有一种变体，除了回答问题之外，语言模型还会引用其来源（例如使用的文档）。



使用带来源的问答链的推荐方法是：



```python

from langchain.chains.qa_with_sources import load_qa_with_sources_chain

chain = load_qa_with_sources_chain(llm, chain_type="stuff")

chain({"input_documents": docs, "question": query}, return_only_outputs=True)

```



以下资源可用：



- [带来源的问答笔记本](../modules/chains/index_examples/qa_with_sources.ipynb)：演示如何完成此任务的笔记本。

- [VectorDB带来源的问答笔记本](../modules/chains/index_examples/vector_db_qa_with_sources.ipynb)：演示如何在向量数据库上使用带来源的问答。当您有大量文档，并且不想全部传递给LLM，而是首先对嵌入进行一些语义搜索时，这通常很有用。



## 其他相关资源



其他相关资源包括：



- [与文档一起使用的实用程序](/modules/utils/how_to_guides.rst)：关于如何使用几个实用程序的指南，这些实用程序对于此任务将非常有帮助，包括文本拆分器（用于拆分长文档）和嵌入向量和向量存储（适用于上述向量数据库示例）。

- [合并文档链](/modules/indexes/combine_docs.md)：对于可以完成此任务的特定类型的链的概念概述。



## 端到端示例



有关在端到端方式下完成此任务的示例，请参阅以下资源：



- [语义搜索聊天记录笔记本](question_answering/semantic-search-over-chat.ipynb)：演示如何对群聊会话进行语义搜索的笔记本。

