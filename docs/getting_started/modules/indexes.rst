索引
==========================



注意：
   `概念指南 <https://docs.langchain.com/docs/components/indexing>`_





**索引** 指的是结构化文档的方法，以便于LLMs能够最好地与它们交互。



索引在链中最常见的用途是在“检索”步骤中使用。

此步骤是指获取用户的查询并返回最相关的文档。

我们之所以做出这种区分，是因为（1）索引可以用于除检索以外的其他事情，并且

（2）检索可以使用除索引以外的其他逻辑来查找相关文档。

因此，我们有一个**Retriever** 接口的概念 - 这是大多数链所使用的接口。



大多数情况下，当我们谈论索引和检索时，我们正在谈论索引和检索

非结构化数据（例如文本文档）。

要与结构化数据（SQL 表等）或 API 进行交互，请参阅相应的用例

章节，了解相关功能的链接。



|

- `入门 <./indexes/getting_started.html>`_：索引的概述。





索引类型

---------------------



- `文档加载程序 <./indexes/document_loaders.html>`_：如何从各种来源加载文档。



- `文本拆分器 <./indexes/text_splitters.html>`_：**文本拆分器** 的概述和不同类型。



- `向量存储 <./indexes/vectorstores.html>`_： **向量存储** 的概述和不同类型。



- `检索器 <./indexes/retrievers.html>`_：**检索器** 的概述和不同类型。







.. toctree::

   :maxdepth: 1

   :hidden:



   ./indexes/getting_started.ipynb

   ./indexes/document_loaders.rst

   ./indexes/text_splitters.rst

   ./indexes/vectorstores.rst

   ./indexes/retrievers.rst



