## OpenSearch（OpenSearch）

本页面介绍如何在LangChain中使用OpenSearch生态系统。
它分为两个部分，安装和设置，并提供对特定OpenSearch包装器的引用。

## 安装和设置
- 使用`pip install opensearch-py`安装Python包
## 包装器

### VectorStore(向量存储)

存在一种围绕OpenSearch向量数据库的包装器，可让您将其用作用于近似向量搜索的语义搜索向量存储库，使用lucene、nmslib和faiss引擎，或使用无痛脚本和脚本评分函数进行bruteforce向量搜索。

要导入此向量存储：

```python
```python

from langchain.vectorstores import OpenSearchVectorSearch

```


For a more detailed walkthrough of the OpenSearch wrapper, see [this notebook](../modules/indexes/vectorstores/examples/opensearch.ipynb)

