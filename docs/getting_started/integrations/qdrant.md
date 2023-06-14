Qdrant



本页面介绍如何在LangChain中使用Qdrant生态系统。

它分为两部分：安装和设置，以及对特定的Qdrant包装器的引用。



安装和设置

- 使用`pip install qdrant-client`安装Python SDK

包装器



VectorStore



存在一个围绕Qdrant索引的包装器，允许您将其用作向量存储，

无论是用于语义搜索还是示例选择。



要导入这个向量存储：

```python

from langchain.vectorstores import Qdrant

```



有关Qdrant包装器的更详细演示，请参见这个notebook](../modules/indexes/vectorstores/examples/qdrant.ipynb)
