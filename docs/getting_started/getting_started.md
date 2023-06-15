# 快速入门指南





这个教程将带您快速了解如何使用LangChain构建端到端语言模型应用程序。



## 安装



要开始使用LangChain，请使用以下命令安装LangChain：



```bash

pip install langchain

# 或

conda install langchain -c conda-forge

```





## 环境设置



通常，使用LangChain会需要与一个或多个模型提供者、数据存储和API等进行集成。



对于这个示例，我们将使用OpenAI的API，所以我们首先需要安装他们的SDK：



```bash

pip install openai

```



然后我们需要在终端中设置环境变量。



```bash

export OPENAI_API_KEY="..."

```



或者，您可以在Jupyter笔记本（或Python脚本）中执行以下操作：



```python

import os

os.environ["OPENAI_API_KEY"] = "..."

```



如果您想动态设置API密钥，可以在初始化OpenAI类时使用openai_api_key参数，比如每个用户的API密钥。



```python

from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="OPENAI_API_KEY")

```



## 构建语言模型应用程序：LLMs



现在我们已经安装了LangChain并设置了环境，我们可以开始构建我们的语言模型应用程序。



LangChain提供了许多模块，可用于构建语言模型应用程序。模块可以组合在一起以创建更复杂的应用程序，也可以单独用于简单的应用程序。







## LLMs：从语言模型获取预测结果



LangChain的最基本的构建块是对某个输入调用LLM。

让我们通过一个简单的例子来了解如何做到这一点。

为此，假设我们正在构建一个基于公司所制造产品的公司名称生成服务。



为了做到这一点，我们首先需要导入LLM包装器。



```python

from langchain.llms import OpenAI

```



然后我们可以使用任何参数来初始化包装器。

在这个例子中，我们可能希望输出的结果更随机些，所以我们将使用较高的temperature值进行初始化。



```python

llm = OpenAI(temperature=0.9)

```



现在我们可以对某个输入进行调用！



```python

text = "关于一家生产多彩袜子的公司，有什么好的公司名称可以给推荐一下？"

print(llm(text))

```



```pycon

充满趣味的脚

```



有关在LangChain中使用LLMs的更多细节，请参阅[LLM入门指南](../modules/models/llms/getting_started.ipynb)。





## 提示模板：管理LLMs的提示



调用LLM只是一个很好的第一步，但这只是一个开始。

通常情况下，当您在应用程序中使用LLM时，您不会直接将用户输入发送到LLM。

相反，您可能希望选择性地接收用户输入并构建提示，然后将提示发送到LLM。



例如，在前面的示例中，我们传递的文本是硬编码的，要求为一家制造彩色袜子的公司提供名称。

在这个想象中的服务中，我们只希望获取描述公司所做工作的用户输入，并使用这些信息格式化提示。



使用LangChain很容易实现这个功能！



首先让我们定义提示模板：



```python

from langchain.prompts import PromptTemplate



prompt = PromptTemplate(

    input_variables=["product"],

    template="一家制造{product}的公司需要一个好的名字，您有什么推荐吗？",

)

```



让我们看看它是如何工作的！我们可以调用`.format`方法进行格式化。



```python

print(prompt.format(product="彩色袜子"))

```



```pycon

一家制造彩色袜子的公司需要一个好的名字，您有什么推荐吗？

```





有关更多详细信息，请查看[提示入门指南](../modules/prompts/chat_prompt_template.ipynb)。









## 链式操作：将LLMs和提示组合成多步工作流



到目前为止，我们已经单独讨论了PromptTemplate和LLM原语。但是实际上，一个真实的应用程序不仅仅是一个原语，而是其中的组合。



在LangChain中，链由链接组成，链接可以是LLM或其他链等原语。



链式操作的主要类型是LLMChain，它由PromptTemplate和LLM组成。



在上面的例子的基础上，我们可以构建一个LLMChain，该链接收用户输入并使用PromptTemplate对其进行格式化，然后将格式化的响应传递给LLM。



```python

from langchain.prompts import PromptTemplate

from langchain.llms import OpenAI



llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(

    input_variables=["product"],

    template="一家制造{product}的公司需要一个好的名字，您有什么推荐吗？",

)

```



现在，我们可以创建一个非常简单的链，该链将接收用户输入，使用它来格式化提示，然后将其发送给LLM：



```python

from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)

```



现在，我们可以只指定产品来运行该链！



```python

chain.run("彩色袜子")

# -> '\n\n充满趣味的脚'

```



完成了！这就是第一个链 - 一个LLM Chain。

这是较简单类型的链之一，但是理解它的工作原理将为您处理更复杂的链提供基础。



有关更多详细信息，请查看[链式操作入门指南](../modules/chains/getting_started.ipynb)。



## Agents：根据用户输入动态调用链



到目前为止，我们看到的链是按照预定义的顺序运行的。



但是Agents不再这样做：它们使用LLM来确定要采取的行动及其顺序。行动可以是使用工具并观察其输出，或返回给用户。



正确使用Agents可以非常强大。在本教程中，我们将向您展示如何通过最简单、最高级别的API轻松使用Agents。





为了加载Agents，您应该了解以下概念：



- 工具（Tool）：执行特定任务的函数。这可以是Google搜索、数据库查询、Python REPL或其他链。工具的接口当前期望函数的输入为字符串，输出为字符串。

- LLM：驱动Agent的语言模型。

- Agent：要使用的Agent。这应该是一个字符串，该字符串引用了支持的Agent类。因为本笔记本重点介绍了最简单、最高级别的API的使用，所以只介绍了使用标准支持的Agent。如果您想实现自定义的Agent，请参阅自定义Agent的文档（即将推出）。



**Agents**：支持的Agent及其规格的列表，请参见[此处](../modules/agents/getting_started.ipynb)。



**工具**：预定义工具及其规格的列表，请参见[此处](../modules/agents/tools/getting_started.md)。



对于此示例，您还需要安装SerpAPI Python包。



```bash

pip install google-search-results

```



并设置适当的环境变量。



```python

import os

os.environ["SERPAPI_API_KEY"] = "..."

```



现在我们可以开始！



```python

from langchain.agents import load_tools

from langchain.agents import initialize_agent

from langchain.agents import AgentType

from langchain.llms import OpenAI



# 首先，让我们加载要用于控制Agent的语言模型。

llm = OpenAI(temperature=0)



# 接下来，让我们加载一些要使用的工具。请注意，“llm-math”工具使用LLM，因此我们需要传入它。

tools = load_tools(["serpapi", "llm-math"], llm=llm)





# 最后，让我们使用工具、语言模型和要使用的Agent类型初始化一个Agent。

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)



# 现在让我们来测试一下！

agent.run("昨天旧金山的最高温度是多少摄氏度？将该数字提高到0.23次方是多少？")

```



```pycon

> 进入新的AgentExecutor链...

我需要首先找到温度，然后使用计算器将其提升到0.23次方。

行动：搜索

行动输入：“昨天旧金山的最高温度”

观察：旧金山昨天的温度。昨天的最高温度为57°F（下午1:56）昨天的最低温度为49°F（上午1:56）昨天的平均温度...

思考：现在我有了温度，所以可以使用计算器将其提升到0.23次方。

行动：计算器

行动输入：“57^0.23”

观察：答案：1.0974509573251117



思考：我现在知道了最终的答案

最终答案：昨天旧金山的最高温度提升到0.23次方为1.0974509573251117。



> 完成链。

```







## 存储：为链和Agents添加状态



到目前为止，我们涉及的所有链和Agents都是无状态的。但是通常，您可能希望链或Agents具有某种"记忆"概念，以便它可以记住有关以前交互的信息。这个例子中最清晰、简单的例子是在设计聊天机器人时，您希望它记住先前的消息，以便能够利用上下文进行更好的对话。这将是一种"短期记忆"的形式。在更复杂的情况下，您可以想象一个链/Agents随时间记住关键信息的情况，这将是一种"长期记忆"的形式。有关后一种情况的更具体的想法，请参见此[出色的论文](https://memprompt.com/)。



LangChain提供了几种专门为此目的而创建的链。本笔记本介绍了如何使用其中一种链（`ConversationChain`）与两种不同类型的记忆。



默认情况下，`ConversationChain`具有一种简单的记忆类型，它记住所有先前的输入/输出并将它们添加到传递的上下文中。让我们看看如何使用这个链（设置`verbose=True`以便我们可以看到提示）。



```python

from langchain import OpenAI, ConversationChain



llm = OpenAI(temperature=0)

conversation = ConversationChain(llm=llm, verbose=True)



output = conversation.predict(input="你好！")

print(output)

```



```pycon

> 进入新的链...

格式化后的提示：

以下是人机友好的对话。AI非常健谈，并从其上下文中提供大量具体细节。如果AI不知道问题的答案，它会真实地说出来。



当前对话：



人类：你好！

AI：



> 完成链。

' 你好！你好吗？'

```



```python

output = conversation.predict(input="我很好！只是和一个AI进行对话。")

print(output)

```



```pycon

> 进入新的链...

格式化后的提示：

以下是人机友好的对话。AI非常健谈，并从其上下文中提供大量具体细节。如果AI不知道问题的答案，它会真实地说出来。



当前对话：



人类：你好！

AI： 你好！你好吗？

人类：我很好！只是和一个AI进行对话。

AI：



> 完成链。

" 这听起来很有趣！很高兴能和你聊天。你想具体聊些什么呢？"

```



## 构建语言模型应用程序：聊天模型



类似地，您可以使用聊天模型来替代LLMs。聊天模型是对语言模型的一种变体。虽然聊天模型在内部使用语言模型，但它们公开的接口略有不同：它们不是“输入文本，输出文本”的API，而是以“聊天消息”作为输入和输出的接口。



聊天模型的API还比较新，因此我们还在探索正确的抽象方式。



## 从聊天模型获取消息补全



通过向聊天模型传递一个或多个消息，您可以获取聊天补全。响应将是一条消息。在LangChain中支持的消息类型是`AIMessage`、`HumanMessage`、`SystemMessage`和`ChatMessage`——`ChatMessage`接受一个任意的角色参数。大多数时候，您只需要处理`HumanMessage`、`AIMessage`和`SystemMessage`。



```python

from langchain.chat_models import ChatOpenAI

from langchain.schema import (

    AIMessage,

    HumanMessage,

    SystemMessage

)



chat = ChatOpenAI(temperature=0)

```



您可以通过传递单个消息来获取完成。



```python

chat([HumanMessage(content="将这句英文句子翻译成法语。我喜欢编程。")])

# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

```



您还可以传递多个消息给OpenAI的gpt-3.5-turbo和gpt-4模型。



```python

messages = [

    SystemMessage(content="您是一个可帮助翻译英语到法语的助手。")，

    HumanMessage(content="我喜欢编程。")

]

chat(messages)

# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

```



可以进一步生成多个消息集的补全，使用`generate`方法。这将返回一个带有附加的`message`参数的`LLMResult`：

```python

batch_messages = [

    [

        SystemMessage(content="您是一个可帮助翻译英语到法语的助手。")，

        HumanMessage(content="我喜欢编程。")

    ],

    [

        SystemMessage(content="您是一个可帮助翻译英语到法语的助手。")，

        HumanMessage(content="我喜欢人工智能。")

    ],

]

result = chat.generate(batch_messages)

result

# -> LLMResult(generations=[[ChatGeneration(text="J'aime programmer.", generation_info=None, message=AIMessage(content="J'aime programmer.", additional_kwargs={}))], [ChatGeneration(text="J'aime l'intelligence artificielle.", generation_info=None, message=AIMessage(content="J'aime l'intelligence artificielle.", additional_kwargs={}))]], llm_output={'token_usage': {'prompt_tokens': 57, 'completion_tokens': 20, 'total_tokens': 77}})

```



您可以从此LLMResult中获取诸如token使用情况等信息：

```

result.llm_output['token_usage']

# -> {'prompt_tokens': 57, 'completion_tokens': 20, 'total_tokens': 77}

```





## 聊天提示模板

类似于LLMs，您可以使用模板来进行提示，通过使用`MessagePromptTemplate`来使用`ChatPromptTemplate` 。您可以根据一个或多个`MessagePromptTemplate`构建一个`ChatPromptTemplate`。您可以使用`ChatPromptTemplate`的`format_prompt`方法，可以将其转换为字符串或`Message`对象，具体取决于您是想将格式化值作为输入传递给llm还是chat model。



为了方便起见，模板上公开了`from_template`方法。如果您要使用此模板，它将如下所示：



```python

from langchain.chat_models import ChatOpenAI

from langchain.prompts.chat import (

    ChatPromptTemplate,

    SystemMessagePromptTemplate,

    HumanMessagePromptTemplate,

)



chat = ChatOpenAI(temperature=0)



template = "您是一个可帮助将{input_language}翻译为{output_language}的助手。"

system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template = "{text}"

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)



chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])



# 从格式化的消息中获取一个chat completion

chat(chat_prompt.format_prompt(input_language="英语", output_language="法语", text="我喜欢编程。").to_messages())

# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

```



## 带有聊天模型的链式操作

上述部分讨论的`LLMChain`也可以与聊天模型一起使用:



```python

from langchain.chat_models import ChatOpenAI

from langchain import LLMChain

from langchain.prompts.chat import (

    ChatPromptTemplate,

    SystemMessagePromptTemplate,

    HumanMessagePromptTemplate,

)



chat = ChatOpenAI(temperature=0)



template = "您是一个可帮助将{input_language}翻译为{output_language}的助手。"

system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template = "{text}"

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])



chain = LLMChain(llm=chat, prompt=chat_prompt)

chain.run(input_language="英语", output_language="法语", text="我喜欢编程。")

# -> "J'aime programmer."

```



## Agents与聊天模型

Agents还可以与聊天模型一起使用，您可以使用`AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION`作为Agent类型进行初始化。



```python

from langchain.agents import load_tools

from langchain.agents import initialize_agent

from langchain.agents import AgentType

from langchain.chat_models import ChatOpenAI

from langchain.llms import OpenAI



# 首先，让我们加载要用于控制Agent的语言模型。

chat = ChatOpenAI(temperature=0)



# 接下来，让我们加载一些要使用的工具。请注意，“llm-math”工具使用LLM，因此我们需要传入它。

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=llm)





# 最后，让我们使用工具、语言模型和要使用的Agent类型初始化一个Agent。

agent = initialize_agent(tools, chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)



# 现在让我们来测试一下！

agent.run("奥利维亚·王尔德的男朋友是谁？他的年龄提高到0.23次方是多少？")

```



```pycon



> 进入新的AgentExecutor链...

Thought: 首先我需要找到温度，然后使用计算器将其提升到0.23次方。

Action: Search

Action Input: "奥利维亚·王尔德男朋友"

Observation: 苏德基斯和王尔德的关系于2020年11月结束。王尔德在2022年CinemaCon展示《别担心，亲爱》期间公开收到儿童监护方面的法庭文件。2021年1月，王尔德和歌手哈里·斯泰尔斯开始约会，两人在拍摄《别担心，亲爱》期间相识。

Thought: 我现在需要使用搜索引擎找到哈里·斯泰尔斯的年龄。

Action: Search

Action Input: "哈里·斯泰尔斯年龄"

Observation: 29岁

Thought: 现在我需要计算29的0.23次方。

Action: Calculator

Action Input: "29^0.23"

Observation: Answer: 2.169459462491557



Thought: 现在我知道了最终答案

Final Answer: 奥利维亚·王尔德的男友年龄提高到0.23次方约为2.169459462491557。



> 完成链。

'2.169459462491557'

{



















> 完成链。

'2.169459462491557'

```



## 存储：为链和Agents添加状态

您可以在使用聊天模型初始化的链和Agents中使用存储。这与LLMs的存储的主要区别在于，我们不再尝试将所有先前的消息压缩为一个字符串，而是可以将它们作为自己的唯一的内存对象保留。

```python



from langchain.prompts import (

    ChatPromptTemplate, 

    MessagesPlaceholder, 

    SystemMessagePromptTemplate, 

    HumanMessagePromptTemplate

)

from langchain.chains import ConversationChain

from langchain.chat_models import ChatOpenAI

from langchain.memory import ConversationBufferMemory



prompt = ChatPromptTemplate.from_messages([

    SystemMessagePromptTemplate.from_template("以下是人机友好的对话。AI非常健谈，并提供了许多来自其上下文的具体细节。如果AI不知道问题的答案，它会诚实地说出来。"),

    MessagesPlaceholder(variable_name="history"),

    HumanMessagePromptTemplate.from_template("{input}")

])



llm = ChatOpenAI(temperature=0)

memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)



conversation.predict(input="你好！")

# -> '你好！我如何帮助您？'





conversation.predict(input="我很好！只是和一个AI进行对话。")

# -> "听起来很有趣！很高兴和您聊天。有什么特别的事情想要聊的吗？"



conversation.predict(input="向我介绍一下自己。")

# -> "当然！我是由OpenAI创建的AI语言模型。我使用互联网上的大量文本进行训练，这使我能够理解和生成人类语言。我可以回答问题、提供信息，甚至进行像这样的对话。还有什么关于我的事情您想知道的吗？"



