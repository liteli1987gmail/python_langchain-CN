## MyScale


本页介绍如何在LangChain中使用MyScale向量数据库。
它被分为两个部分：安装和设置，然后引用特定的MyScale包装器。


使用MyScale，您可以管理结构化和非结构化（向量化）数据，并使用SQL对两种类型的数据执行联合查询和分析。此外，MyScale的基于ClickHouse的云本机OLAP架构可在大型数据集上实现极快的数据处理。


## 介绍


[MyScale和高性能向量搜索概述](https://docs.myscale.com/en/overview/)


现在，您可以在我们的SaaS上注册并[立即启动群集！](https://docs.myscale.com/en/quickstart/)


如果您也对我们如何将SQL和向量集成感兴趣，请参阅[此文档](https://docs.myscale.com/en/vector-reference/)获取更详细的语法参考。


我们还提供了基于huggingface的现场演示！请查看我们的[huggingface空间](https://huggingface.co/myscale)！他们可以在眨眼之间搜索数百万个向量！


## 安装和设置
- 使用`pip install clickhouse-connect`安装Python SDK


### 设置环境


有两种设置myscale指数参数的方法。


1.环境变量


    Before you run the app, please set the environment variable with `export`:

    `export MYSCALE_URL='<your-endpoints-url>' MYSCALE_PORT=<your-endpoints-port> MYSCALE_USERNAME=<your-username> MYSCALE_PASSWORD=<your-password> ...`

2.使用参数创建`MyScaleSettings`对象
    You can easily find your account, password and other info on our SaaS. For details please refer to [this document](https://docs.myscale.com/en/cluster-management/)

    Every attributes under `MyScaleSettings` can be set with prefix `MYSCALE_` and is case insensitive.



2. Create `MyScaleSettings` object with parameters





    ```python

    from langchain.vectorstores import MyScale, MyScaleSettings

    config = MyScaleSetting(host="<your-backend-url>", port=8443, ...)

    index = MyScale(embedding_function, config)

    index.add_documents(...)

    ```

  

## 包装器
支持的函数：
- `add_texts`
- `add_documents`
- `from_texts`
- `from_documents`
- `similarity_search`
- `asimilarity_search`
- `similarity_search_by_vector`
- `asimilarity_search_by_vector`

- `similarity_search_with_relevance_scores`

### VectorStore（向量数据仓库）

这里有一个MyScale数据库的封装，允许你将其用作向量数据仓库，无论是用于语义搜索还是类似的示例检索。

要导入这个向量数据仓库：
```python
...
from langchain.vectorstores import MyScale

```


For a more detailed walkthrough of the MyScale wrapper, see [this notebook](../modules/indexes/vectorstores/examples/myscale.ipynb)

