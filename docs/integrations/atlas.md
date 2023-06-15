# AtlasDB



本页介绍如何在LangChain中使用Nomic的Atlas生态系统。

它分为两部分：安装和设置，以及对特定Atlas包装器的引用。



## 安装和设置

- 使用`pip install nomic`安装Python包

- Nomic也包含在langchains poetry extras中，使用`poetry install -E all`安装



## 包装器



### VectorStore



存在一个围绕Atlas神经数据库的包装器，允许您将其用作向量存储库。

此向量存储库还提供了对底层AtlasProject对象的完全访问权限，这将允许您使用Atlas地图交互的全部功能，例如批量标记和自动主题建模。

请参阅[Atlas文档](https://docs.nomic.ai/atlas_api.html)获取更详细的信息。











要导入此向量存储库，请执行以下操作：

```python

from langchain.vectorstores import AtlasDB

```



有关AtlasDB包装器的更详细说明，请参阅[此笔记本](../modules/indexes/vectorstores/examples/atlas.ipynb)

