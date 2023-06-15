# ClickHouse 点击房



本页介绍如何在LangChain中使用ClickHouse矢量搜索。



[ClickHouse](https://clickhouse.com) is a open source real-time OLAP database with full SQL support and a wide range of functions to assist users in writing analytical queries. Some of these functions and data structures perform distance operations between vectors, enabling ClickHouse to be used as a vector database. [ClickHouse](https://clickhouse.com)是一个开源的实时OLAP数据库，具有完整的SQL支持和广泛的功能，可以帮助用户编写分析查询。其中一些功能和数据结构可以在向量之间执行距离操作，使得ClickHouse可以用作矢量数据库。



Due to the fully parallelized query pipeline, ClickHouse can process vector search operations very quickly, especially when performing exact matching through a linear scan over all rows, delivering processing speed comparable to dedicated vector databases. 由于完全并行化的查询管道，ClickHouse可以非常快速地处理矢量搜索操作，特别是在通过线性扫描所有行进行精确匹配时，可以提供与专用矢量数据库相媲美的处理速度。



High compression levels, tunable through custom compression codecs, enable very large datasets to be stored and queried. ClickHouse is not memory-bound, allowing multi-TB datasets containing embeddings to be queried. 高度可调的压缩级别通过自定义压缩编解码器使得能够存储和查询非常大的数据集。ClickHouse不受内存限制，可以查询包含嵌入内容的TB级数据集。



The capabilities for computing the distance between two vectors are just another SQL function and can be effectively combined with more traditional SQL filtering and aggregation capabilities. This allows vectors to be stored and queried alongside metadata, and even rich text, enabling a broad array of use cases and applications. 计算两个向量之间距离的能力只是另一个SQL函数，可以有效地与更传统的SQL过滤和聚合功能结合使用。这可以允许向量与元数据以及丰富的文本一起存储和查询，从而实现广泛的用例和应用。



Finally, experimental ClickHouse capabilities like [Approximate Nearest Neighbour (ANN) indices](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/annindexes) support faster approximate matching of vectors and provide a promising development aimed to further enhance the vector matching capabilities of ClickHouse. 最后，实验性的ClickHouse功能，如[近似最近邻（ANN）索引](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/annindexes)，支持更快速的向量近似匹配，并提供了一个有望进一步增强ClickHouse矢量匹配能力的有前途的功能。



## 安装 Installation

- 通过[二进制](https://clickhouse.com/docs/en/install)或者[镜像](https://hub.docker.com/r/clickhouse/clickhouse-server/)方式安装ClickHouse服务器 Install clickhouse server by [binary](https://clickhouse.com/docs/en/install) or [docker image](https://hub.docker.com/r/clickhouse/clickhouse-server/)

- 使用`pip install clickhouse-connect`命令安装Python SDK Install the Python SDK with `pip install clickhouse-connect`



### 配置clickhouse vector index Configure clickhouse vector index



自定义`ClickhouseSettings`对象及参数 Customize `ClickhouseSettings` object with parameters



    ```python

    from langchain.vectorstores import ClickHouse, ClickhouseSettings

    config = ClickhouseSettings(host="<clickhouse-server-host>", port=8123, ...)

    index = Clickhouse(embedding_function, config)

    index.add_documents(...)

    ```

  

## 封装器 Wrappers

支持的函数 supported functions:

- `add_texts`  添加文本

- `add_documents`  添加文档

- `from_texts`  从文本创建

- `from_documents`  从文档创建

- `similarity_search`  相似性搜索

- `asimilarity_search`  相似性搜索

- `similarity_search_by_vector`  通过向量进行相似性搜索

- `asimilarity_search_by_vector`  通过向量进行相似性搜索

- `similarity_search_with_relevance_scores`  通过相关分数进行相似性搜索



### VectorStore 矢量存储



There exists a wrapper around open source Clickhouse database, allowing you to use it as a vectorstore,

whether for semantic search or similar example retrieval. 现有一个围绕开源Clickhouse数据库的封装器，允许您将其用作矢量存储，无论是用于语义搜索还是类似示例检索。



To import this vectorstore:

```python

from langchain.vectorstores import Clickhouse

```



For a more detailed walkthrough of the MyScale wrapper, see [this notebook](../modules/indexes/vectorstores/examples/clickhouse.ipynb) 有关MyScale封装器的更详细的步骤，请参阅[此笔记本](../modules/indexes/vectorstores/examples/clickhouse.ipynb)

