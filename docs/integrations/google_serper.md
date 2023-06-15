# Google Serper谷歌搜索引擎


本页面介绍如何在LangChain中使用[Serper](https://serper.dev)谷歌搜索API。Serper是一个低成本的谷歌搜索API，可用于添加谷歌搜索的答案框、知识图谱和有机结果数据。

它分为两部分：设置和特定谷歌Serper包装器的引用。



## 设置

- 前往[serper.dev](https://serper.dev)注册一个免费账户

- 获取API密钥并将其设置为环境变量（`SERPER_API_KEY`）



## 包装器



### 实用工具



存在一个名为GoogleSerperAPIWrapper的实用工具，用于包装该API。导入该工具的方法如下：



```python

from langchain.utilities import GoogleSerperAPIWrapper

```



您可以将其作为Self Ask链的一部分使用：



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

        description="在需要进行搜索时非常有用"

    )

]



self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)

self_ask_with_search.run("请问最新一届美国网球公开赛男子单打冠军的家乡是哪里？")

```



#### 输出结果

```

进入新的AgentExecutor链...

 是的。

后续问题：谁是最新一届美国网球公开赛男子单打冠军？

中间答案：目前的冠军是2022年男子单打冠军Carlos Alcaraz。

后续问题：Carlos Alcaraz来自哪里？

中间答案：西班牙的El Palmar

因此最终答案是：El Palmar, Spain



> 链条执行结束。



'El Palmar, Spain'

```



有关此包装器的详细介绍，请参阅[此笔记本](../modules/agents/tools/examples/google_serper.ipynb)。



### 工具



您还可以将此包装器轻松加载为工具（用于与Agent配合使用）。

您可以使用以下方法实现：

```python

from langchain.agents import load_tools

tools = load_tools(["google-serper"])

```



有关更多信息，请参阅[此页面](../modules/agents/tools/getting_started.md)

