AtlasDB
此页面介绍了如何在LangChain中使用Nomic的Atlas生态系统。
它分为两个部分：安装和设置，以及对特定Atlas包装器的引用。
 
安装和设置
 - 用`pip install nomic`安装Python包
 - Nomic也包含在langchains poetry extras `poetry install -E all`中
 
包装器
 
VectorStore
 
存在一个围绕Atlas神经数据库的包装器，它允许您将其用作VectorStore。
此VectorStore还为您提供对底层AtlasProject对象的完全访问权限，从而允许您使用Atlas地图交互的全部功能范围，如批量标记和自动主题建模。
请参阅Atlas文档](https://docs.nomic.ai/atlas_api.html)以获取更详细的信息。
 
 
 
 
 
 
导入此VectorStore:
```python

from langchain.vectorstores import AtlasDB

```

 
有关AtlasDB包装器的更详细说明，请参阅此笔记本](../modules/indexes/vectorstores/examples/atlas.ipynb)
