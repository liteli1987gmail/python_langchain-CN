## Chroma（嵌入式AI应用数据库）


> [Chroma](https://docs.trychroma.com/getting-started)是一个用于嵌入式AI应用程序建模的数据库。


## 安装和设置


```bash
pip install chromadb

```





## VectorStore



存在一个Chroma向量数据库的包装器，允许您将其用作向量库，无论是用于语义搜索还是示例选择。
（注：Chroma向量数据库是一种非常适用于建立基于向量的应用程序的数据库。）


```python
from langchain.vectorstores import Chroma

```



更详细的Chroma包装器操作请参见 [此文档](../modules/indexes/vectorstores/getting_started.ipynb)


## 检索器


请查看 [使用示例](../modules/indexes/retrievers/examples/chroma_self_query.ipynb)。


```python

from langchain.retrievers import SelfQueryRetriever

```

