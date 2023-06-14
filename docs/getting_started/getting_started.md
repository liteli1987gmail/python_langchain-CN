# 快速入门指南




本教程为您介绍如何使用LangChain构建端到端的语言模型应用程序。


## 安装


要开始使用LangChain，请使用以下命令安装LangChain：


```bash

pip install langchain
# or
conda install langchain -c conda-forge
```





## 环境设置


使用LangChain通常需要与一个或多个模型提供者、数据存储、API等进行集成。


在本示例中，我们将使用OpenAI的API，因此我们首先需要安装他们的SDK：


```bash

pip install openai
```



然后，我们需要在终端中设置环境变量。


```bash

export OPENAI_API_KEY="..."
```



或者，您可以在Jupyter笔记本（或Python脚本）中执行此操作：


```python

import os

os.environ["OPENAI_API_KEY"] = "..."

```



如果您想要动态设置API密钥，可以在初始化OpenAI类时使用openai_api_key参数，例如，每个用户的API密钥。


```python

from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="OPENAI_API_KEY")

```



## 构建语言模型应用程序：LLMs


既然我们已经安装了LangChain并设置了环境，我们可以开始构建语言模型应用程序了。


LangChain提供了许多模块，可用于构建语言模型应用程序。可以组合这些模块以创建更复杂的应用程序，或者单独用于简单的应用程序。






## LLMs：从语言模型获取预测


LangChain的最基本构建块是在某个输入上调用LLM。
让我们通过一个简单的例子来演示如何做到这一点。
为此，让我们假设我们正在构建一个根据公司所做的产品生成公司名称的服务。


为了做到这一点，我们首先需要导入LLM封装器。


```python

from langchain.llms import OpenAI

```



然后，我们可以使用任何参数来初始化封装器。
在这个例子中，我们可能希望输出更随机，因此我们将使用高温度进行初始化。


```python

llm = OpenAI(temperature=0.9)

```



现在，我们可以在某个输入上调用它！


```python

text = "What would be a good company name for a company that makes colorful socks?"

print(llm(text))

```



```python

乐趣之足
```



有关如何在LangChain中使用LLMs的更多详细信息，请参阅[LLM入门指南](../modules/models/llms/getting_started.ipynb)。




## 提示模板：管理LLMs的提示


调用LLM是一个很好的第一步，但这只是一个开始。
通常，在应用程序中使用LLM时，您不会直接将用户输入发送到LLM。
相反，您可能会使用用户输入构造提示，然后将其发送到LLM。


例如，在之前的例子中，我们传入的文本是固定的，要求为一个制造彩色袜子的公司提供名称。
在这个想象中的服务中，我们希望只采用描述公司所做产品的用户输入，并使用该信息格式化提示。


使用LangChain很容易做到这一点！


首先让我们定义提示模板：


```python

from langchain.prompts import PromptTemplate



prompt = PromptTemplate(

    input_variables=["product"],

    template="What is a good name for a company that makes {product}?",

)

```



现在让我们看看它是如何工作的！我们可以调用`format`方法进行格式化。


```python

print(prompt.format(product="colorful socks"))

```



```pycon

一个制造彩色袜子的公司的好名字是什么？
```





有关更多详细信息，请参阅提示入门指南](../modules/prompts/chat_prompt_template.ipynb)。








## 链式流程：将LLMs和提示组合成多步工作流


迄今为止，我们只使用了单个原语（即LLMs和提示模板）。但是，一个真实的应用程序不仅仅是一个原语，而是它们的组合。


在LangChain中，链由链接组成，可以是原语（如LLMs）或其他链。


链的最核心类型是LLMChain，由PromptTemplate和LLM组成。


通过扩展之前的例子，我们可以构建一个LLMChain，它接受用户输入，使用PromptTemplate格式化它，然后将格式化的回复传递给LLM。


```python

from langchain.prompts import PromptTemplate

from langchain.llms import OpenAI



llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(

    input_variables=["product"],

    template="What is a good name for a company that makes {product}?",

)

```



现在我们可以创建一个非常简单的链，它将接受用户输入，使用它来格式化提示，然后将其发送到LLM：


```python

from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)

```



现在我们可以只指定产品来运行该链！


```python

chain.run("colorful socks")

# -> '\n\nSocktastic!'

```



好了！这就是第一个链 - 一个LLM链。
这是一种比较简单的链的类型，但是了解它的工作原理将为您处理更复杂的链奠定基础。


有关更多详细信息，请参阅链入门指南](../modules/chains/getting_started.ipynb)。


##  代理：根据用户输入动态调用链


到目前为止，我们查看的链是按照预定顺序运行的。


代理不再如此：它们使用LLM来确定采取的操作及其顺序。操作可以是使用工具并观察其输出，或将其返回给用户。






为了加载代理，您应该了解以下概念：


- 工具：执行特定任务的功能。这可以包括Google搜索、数据库查找、Python REPL和其他链。工具的接口目前是期望一个字符串作为输入，并输出一个字符串的函数。
- LLM：代理的语言模型。
- 代理：要使用的代理。这应该是一个引用支持的代理类的字符串。因为这个笔记本专注于最简单、最高级别的API，所以只涵盖了使用标准支持的代理。如果要实现自定义代理，请参阅自定义代理的文档（即将推出）。


代理：支持的代理及其规格清单，请参阅[这里](../modules/agents/getting_started.ipynb)。
工具**Tools**：预定义工具及其规格清单，请参阅这里](../modules/agents/tools/getting_started.md)。




对于本示例，您还需要安装SerpAPI Python包。


```bash

pip install google-search-results

```



并设置适当的环境变量。


```python

import os

os.environ["SERPAPI_API_KEY"] = "..."

```



现在我们可以开始了！


```python

from langchain.agents import load_tools

from langchain.agents import initialize_agent

from langchain.agents import AgentType

from langchain.llms import OpenAI



# First, let's load the language model we're going to use to control the agent.

llm = OpenAI(temperature=0)



# Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.

tools = load_tools(["serpapi", "llm-math"], llm=llm)





# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)



# Now let's test it out!

agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")

```



```pycon

> 进入新的AgentExecutor链...
我首先需要找到温度，然后使用计算器将其提高到0.023的幂。
操作：搜索
操作输入："昨天旧金山的高温"
观察结果：旧金山昨天的温度。昨天最高温度为57°F（下午1:56） 昨天最低温度为49°F（上午1:56） 昨天平均温度...
思考：现在我知道了温度，所以我可以使用计算器将其提高到0.023的幂。
操作：计算器
操作输入：57^0.023
观察结果：答案：1.0974509573251117


思考：现在我知道了最终答案
最终答案：昨天旧金山的高温度以华氏度为单位提高到0.023的幂为1.0974509573251117。


> Finished chain.

```







## 内存：将状态添加到链和代理


到目前为止，我们所处理的所有链和代理都是无状态的。但是通常情况下，您可能希望链或代理具有一些"记忆"的概念，以便它们可以记住与其之前的交互有关的信息。这在设计聊天机器人时最为明显和简单 - 您希望它记住以前的消息，以便可以使用上下文进行更好的对话。这是一种"短期记忆"的一种类型。更复杂的情况下，可以想象一条链/代理随着时间记住关键信息 - 这是一种"长期记忆"的形式。有关后一种的更具体的想法，请参阅这篇精彩的论文](https://memprompt.com/)。


LangChain提供了几个专门为此目的创建的链。本笔记本介绍了其中一个链（ConversationChain）的使用方式，并使用了两种不同类型的记忆。


默认情况下，ConversationChain具有简单类型的记忆，它记住所有先前的输入/输出并将它们添加到传递的上下文中。让我们看看如何使用这个链（设置`verbose=True`以便我们可以看到提示）。


```python

from langchain import OpenAI, ConversationChain



llm = OpenAI(temperature=0)

conversation = ConversationChain(llm=llm, verbose=True)



output = conversation.predict(input="Hi there!")

print(output)

```



```python

> 进入新的链...
格式化后的提示：
以下是人类和AI之间的友好对话。AI健谈，提供了许多来自其上下文的具体细节。如果AI无法回答问题，它会诚实地说它不知道。


当前对话：


人类：你好！
AI：


> 完成链。
'你好！你今天好吗？'
```



```python

output = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")

print(output)

```



```pycon

> 进入新的链...
格式化后的提示：
以下是人类和AI之间的友好对话。AI健谈，提供了许多来自其上下文的具体细节。如果AI无法回答问题，它会诚实地说它不知道。


当前对话：


人类：你好！
AI：你好！你今天好吗？
人类：我过得很好！只是和AI聊天。
AI：


> 完成链。
"太好了！你想聊什么？"
```



构建语言模型应用程序：聊天模型


类似地，您可以使用聊天模型而不是LLMs。聊天模型是语言模型的一种变体。虽然聊天模型在内部使用语言模型，但它们公开的接口略有不同：它们不是公开一个"文本输入，文本输出"的API，而是公开了一个"聊天消息"作为输入和输出的接口。


聊天模型API还相对较新，所以我们仍在探索正确的抽象方式。


从聊天模型获取消息补全


您可以通过向聊天模型传递一个或多个消息来获取聊天补全。响应将是一条消息。LangChain当前支持的消息类型有AIMessage、HumanMessage、SystemMessage和ChatMessage - ChatMessage接受一个任意的角色参数。大多数情况下，您只需要处理HumanMessage、AIMessage和SystemMessage。


```python

from langchain.chat_models import ChatOpenAI

from langchain.schema import (

    AIMessage,

    HumanMessage,

    SystemMessage

)



chat = ChatOpenAI(temperature=0)

```



您可以通过传递单个消息来获取补全。


```python

chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")])

# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

```



您也可以传递多个消息给OpenAI的gpt-3.5-turbo和gpt-4模型。


```python

messages = [

    SystemMessage(content="You are a helpful assistant that translates English to French."),

    HumanMessage(content="I love programming.")

]

chat(messages)

# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

```



您还可以使用`generate`为多个消息组生成补全，这将返回一个带有额外的`message`参数的`LLMResult`：
```python

batch_messages = [

    [

        SystemMessage(content="You are a helpful assistant that translates English to French."),

        HumanMessage(content="I love programming.")

    ],

    [

        SystemMessage(content="You are a helpful assistant that translates English to French."),

        HumanMessage(content="I love artificial intelligence.")

    ],

]

result = chat.generate(batch_messages)

result

# -> LLMResult(generations=[[ChatGeneration(text="J'aime programmer.", generation_info=None, message=AIMessage(content="J'aime programmer.", additional_kwargs={}))], [ChatGeneration(text="J'aime l'intelligence artificielle.", generation_info=None, message=AIMessage(content="J'aime l'intelligence artificielle.", additional_kwargs={}))]], llm_output={'token_usage': {'prompt_tokens': 57, 'completion_tokens': 20, 'total_tokens': 77}})

```



您可以从这个LLMResult中恢复诸如令牌使用情况之类的信息：
```

result.llm_output['token_usage']

# -> {'prompt_tokens': 57, 'completion_tokens': 20, 'total_tokens': 77}

```





## 聊天提示模板
类似于LLMs，您可以使用模板来使用`MessagePromptTemplate`。您可以从一个或多个`MessagePromptTemplate`构建`ChatPromptTemplate`。您可以使用`ChatPromptTemplate`的`format_prompt`方法 - 这将返回一个`PromptValue`，您可以将其转换为字符串或`Message`对象，具体取决于您是否希望将格式化的值用作LLM或聊天模型的输入。


为了方便起见，模板上公开了一个`from_template`方法。如果您要使用此模板，将如下所示：


```python

from langchain.chat_models import ChatOpenAI

from langchain.prompts.chat import (

    ChatPromptTemplate,

    SystemMessagePromptTemplate,

    HumanMessagePromptTemplate,

)



chat = ChatOpenAI(temperature=0)



template = "You are a helpful assistant that translates {input_language} to {output_language}."

system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template = "{text}"

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)



chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])



# get a chat completion from the formatted messages

chat(chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages())

# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

```



##  与聊天模型一起使用的链
在上面的部分中讨论的`LLMChain`也可以与聊天模型一起使用：


```python

from langchain.chat_models import ChatOpenAI

from langchain import LLMChain

from langchain.prompts.chat import (

    ChatPromptTemplate,

    SystemMessagePromptTemplate,

    HumanMessagePromptTemplate,

)



chat = ChatOpenAI(temperature=0)



template = "You are a helpful assistant that translates {input_language} to {output_language}."

system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template = "{text}"

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])



chain = LLMChain(llm=chat, prompt=chat_prompt)

chain.run(input_language="English", output_language="French", text="I love programming.")

# -> "J'aime programmer."

```



## 与聊天模型一起使用的代理
代理也可以与聊天模型一起使用，您可以使用`AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION`作为代理类型进行初始化。


```python

from langchain.agents import load_tools

from langchain.agents import initialize_agent

from langchain.agents import AgentType

from langchain.chat_models import ChatOpenAI

from langchain.llms import OpenAI



# First, let's load the language model we're going to use to control the agent.

chat = ChatOpenAI(temperature=0)



# Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=llm)





# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.

agent = initialize_agent(tools, chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)



# Now let's test it out!

agent.run("Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?")

```



```pycon



> 进入新的AgentExecutor链...
思考：我需要使用搜索引擎找到Olivia Wilde的男友，并使用计算器将他的年龄提高到0.23的幂。
操作：
{
    "action": "Search",
    "action_input": "Olivia Wilde boyfriend"
}
  "action": "Search",

  "action_input": "Olivia Wilde boyfriend"

观察结果：Sudeikis和Wilde的关系在2020年11月结束。Wilde在2022年的CinemaCon上演示Don't Worry Darling时公开接到了关于儿童监护的法庭文件。2021年1月，Wilde在拍摄Don't Worry Darling期间与歌手Harry Styles约会。



思考：我需要使用搜索引擎找到Harry Styles的当前年龄。
操作：
{
    "action": "Search",
    "action_input": "Harry Styles age"
}
{

  "action": "Search",

观察结果：29岁
}

思考：现在我需要计算29的0.23次方。
操作：
{
    "action": "Calculator",
    "action_input": "29^0.23"
}
Action:

{

观察结果：答案：2.169459462491557
  "action_input": "29^0.23"

}



Observation: Answer: 2.169459462491557



思考：现在我知道了最终答案。
最终答案：昨天旧金山的高温度以华氏度为单位提高到0.023的幂为2.169459462491557。


> Finished chain.

'2.169459462491557'

```

## 内存：为链和代理添加状态
You can use Memory with chains and agents initialized with chat models. The main difference between this and Memory for LLMs is that rather than trying to condense all previous messages into a string, we can keep them as their own unique memory object.



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

    SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),

    MessagesPlaceholder(variable_name="history"),

    HumanMessagePromptTemplate.from_template("{input}")

])



llm = ChatOpenAI(temperature=0)

memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)



conversation.predict(input="Hi there!")

# -> 'Hello! How can I assist you today?'





conversation.predict(input="I'm doing well! Just having a conversation with an AI.")

# -> "That sounds like fun! I'm happy to chat with you. Is there anything specific you'd like to talk about?"



conversation.predict(input="Tell me about yourself.")

# -> "Sure! I am an AI language model created by OpenAI. I was trained on a large dataset of text from the internet, which allows me to understand and generate human-like language. I can answer questions, provide information, and even have conversations like this one. Is there anything else you'd like to know about me?"

```


