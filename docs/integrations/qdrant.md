# Qdrant

本页面介绍如何在LangChain内使用Qdrant生态系统。
它分为两个部分:安装和设置,然后引用特定的Qdrant包装器。

## 安装和设置
- 使用`pip install qdrant-client`安装Python SDK。
## 包装器

### VectorStore

存在一个围绕Qdrant索引的包装器，使您可以将其用作向量存储器，,进行语义搜索或示例选择。

要导入此向量存储器:，
```python
from qdrant_client import VectorIndex
from langchain.vectorstores import Qdrant

```


For a more detailed walkthrough of the Qdrant wrapper, see [this notebook](../modules/indexes/vectorstores/examples/qdrant.ipynb)

