# AtlasDB（Atlas数据库）


本页介绍如何在LangChain中使用Nomic的Atlas生态系统。
它被分成两部分：安装和设置（installation and setup），然后是对特定Atlas包装器的引用。


安装和设置
- 使用'pip install nomic'安装Python包。
- Nomic也包含在LangChain的poetry extras中的'poetry install -E all'中。


包装器


VectorStore


周围存在一个关于Atlas神经数据库的包装器，允许您将其用作矢量存储器。
这个矢量存储器还使您完全访问基础AtlasProject对象，这将允许您使用Atlas地图交互的全部范围，例如批量标记和自动主题建模。
有关更详细信息，请参见[Atlas文档](https://docs.nomic.ai/atlas_api.html)。










导入此矢量存储器：
```python
from langchain.vectorstores import AtlasDB

```



For a more detailed walkthrough of the AtlasDB wrapper, see [this notebook](../modules/indexes/vectorstores/examples/atlas.ipynb)

