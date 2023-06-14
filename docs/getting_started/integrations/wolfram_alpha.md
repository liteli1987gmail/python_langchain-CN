Wolfram Alpha

> WolframAlpha](https://en.wikipedia.org/wiki/WolframAlpha)是由Wolfram Research开发的答案引擎。
> 它通过计算外部数据的答案来回答事实查询。

此页面介绍了如何在LangChain内使用Wolfram Alpha API。

安装和设置
- 使用以下命令安装要求
```bash

pip install wolframalpha
```

- 前往wolfram alpha并注册开发者帐户这里](https://developer.wolframalpha.com/)
- 创建一个应用程序并获取您的APP ID
- 将您的APP ID设置为环境变量WOLFRAM_ALPHA_APPID


包装器

实用工具

存在一个名为WolframAlphaAPIWrapper的实用工具，它封装了这个API。要导入此实用程序：

```python

from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper

```


有关此包装器的更详细示例，请参见此笔记本](../modules/agents/tools/examples/wolfram_alpha.ipynb)。

工具

您还可以将此包装器轻松加载为工具（用于与代理一起使用）。
您可以使用以下方式实现：
```python

from langchain.agents import load_tools

tools = load_tools(["wolfram-alpha"])

```


有关更多信息，请参见此页面](../modules/agents/tools/getting_started.md)
