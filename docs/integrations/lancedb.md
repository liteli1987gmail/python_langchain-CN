# LanceDB 安装和设置


这个页面介绍如何在LangChain中使用[LanceDB](https://github.com/lancedb/lancedb)。

它分为两部分：安装和设置，以及对特定LanceDB包装器的引用。



## 安装和设置



- 使用 `pip install lancedb` 安装Python SDK



## 包装器



### VectorStore



存在一个LanceDB数据库的包装器，可用于作为矢量存储，
无论是用于语义搜索还是示例选择。



要导入这个矢量存储：



```python

from langchain.vectorstores import LanceDB

```



有关LanceDB包装器的更详细介绍，请参阅[此笔记本](../modules/indexes/vectorstores/examples/lancedb.ipynb)

