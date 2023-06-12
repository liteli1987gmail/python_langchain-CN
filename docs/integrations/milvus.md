# Milvus


本页面介绍如何在LangChain中使用Milvus生态系统。
它被分为两部分:安装和设置，以及特定Milvus包装的参考。


## 安装和设置
- 使用 `pip install pymilvus` 安装Python SDK
## 包装器


### VectorStore


存在一个Milvus索引的包装器，使您可以将其用作矢量存储，无论是用于语义搜索还是示例选择。



要导入此矢量存储:，请执行以下操作
```python
from langchain.vectorstores import Milvus

```



For a more detailed walkthrough of the Miluvs wrapper, see [this notebook](../modules/indexes/vectorstores/examples/milvus.ipynb)

