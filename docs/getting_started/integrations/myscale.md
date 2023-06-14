MyScale是什么



本页介绍如何在LangChain中使用MyScale向量数据库。

它分为两个部分：安装和设置，以及对特定MyScale包装器的引用。



使用MyScale，您可以管理结构化和非结构化（向量化）数据，并使用SQL对两种类型的数据执行联合查询和分析。此外，MyScale的基于ClickHouse的云原生OLAP架构使得即使在大规模数据集上也能实现闪电般快速的数据处理。



介绍



MyScale和高性能向量搜索概述](https://docs.myscale.com/en/overview/)



现在您可以在我们的SaaS上注册并立即启动集群！](https://docs.myscale.com/en/quickstart/)



如果您对我们如何将SQL和向量集成感兴趣，请参考此文档](https://docs.myscale.com/en/vector-reference/)以获取更多语法参考。



我们还提供有关huggingface的在线演示！请访问我们的huggingface空间](https://huggingface.co/myscale)！它们可以在瞬间搜索数百万个向量！



安装和设置

- 使用`pip install clickhouse-connect`安装Python SDK



设置环境



有两种方式来设置myscale索引的参数。



1. 环境变量



在运行应用程序之前，请使用`export`设置环境变量：

`export MYSCALE_URL='<your-endpoints-url>' MYSCALE_PORT=<your-endpoints-port> MYSCALE_USERNAME=<your-username> MYSCALE_PASSWORD=<your-password> ...`



您可以在我们的SaaS上轻松找到您的帐户、密码和其他信息。有关详细信息，请参阅此文档](https://docs.myscale.com/en/cluster-management/)

所有`MyScaleSettings`下的属性都可以使用前缀`MYSCALE_`来设置，且不区分大小写。



2. 使用参数创建`MyScaleSettings`对象





```python

from langchain.vectorstores import MyScale, MyScaleSettings

config = MyScaleSetting(host="<your-backend-url>", port=8443, ...)

index = MyScale(embedding_function, config)

index.add_documents(...)

```

  

包装器

支持的函数:

- `add_texts`

- `add_documents`

- `from_texts`

- `from_documents`

- `similarity_search`

- `asimilarity_search`

- `similarity_search_by_vector`

- `asimilarity_search_by_vector`

- `similarity_search_with_relevance_scores`



向量存储



MyScale数据库周围存在一个包装器，使您可以将其用作向量存储，

无论是用于语义搜索还是类似示例的检索。



导入此向量存储：

```python

from langchain.vectorstores import MyScale

```



有关MyScale包装器的更详细演示，请参阅此笔记本](../modules/indexes/vectorstores/examples/myscale.ipynb)

