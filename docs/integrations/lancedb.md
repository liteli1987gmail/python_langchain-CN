# LanceDB（Lance 数据库）

本页面介绍如何在 LangChain 中使用 [LanceDB](https://github.com/lancedb/lancedb)。
它分为两部分：安装和设置，,然后是对特定 LanceDB 封装的引用。

## 安装和设置

- 用 `pip install lancedb` 安装 Python SDK。

## 封装

### VectorStore

有一个 LanceDB 数据库的封装，允许您将其用作向量库，,无论用于语义搜索还是示例选择。

要导入此向量库:

```python
```python

from langchain.vectorstores import LanceDB

```


For a more detailed walkthrough of the LanceDB wrapper, see [this notebook](../modules/indexes/vectorstores/examples/lancedb.ipynb)

