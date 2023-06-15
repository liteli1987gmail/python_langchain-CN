# PGVector

本页面介绍了如何在LangChain中使用Postgres [PGVector](https://github.com/pgvector/pgvector)生态系统
它分为两个部分：安装和设置，然后引用特定的PGVector包装器。

## 安装
- 使用`pip install pgvector`安装Python包


## 设置
1. 第一步是创建一个已安装`pgvector`扩展的数据库。

    按照[PGVector安装步骤](https://github.com/pgvector/pgvector#installation)的步骤安装数据库和扩展。Docker镜像是最简单的入门方式。

## 包装器

### VectorStore

存在一个围绕Postgres矢量数据库的包装器，允许您将其用作矢量存储。
无论是用于语义搜索还是示例选择。

要导入此矢量存储：
```python

from langchain.vectorstores.pgvector import PGVector
```


### 用法

有关PGVector包装器的更详细演练，请参阅[此笔记本](../modules/indexes/vectorstores/examples/pgvector.ipynb)
