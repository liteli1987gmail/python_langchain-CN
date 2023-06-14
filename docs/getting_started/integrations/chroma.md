Chroma（https://docs.trychroma.com/getting-started）是一个用于构建带有嵌入向量的AI应用程序的数据库。

安装和设置

## 安装和设置

```bash

pip安装chromadb
```



## VectorStore

存在一个Chroma向量数据库的包装器，允许您将其用作向量存储，无论是用于语义搜索还是示例选择。
无论是用于语义搜索还是示例选择。

```python

from langchain.vectorstores import Chroma

```


有关Chroma包装器的更详细操作说明，请参见此笔记本](../modules/indexes/vectorstores/getting_started.ipynb)

## 检索器

查看使用示例](../modules/indexes/retrievers/examples/chroma_self_query.ipynb)。

```python

from langchain.retrievers import SelfQueryRetriever

```

