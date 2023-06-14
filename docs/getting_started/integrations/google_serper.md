谷歌Serper


本页介绍如何在LangChain中使用Serper](https://serper.dev)谷歌搜索API。Serper是一个低成本的谷歌搜索API，可用于从谷歌搜索中添加答案框、知识图和有机结果数据。
它分为两个部分：设置和对特定谷歌Serper包装器的引用。


设置
- 前往serper.dev](https://serper.dev)注册一个免费帐户
- 获取API密钥并将其设置为环境变量（`SERPER_API_KEY`）


包装器


实用工具


存在一个名为GoogleSerperAPIWrapper的实用工具，用于包装此API。要导入此实用工具：


```python

from langchain.utilities import GoogleSerperAPIWrapper

```



您可以将其用作Self Ask链的一部分：


```python

from langchain.utilities import GoogleSerperAPIWrapper

from langchain.llms.openai import OpenAI

from langchain.agents import initialize_agent, Tool

from langchain.agents import AgentType



import os



os.environ["SERPER_API_KEY"] = ""

os.environ['OPENAI_API_KEY'] = ""



llm = OpenAI(temperature=0)

search = GoogleSerperAPIWrapper()

tools = [

    Tool(

        name="Intermediate Answer",

        func=search.run,

        description="useful for when you need to ask with search"

    )

]



self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)

self_ask_with_search.run("What is the hometown of the reigning men's U.S. Open champion?")

```



输出
```

输入新的AgentExecutor链...
是的。
后续问题：谁是男子美国公开赛的现任冠军？
中间答案：当前冠军是卡洛斯·阿尔卡拉斯，2022年男子单打冠军。
后续问题：卡洛斯·阿尔卡拉斯来自哪里？
中间答案：西班牙埃尔帕尔马尔。
所以最终答案是：西班牙埃尔帕尔马尔。


> 链结束。


'西班牙埃尔帕尔马尔'
```



有关此包装器的更详细演练，请参见此笔记本](../modules/agents/tools/examples/google_serper.ipynb)。


工具


您还可以将此包装器轻松加载为工具（供代理使用）。
您可以通过以下方式实现：
```python

from langchain.agents import load_tools

tools = load_tools(["google-serper"])

```



有关更多信息，请参见此页面](../modules/agents/tools/getting_started.md)
