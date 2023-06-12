# PGVector（PG向量）


This page covers how to use the Postgres [PGVector](https://github.com/pgvector/pgvector) ecosystem within LangChain（本页面介绍如何在LangChain中使用Postgres [PGVector](https://github.com/pgvector/pgvector)生态系统）
It is broken into two parts: installation and setup, and then references to specific PGVector wrappers.（本文分为两部分：安装和设置，然后引用特定的PGVector包装器。）


## Installation（安装）
- Install the Python package with `pip install pgvector`（使用`pip install pgvector`命令安装Python包）




## Setup（设置）
1. The first step is to create a database with the `pgvector` extension installed.（第一步是创建一个已安装`pgvector`扩展的数据库。）


    Follow the steps at [PGVector Installation Steps](https://github.com/pgvector/pgvector#installation) to install the database and the extension. The docker image is the easiest way to get started.



## Wrappers（包装器）


### VectorStore（向量存储）


There exists a wrapper around Postgres vector databases, allowing you to use it as a vectorstore,（存在一个Postgres向量数据库的包装器，可以让您将其用作向量存储）
whether for semantic search or example selection.（无论是进行语义搜索还是示例选择。）


To import this vectorstore:（导入此向量存储:）
```python
from langchain.vectorstores.pgvector import PGVector

```



### Usage（用法）


For a more detailed walkthrough of the PGVector Wrapper, see [this notebook](../modules/indexes/vectorstores/examples/pgvector.ipynb)

