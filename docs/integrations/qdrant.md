# Qdrant Qdrant



本页介绍在LangChain中如何使用Qdrant生态系统。

它分为两部分：安装和设置，然后是特定Qdrant封装的参考。



## 安装和设置

- 使用`pip install qdrant-client`安装Python SDK。

## 封装



### VectorStore



存在一个封装Qdrant索引的包装器，使您可以将其用作矢量存储，用于语义搜索或示例选择。



要导入此VectorStore：



```python

from langchain.vectorstores import Qdrant

```



有关Qdrant封装的更详细介绍，请参阅[此笔记本](../modules/indexes/vectorstores/examples/qdrant.ipynb)

