ClickHouse


本页面介绍如何在LangChain中使用ClickHouse矢量搜索功能。


ClickHouse](https://clickhouse.com)是一个开源的实时OLAP数据库，具备完全的SQL支持和多种函数，可帮助用户编写分析查询。其中一些函数和数据结构执行向量之间的距离计算操作，使得ClickHouse可以用作向量数据库。


由于完全并行化的查询流程，ClickHouse可以非常快速地处理向量搜索操作，尤其是在通过线性扫描所有行执行精确匹配时，其处理速度可与专用向量数据库相媲美。


高度可压缩的数据集（通过自定义压缩编解码器进行调整）可存储和查询非常大的数据集。ClickHouse并不受内存限制，可以查询包含嵌入式向量的多TB数据集。


计算两个向量之间的距离的能力只是另一个SQL函数，可以与更传统的SQL过滤和聚合功能有效结合。这使得向量可以与元数据、甚至富文本一起存储和查询，从而实现广泛的用例和应用。


最后，ClickHouse的实验性功能，如近似最近邻（ANN）索引](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/annindexes)，支持更快速的向量近似匹配，并提供了一个有希望提升ClickHouse向量匹配能力的发展方向。


安装
- 通过二进制文件](https://clickhouse.com/docs/en/install)或docker镜像](https://hub.docker.com/r/clickhouse/clickhouse-server/)安装ClickHouse服务器
- 使用`pip install clickhouse-connect`安装Python SDK


配置clickhouse向量索引


使用参数自定义`ClickhouseSettings`对象


    ```python

    from langchain.vectorstores import ClickHouse, ClickhouseSettings

    config = ClickhouseSettings(host="<clickhouse-server-host>", port=8123, ...)

    index = Clickhouse(embedding_function, config)

    index.add_documents(...)

    ```

  

## Wrappers

supported functions:

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



存在一个开源Clickhouse数据库的包装器，允许您将其用作向量存储
无论是用于语义搜索还是类似示例检索


导入此向量存储
```python

from langchain.vectorstores import Clickhouse

```



有关MyScale包装器的更详细使用说明，请参阅此笔记本](../modules/indexes/vectorstores/examples/clickhouse.ipynb)
