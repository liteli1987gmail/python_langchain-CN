Milvus


本页面介绍如何在LangChain中使用Milvus生态系统。
它分为两个部分：安装和设置，以及特定Milvus封装的参考资料。


安装和设置
- 使用`pip install pymilvus`安装Python SDK
封装器


VectorStore


存在一个围绕Milvus索引的封装器，使您可以将其用作向量存储，
无论是用于语义搜索还是示例选择。


要导入此向量存储：
```python

from langchain.vectorstores import Milvus

```



有关Miluvs封装器的更详细步骤，请参阅此笔记本](../modules/indexes/vectorstores/examples/milvus.ipynb)。
