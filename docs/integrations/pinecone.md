# 松果


本页面介绍如何在LangChain中使用松果生态系统。
分为两部分：安装和设置，然后引用特定的松果封装。


## 安装和设置
安装Python SDK:
```bash

pip install pinecone-client

```





## Vectorstore


存在一个Pinecone索引的封装，使您可以将其用作矢量存储,
无论是用于语义搜索还是示例选择。


```python

from langchain.vectorstores import Pinecone

```



For a more detailed walkthrough of the Pinecone vectorstore, see [this notebook](../modules/indexes/vectorstores/examples/pinecone.ipynb)

