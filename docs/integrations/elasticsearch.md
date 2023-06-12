# Elasticsearch说明：Elasticsearch


>[Elasticsearch](https://www.elastic.co/elasticsearch/) is a distributed, RESTful search and analytics engine. 说明：Elasticsearch是一个分布式的RESTful搜索和分析引擎。
> It provides a distributed, multi-tenant-capable full-text search engine with an HTTP web interface and schema-free 说明：它提供了一个分布式的多租户全文搜索引擎，具有HTTP web界面和无模式的特点。
> JSON documents.说明：JSON文档。




## Installation and Setup说明：安装和设置


```bash

pip install elasticsearch

```



## Retriever



>In information retrieval, [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25) (BM is an abbreviation of best matching) is a ranking function used by search engines to estimate the relevance of documents to a given search query. It is based on the probabilistic retrieval framework developed in the 1970s and 1980s by Stephen E. Robertson, Karen Spärck Jones, and others. 说明：在信息检索中，,Okapi BM25》（BM是“best matching”的缩写）是搜索引擎使用的一种排名函数，用于估计文档与给定搜索查询的相关性。它基于由Stephen E. Robertson、Karen Spärck Jones等人在1970年代和1980年代开发的概率检索框架。


>The name of the actual ranking function is BM25. The fuller name, Okapi BM25, includes the name of the first system to use it, which was the Okapi information retrieval system, implemented at London's City University in the 1980s and 1990s. BM25 and its newer variants, e.g. BM25F (a version of BM25 that can take document structure and anchor text into account), represent TF-IDF-like retrieval functions used in document retrieval.说明：实际排名函数的名称是BM25。完整的名称Okapi BM25包括第一个使用它的系统的名称，即在1980年代和1990年代实施的伦敦城市大学的Okapi信息检索系统。BM25及其新版本（如可以考虑文档结构和锚文本的BM25F）代表用于文档检索的类似TF-IDF的检索函数。


See a [usage example](../modules/indexes/retrievers/examples/elastic_search_bm25.ipynb).说明：请参见一个用法示例。


```python

from langchain.retrievers import ElasticSearchBM25Retriever

```

