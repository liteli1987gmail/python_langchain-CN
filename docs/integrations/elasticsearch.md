# Elasticsearch 搜索引擎



>[Elasticsearch](https://www.elastic.co/elasticsearch/) 是一个分布式的、RESTful的搜索和分析引擎。

>它提供了一个带有HTTP网页界面和无模式（schema-free）JSON文档的分布式、多租户可用的全文搜索引擎。

>JSON文档。





## 安装和设置



```bash

pip install elasticsearch

```



## Retriever 检索器



>在信息检索中，[Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25)（BM是最佳匹配的缩写）是一种搜索引擎使用的排名函数，用于估计文档与给定搜索查询的相关性。它基于20世纪70年代和80年代由Stephen E. Robertson，Karen Spärck Jones等人开发的概率检索框架。



>实际排名函数的名称是BM25。更完整的名称是Okapi BM25，包括第一个使用它的系统的名称，这是在20世纪80年代和90年代实施在伦敦的城市大学的Okapi信息检索系统。BM25及其较新的变体，例如BM25F（可以考虑文档结构和锚文本的BM25版本），表示文档检索中使用的类似于TF-IDF的检索函数。



查看[使用示例](../modules/indexes/retrievers/examples/elastic_search_bm25.ipynb)。



```python

from langchain.retrievers import ElasticSearchBM25Retriever

```

