# Google BigQuery谷歌 大型查询


>[Google BigQuery](https://cloud.google.com/bigquery) is a serverless and cost-effective enterprise data warehouse that works across clouds and scales with your data.“谷歌大型查询”是一种无服务器、经济实惠且可横向扩展的企业数据仓库，可跨多个云平台操作和扩展。
`BigQuery` is a part of the `Google Cloud Platform`.“BigQuery”是“谷歌云平台”的一部分。


## Installation and Setup安装和设置


First, you need to install `google-cloud-bigquery` python package.首先，需要安装 `google-cloud-bigquery` 的 Python 包。


```bash

pip install google-cloud-bigquery

```



## Document Loader文档加载器


See a [usage example](../modules/indexes/document_loaders/examples/google_bigquery.ipynb).请参阅 [使用示例](../modules/indexes/document_loaders/examples/google_bigquery.ipynb)。


```python

from langchain.document_loaders import BigQueryLoader

```

