# Wolfram Alpha（沃尔夫拉姆阿尔法）


>[WolframAlpha](https://en.wikipedia.org/wiki/WolframAlpha)是由沃尔夫拉姆研究公司开发的回答引擎。 
> 它通过计算从外部数据源获得的答案来回答客观查询。


本页介绍如何在LangChain中使用`Wolfram Alpha API`。


## 安装和设置
- 通过以下命令安装所需项目：
```bash
pip install wolframalpha

```

- 前往沃尔夫拉姆阿尔法开发者账户并注册[此处](https://developer.wolframalpha.com/)
- 创建应用程序并获取您的`APP ID`。
- 将APP ID设置为环境变量`WOLFRAM_ALPHA_APPID`




## 封装器


### 工具


存在一个名为WolframAlphaAPIWrapper的实用程序包装器可以包装此API。 要导入此实用程序，请使用以下代码：


```python
from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper

```



有关此封装器更详细的演练，请参见[此笔记本](../modules/agents/tools/examples/wolfram_alpha.ipynb)。


### 工具


您还可以轻松地将此包装器作为工具加载（与代理一起使用）。 您可以使用以下代码执行此操作：
You can do this with:

```python
from langchain.agents import load_tools

tools = load_tools(["wolfram-alpha"])

```



For more information on this, see [this page](../modules/agents/tools/getting_started.md)

