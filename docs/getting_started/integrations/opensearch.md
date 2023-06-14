OpenSearch 搜索引擎


本页介绍如何在LangChain中使用OpenSearch生态系统。
它分为两部分：安装和设置，以及特定OpenSearch封装的参考内容。


安装和设置
- 使用 `pip install opensearch-py` 安装Python包
封装器


向量存储


有一个围绕OpenSearch向量数据库的封装器，允许您将其作为向量存储使用
用于通过lucene、nmslib和faiss引擎提供的近似向量搜索进行语义搜索
或使用无痛脚本和脚本评分功能进行暴力向量搜索。


要导入此向量存储：
```python

from langchain.vectorstores import OpenSearchVectorSearch

```



有关OpenSearch封装器的更详细步骤，请参阅此笔记本](../modules/indexes/vectorstores/examples/opensearch.ipynb)
