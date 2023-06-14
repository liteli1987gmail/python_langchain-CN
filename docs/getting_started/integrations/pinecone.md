松果


本页面介绍了如何在LangChain中使用松果生态系统。
它分为两部分：安装和设置，以及特定松果包装器的参考。


安装和设置
安装Python SDK：
```bash

pip安装松果客户端
```





向量存储


存在一个围绕松果索引的包装器，使您可以将其用作向量存储，
无论是用于语义搜索还是示例选择。


```python

from langchain.vectorstores import Pinecone

```



有关更详细的松果向量存储演示，请参阅此笔记本](../modules/indexes/vectorstores/examples/pinecone.ipynb)
