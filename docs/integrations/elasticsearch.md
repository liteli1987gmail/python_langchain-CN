Elasticsearch



>Elasticsearch](https://www.elastic.co/elasticsearch/) 是一个分布式的、RESTful的搜索和分析引擎。

> 它提供了一个分布式的、多租户能力的全文搜索引擎，具有HTTP web接口和无模式的

> JSON documents。





安装和设置



```bash

pip install elasticsearch

```



检索器



>在信息检索领域，Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25)是一种由搜索引擎用于估计文档与给定搜索查询的相关性的排名函数。它基于20世纪70年代和80年代由Stephen E. Robertson、Karen Spärck Jones等人开发的概率检索框架。



>实际排名函数的名称是BM25。全名Okapi BM25包括第一个使用它的系统的名称，即80年代和90年代在伦敦城市大学实施的Okapi信息检索系统。BM25及其较新的变体，如BM25F（可以考虑文档结构和锚文本的BM25版本），代表文档检索中使用的类似于TF-IDF的检索函数。



查看一个使用示例](../modules/indexes/retrievers/examples/elastic_search_bm25.ipynb)。



```python

from langchain.retrievers import ElasticSearchBM25Retriever

```

