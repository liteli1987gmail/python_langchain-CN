SerpAPI

本页面介绍了如何在LangChain中使用SerpAPI搜索API。
它分为两个部分：安装和设置，以及对特定SerpAPI包装器的引用。

安装和设置
- 使用`pip install google-search-results`安装必备条件
- 获取SerpAPI API密钥，并将其设置为环境变量（`SERPAPI_API_KEY`）

包装器

实用工具

存在一个将此API包装起来的SerpAPI实用程序。要导入此实用程序：

```python

from langchain.utilities import SerpAPIWrapper

```


有关此包装器的更详细演示，请参阅此笔记本](../modules/agents/tools/examples/serpapi.ipynb)。

工具

您还可以将此包装器轻松加载为工具（用于与Agent一起使用）
您可以使用以下方式完成：
```python

from langchain.agents import load_tools

tools = load_tools(["serpapi"])

```


有关更多信息，请参阅此页面](../modules/agents/tools/getting_started.md)
