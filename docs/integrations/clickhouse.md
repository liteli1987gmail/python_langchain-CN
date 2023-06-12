ClickHouse（点击房子）


本页介绍如何在LangChain中使用ClickHouse Vector Search。


[ClickHouse](https://clickhouse.com)是一款开源实时OLAP数据库，具有完整的SQL支持和广泛的函数，以帮助用户编写分析查询。其中一些函数和数据结构执行向量之间的距离操作，使得ClickHouse成为向量数据库的选择之一。


由于完全并行化的查询管道，ClickHouse可以非常快地处理向量搜索操作，特别是在通过线性扫描所有行进行精确匹配时，可以提供与专用向量数据库相当的处理速度。


高压缩级别，可以通过定制的压缩编解码器进行调整，使得非常大的数据集能够被存储和查询。ClickHouse不受内存限制，可以查询包含嵌入向量的多个TB数据集。


计算两个向量之间距离的能力仅是另一个SQL函数，可以有效地与更传统的SQL过滤和聚合功能相结合。这允许向量与元数据以及甚至富文本一起存储和查询，从而实现广泛的用例和应用。


最后，实验性的ClickHouse功能，比如[近似最近邻（ANN）索引](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/annindexes)，支持更快的向量近似匹配，并提供有望进一步增强ClickHouse向量匹配能力的发展。


安装
- Install clickhouse server by [binary](https://clickhouse.com/docs/en/install) or [docker image](https://hub.docker.com/r/clickhouse/clickhouse-server/)

使用 `pip install clickhouse-connect` 安装 Python SDK


### 配置 Clickhouse 向量索引


使用自定义参数配置 `ClickhouseSettings` 对象


    ```python

    from langchain.vectorstores import ClickHouse, ClickhouseSettings

    config = ClickhouseSettings(host="<clickhouse-server-host>", port=8123, ...)

    index = Clickhouse(embedding_function, config)

    index.add_documents(...)

    ```

  

## 包装函数
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


### VectorStore


有一个 MyScale 的包装器可以让你将开源的 Clickhouse 数据库作为向量存储使用，用于语义搜索或类似的示例检索



导入此向量存储:
```python
from langchain.vectorstores import Clickhouse

```



For a more detailed walkthrough of the MyScale wrapper, see [this notebook](../modules/indexes/vectorstores/examples/clickhouse.ipynb)

