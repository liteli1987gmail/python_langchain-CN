# Milvus



本页介绍如何在LangChain中使用Milvus生态系统。

它分为两部分：安装和设置，然后引用到特定的Milvus包装器。



## 安装和设置

- 使用`pip install pymilvus`安装Python SDK

## 包装器



### VectorStore



有一个围绕Milvus索引的包装器，您可以将其用作向量存储，

无论是用于语义搜索还是示例选择。



导入这个向量存储：

```python

from langchain.vectorstores import Milvus

```



有关Miluvs包装器的更详细说明，请参阅[此笔记本](../modules/indexes/vectorstores/examples/milvus.ipynb)

