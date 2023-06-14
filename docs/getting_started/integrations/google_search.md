谷歌搜索



本页面介绍如何在LangChain中使用谷歌搜索API。

它分为两部分：安装和设置，以及对特定谷歌搜索包装器的引用。



安装和设置

- 使用`pip install google-api-python-client`安装必要的依赖

- 按照这些说明](https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search)设置自定义搜索引擎

- 从上一步骤获取API密钥和自定义搜索引擎ID，并将其分别设置为环境变量`GOOGLE_API_KEY`和`GOOGLE_CSE_ID`



包装器



实用工具



存在一个名为GoogleSearchAPIWrapper的实用工具，它包装了这个API。要导入这个工具：



```python

from langchain.utilities import GoogleSearchAPIWrapper

```



有关这个包装器的更详细演示，请参阅这个笔记本](../modules/agents/tools/examples/google_search.ipynb)。



工具



您还可以将此包装器轻松加载为工具（与代理一起使用）。

您可以通过以下方式实现：

```python

from langchain.agents import load_tools

tools = load_tools(["google-search"])

```



有关更多信息，请参阅此页面](../modules/agents/tools/getting_started.md)

