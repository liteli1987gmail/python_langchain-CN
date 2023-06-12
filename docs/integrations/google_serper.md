Google Serper（谷歌搜索API）

本页介绍如何在LangChain中使用[Serper]（https : //serper.dev）Google Search API。 Serper是一种低成本的Google搜索API，可用于添加来自Google搜索的答案框、知识图和有机结果数据。
它分为两个部分：设置和特定的Google Serper包装器的引用。

## 设置
- 转到[serper.dev]（https : //serper.dev）注册免费帐户
- 获取API密钥并将其设置为环境变量（` SERPER_API_KEY`）

## 包装器

### 实用程序

存在一个GoogleSerperAPIWrapper实用程序，将此API包装起来。 要导入此实用程序: 

```python
from langchain.utilities import GoogleSerperAPIWrapper

```


您可以将其用作Self Ask链的一部分: 

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


#### 输出
```
Entering new AgentExecutor chain...

 Yes.

Follow up: Who is the reigning men's U.S. Open champion?

Intermediate answer: Current champions Carlos Alcaraz, 2022 men's singles champion.

Follow up: Where is Carlos Alcaraz from?

Intermediate answer: El Palmar, Spain

So the final answer is: El Palmar, Spain



> Finished chain.



'El Palmar, Spain'

```


有关此包装器的更详细演练，请参见[此笔记本电脑]（../modules/agents/tools/examples/google_serper.ipynb）。

### 工具

您还可以轻松加载此包装器作为工具（与代理一起使用）。 
您可以使用的方法是: 
```python
from langchain.agents import load_tools

tools = load_tools(["google-serper"])

```


For more information on this, see [this page](../modules/agents/tools/getting_started.md)

