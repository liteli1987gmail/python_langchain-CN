LanceDB



本页面介绍如何在LangChain中使用LanceDB](https://github.com/lancedb/lancedb)。

它分为两个部分：安装和设置，以及特定的LanceDB包装器的参考。



安装和设置



- 使用 `pip install lancedb` 安装Python SDK



包装器



向量存储



存在一个围绕LanceDB数据库的包装器，可以将其用作向量存储，

无论是用于语义搜索还是示例选择。



要导入此向量存储：



```python

from langchain.vectorstores import LanceDB

```



有关LanceDB包装器的详细演示，请参阅此笔记本](../modules/indexes/vectorstores/examples/lancedb.ipynb)

