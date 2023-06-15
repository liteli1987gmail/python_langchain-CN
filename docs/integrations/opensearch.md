# OpenSearch



本页面介绍如何在LangChain中使用OpenSearch生态系统。

它分为两部分：安装和设置，以及特定OpenSearch包装器的参考。



## 安装和设置

- 使用 'pip install opensearch-py' 安装Python包

## 包装器



### VectorStore



存在一个围绕OpenSearch向量数据库的包装器，可以将其用作向量库，

用于使用基于lucene，nmslib和faiss引擎的近似向量搜索进行语义搜索

或使用无痛脚本和脚本评分函数进行蛮力向量搜索。



要导入此向量库：

```python

from langchain.vectorstores import OpenSearchVectorSearch

```



有关OpenSearch包装器的更详细演示，请参阅[此笔记本](../modules/indexes/vectorstores/examples/opensearch.ipynb)

