PGVector（PG向量）

本页面介绍如何在LangChain中使用Postgres PGVector](https://github.com/pgvector/pgvector)生态系统
它分为两个部分：安装和设置，然后参考特定的PGVector封装。

安装
- 使用`pip install pgvector`安装Python包


设置
1. 第一步是创建一个带有已安装`pgvector`扩展的数据库。

请按照PGVector安装步骤](https://github.com/pgvector/pgvector#installation)的步骤安装数据库和扩展。Docker镜像是最简单的入门方式。

封装

向量存储

存在一个围绕Postgres向量数据库的封装，使您可以将其用作向量存储，无论是用于语义搜索还是示例选择。
要导入此向量存储：


To import this vectorstore:

```python

from langchain.vectorstores.pgvector import PGVector

```


用法

有关PGVector封装的更详细的步骤，请参阅此笔记本](../modules/indexes/vectorstores/examples/pgvector.ipynb)
