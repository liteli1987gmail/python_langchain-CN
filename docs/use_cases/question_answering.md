# 文档问答


> [概念指南](https://docs.langchain.com/docs/use-cases/qa-docs)


在这个语境下，问答是指针对您的文档数据的问题回答。
如需针对其他类型的数据进行问答，请参考其他来源文档，例如[SQL 数据库问答](./tabular.md)或[与 API 交互](./apis.md)。


如果要对许多文档进行问答，则几乎总是要创建一个数据索引。
这可以用于智能地访问给定问题的最相关文档，从而避免将所有文档传递给 LLM（节省时间和金钱）。


有关更详细的介绍，请参见[此笔记本](../modules/indexes/getting_started.ipynb)，但对于超级快速入门，所涉及的步骤是:


**加载您的文档**


```python

from langchain.document_loaders import TextLoader

loader = TextLoader('../state_of_the_union.txt')

```



有关如何开始加载文档的更多信息，请参见[此处](../modules/indexes/document_loaders.rst)。


**创建您的索引**


```python

from langchain.indexes import VectorstoreIndexCreator

index = VectorstoreIndexCreator().from_loaders([loader])

```



到目前为止，最好、最受欢迎的索引是 VectorStore 索引。


**查询您的索引**


```python

query = "What did the president say about Ketanji Brown Jackson"

index.query(query)

```



或者使用 `query_with_sources` 去得到相应参与的资源。


```python

query = "What did the president say about Ketanji Brown Jackson"

index.query_with_sources(query)

```



同样地，这些高级接口模糊了许多底层操作，因此请参见[此笔记本](../modules/indexes/getting_started.ipynb)进行更低级别的漫步。


## 文档问答


Question answering involves fetching multiple documents, and then asking a question of them.

LLM响应将根据文件内容回答您的问题。


使用问答链的推荐方法是:


```python

from langchain.chains.question_answering import load_qa_chain

chain = load_qa_chain(llm, chain_type="stuff")

chain.run(input_documents=docs, question=query)

```



The following resources exist:



- [问答笔记本](../modules/chains/index_examples/question_answering.ipynb): 这是一篇教您如何完成这个任务的笔记本。
- [VectorDB 问答笔记本](../modules/chains/index_examples/vector_db_qa.ipynb): 这是一篇教您如何在向量数据库上进行问答的笔记本。当您有大量文件，并且不想将它们全部传递给LLM，而是想先在嵌入式向量中进行一些语义搜索时，这通常很有用。


## 添加资源


还有一种变体，除了回答问题外，语言模型还会引用其来源（例如，它使用了哪些传入的文件）。


使用问答及其来源链的推荐方法是:


```python

from langchain.chains.qa_with_sources import load_qa_with_sources_chain

chain = load_qa_with_sources_chain(llm, chain_type="stuff")

chain({"input_documents": docs, "question": query}, return_only_outputs=True)

```



The following resources exist:



- [带来源问答笔记本](../modules/chains/index_examples/qa_with_sources.ipynb): 这是一篇教您如何完成这个任务的笔记本。
- [VectorDB 带来源问答笔记本](../modules/chains/index_examples/vector_db_qa_with_sources.ipynb): 这是一篇教您如何在向量数据库上进行带来源问答的笔记本。当您有大量文件，并且不想将它们全部传递给LLM，而是想先在嵌入式向量中进行一些语义搜索时，这通常很有用。


## 其他相关资源


Additional related resources include:



- [文档处理工具](/modules/utils/how_to_guides.rst): 关于如何使用多个文档处理工具的指南，这些工具将会对此任务非常有帮助, 包括文本拆分器（用于拆分长文档）和Embeddings & Vectorstores（对于上面的Vector DB示例非常有用）。
-[合并文档链](/modules/indexes/combine_docs.md): 一种特定类型的链的概念概述，可以通过它来完成此任务。

## 全流程示例

要了解全流程操作示例， 请参阅以下资源:

- [Semantic search over a group chat with Sources Notebook](question_answering/semantic-search-over-chat.ipynb): A notebook that semantically searches over a group chat conversation.

