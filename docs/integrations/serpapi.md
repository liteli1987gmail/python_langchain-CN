SerpAPI


本页包含如何在LangChain中使用SerpAPI搜索API的说明。
它分为两个部分——安装和设置，并引用特定的SerpAPI封装。


安装和设置
-使用`pip install google-search-results`安装要求
-获取SerpAPI API密钥并将其设置为环境变量(`SERPAPI_API_KEY`)


封装器


实用程序


存在SerpAPI实用程序包装器。导入此实用程序:


```python

from langchain.utilities import SerpAPIWrapper

```



有关此包装器的更详细演练，请参见[此笔记本](../modules/agents/tools/examples/serpapi.ipynb)。


工具


您还可以将此包装器轻松加载为工具(与代理一起使用)。
您可以通过以下方式完成：
```python

from langchain.agents import load_tools

tools = load_tools(["serpapi"])

```



For more information on this, see [this page](../modules/agents/tools/getting_started.md)

