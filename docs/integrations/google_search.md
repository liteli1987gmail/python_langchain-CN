# 谷歌搜索


本页面介绍如何在LangChain内部使用Google搜索API。

它分为两个部分：安装和设置，以及对特定的Google搜索封装的引用。



安装和设置
- 使用`pip install google-api-python-client`安装所需的依赖

- 按照[这些说明](https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search)设置自定义搜索引擎

- 从上一步骤获取API密钥和自定义搜索引擎ID，并将它们分别设置为环境变量`GOOGLE_API_KEY`和`GOOGLE_CSE_ID`



封装


实用工具


有一个GoogleSearchAPIWrapper实用工具可以封装此API。要导入此实用工具：



```python

from langchain.utilities import GoogleSearchAPIWrapper
```



有关此封装的更详细步骤，请参见[此笔记本](../modules/agents/tools/examples/google_search.ipynb)。



工具


您也可以将此封装程序轻松加载为工具（用于与Agent一起使用）。

您可以使用以下命令完成此操作：

```python

from langchain.agents import load_tools
tools = load_tools(["google-search"])

```



有关更多信息，请参见[此页面](../modules/agents/tools/getting_started.md)

