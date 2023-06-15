# 松果 pinecone



本页面介绍如何在LangChain中使用松果生态系统。

它分为两部分：安装和设置，以及特定松果包装器的参考。



## 安装和设置

安装Python SDK：

```bash

pip install pinecone-client

```





## Vectorstore



存在一个围绕松果索引的包装器，可以将其用作向量库，

无论是用于语义搜索还是示例选择。



```python

from langchain.vectorstores import Pinecone

```



有关松果向量库的更详细说明，请参阅[此笔记本](../modules/indexes/vectorstores/examples/pinecone.ipynb)

