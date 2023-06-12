# 谷歌搜索

本页介绍如何在LangChain中使用谷歌搜索API。
它分为两个部分:安装和设置以及对特定谷歌搜索包装器的引用。

## 安装和设置
- 通过'pip install google-api-python-client'安装要求
- 遵循[这些说明](https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search)设置自定义搜索引擎
- 从前一步骤中获取API密钥和自定义搜索引擎ID，将它们设置为环境变量'GOOGLE_API_KEY'和'GOOGLE_CSE_ID'

## 包装器

### 实用工具

存在一个GoogleSearchAPIWrapper实用程序，它包装了此API。要导入此实用程序:

```python
from langchain.utilities import GoogleSearchAPIWrapper

```


有关此包装器的更详细演练，请参见[此笔记本电脑](../modules/agents/tools/examples/google_search.ipynb)。

### 工具

您还可以将此包装器轻松加载为工具（以与代理一起使用）。
你可以用这个做:
```python
from langchain.agents import load_tools

tools = load_tools(["google-search"])

```


For more information on this, see [this page](../modules/agents/tools/getting_started.md)

