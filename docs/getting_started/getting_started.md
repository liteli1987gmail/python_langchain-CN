# 快速入门指南




本教程为您提供了一个快速的指南，介绍如何使用LangChain构建端到端的语言模型应用程序。


## 安装


要开始安装LangChain，请使用以下命令：


```bash
pip install langchain

# or

conda install langchain -c conda-forge

```





## 环境设置


使用LangChain通常需要与一个或多个模型提供程序，数据存储，API等进行集成。


对于这个例子，我们将使用OpenAI的APIs，因此我们需要先安装他们的SDK：


```bash
pip install openai

```



然后我们需要在终端中设置环境变量。


```bash
export OPENAI_API_KEY="..."

```



或者您可以在Jupyter笔记本（或Python脚本）中执行此操作：


```python
import os

os.environ["OPENAI_API_KEY"] = "..."

```



如果您想动态设置API密钥，您可以在初始化OpenAI类时使用openai_api_key参数，例如每个用户的API密钥。


```python
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="OPENAI_API_KEY")

```



## 构建语言模型应用程序:LLMs


现在我们已经安装了LangChain并设置了环境，我们可以开始构建我们的语言模型应用程序。


LangChain提供了许多可以用于构建语言模型应用程序的模块。模块可以组合以创建更复杂的应用程序，也可以单独用于简单的应用程序。






## LLMs:从语言模型获取预测


LangChain最基本的构建块是在一些输入上调用LLM。
Let's walk through a simple example of how to do this. 

为此，让我们假装我们正在构建一个根据公司所生产的产品生成公司名称的服务。


为了做到这一点，我们首先需要导入LLM包装器。


```python

from langchain.llms import OpenAI

```



然后我们可以使用任何参数来初始化该包装器。
在这个例子中，我们可能想要输出更随机的结果，因此我们将使用高温度来初始化它。


```python

llm = OpenAI(temperature=0.9)

```



现在我们可以对一些输入进行调用了！


```python

text = "What would be a good company name for a company that makes colorful socks?"

print(llm(text))

```



```pycon

Feetful of Fun

```



有关如何在LangChain中使用LLMs的更多详细信息，请参见LLM入门指南。




##提示模板:管理LLM的提示


调用LLM是一个很好的第一步，但这只是个开始。
通常当您在应用程序中使用LLM时，您不会直接将用户输入发送到LLM。
相反，您可能会将用户输入进行构造提示，然后再发送到LLM。


例如，在上一个例子中，我们传递的文本是硬编码为询问生产彩色袜子的公司的名称。
在这个想象中的服务中，我们只想获取描述公司所做的事情的用户输入，然后将该信息格式化为提示。


这很容易通过LangChain来实现！


首先让我们定义提示模板:


```python

from langchain.prompts import PromptTemplate



prompt = PromptTemplate(

    input_variables=["product"],

    template="What is a good name for a company that makes {product}?",

)

```



Let's now see how this works! We can call the `.format` method to format it.



```python

print(prompt.format(product="colorful socks"))

```



```pycon

What is a good name for a company that makes colorful socks?

```





更多详情请查看入门指南中的提示模板。








链式——将LLMs和提示结合在多步骤工作流中


到目前为止，我们仅仅使用了PromptTemplate和LLM原始数据。但是，一个真正的应用不仅仅是一个原始数据，而是它们的组合。


在LangChain中，链由链接组成，可以是LLMs或其他链。


最核心的链类型是LLMChain，它由PromptTemplate和LLM组成。


扩展之前的示例，我们可以构建一个LLMChain，它接收用户输入，使用PromptTemplate进行格式化，然后将格式化的响应传递给LLM。


```python

from langchain.prompts import PromptTemplate

from langchain.llms import OpenAI



llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(

    input_variables=["product"],

    template="What is a good name for a company that makes {product}?",

)

```



现在我们可以创建一个非常简单的链，它将接收用户输入，将提示进行格式化，然后将其发送到LLM。


```python

from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)

```



现在我们可以仅指定产品运行该链！


```python

chain.run("colorful socks")

# -> 'Socktastic!'

```



这就是第一个链——一个LLM链。这是较简单的链类型之一，但是了解它的工作原理将为您使用更复杂的链打好基础。
This is one of the simpler types of chains, but understanding how it works will set you up well for working with more complex chains.



更多详情请查阅链式入门指南。


代理——根据用户输入动态调用链


So far the chains we've looked at run in a predetermined order.



代理商不再使用LLM确定要采取哪些行动以及采取何种顺序。一个动作可以是使用工具并观察其输出，或将其返回给用户。

当代理正确使用时，它们可以非常强大。在本教程中，我们向您展示如何通过最简单，最高级别的API轻松使用代理。


为了加载代理，您应该了解以下概念：

- 工具:执行特定职责的功能。这可以是类似于: Google搜索，数据库查找，Python REPL或其他链的内容。工具的界面目前是一个函数，预期其输入为字符串，并输出一个字符串。
- LLM:驱动代理的语言模型。
- 代理:要使用的代理。这应该是引用支持代理类的字符串。因为这个笔记本重点介绍最简单，最高级别的API，所以仅涵盖使用标准支持的代理。如果您想实现自定义代理，请参阅自定义代理的文档（即将推出）。

**代理**:有关受支持的代理及其规格的列表，请参见[此处](../modules/agents/getting_started.ipynb)。

**工具**:有关预定义工具及其规格的列表，请参见[此处](../modules/agents/tools/getting_started.md)。

对于这个例子，您还需要安装SerpAPI Python包。

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
> Entering new AgentExecutor chain...

 I need to find the temperature first, then use the calculator to raise it to the .023 power.

Action: Search

Action Input: "High temperature in SF yesterday"

Observation: San Francisco Temperature Yesterday. Maximum temperature yesterday: 57 °F (at 1:56 pm) Minimum temperature yesterday: 49 °F (at 1:56 am) Average temperature ...

Thought: I now have the temperature, so I can use the calculator to raise it to the .023 power.

Action: Calculator

Action Input: 57^.023

Observation: Answer: 1.0974509573251117



Thought: I now know the final answer

Final Answer: The high temperature in SF yesterday in Fahrenheit raised to the .023 power is 1.0974509573251117.



> Finished chain.

```




## 内存:向链和代理添加状态


到目前为止，我们经过的所有链和代理都是无状态的。但是在很多情况下，您可能希望链或代理具有某种\"内存\"的概念，以便它可以记住有关其以前交互的信息。这种设计聊天机器人时最清晰和简单的示例是：您希望它记住以前的消息，以便它可以利用那些上下文开展更好的对话。这将是一种\"短期记忆\"。在更复杂的一面，您可以想象一条/代理随时间记住重要的信息-这将是一种\"长期记忆\"。有关后者的更具体的想法，请参见[这篇令人敬畏的论文](https://memprompt.com/)。


LangChain为此提供了几个专门创建的链。本笔记本将介绍如何使用其中一个链（\"ConversationChain\"），并使用两种不同类型的内存。


默认情况下，\"ConversationChain\"具有一种简单的记忆方式，可以记住所有之前的输入/输出，并将它们添加到传递的上下文中。让我们看看如何使用此链（设置`verbose=True`，以便我们可以看到提示）。


```python
from langchain import OpenAI, ConversationChain



llm = OpenAI(temperature=0)

conversation = ConversationChain(llm=llm, verbose=True)



output = conversation.predict(input="Hi there!")

print(output)

```

```pycon
```pycon

> Entering new chain...

Prompt after formatting:

The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.



Current conversation:



Human: Hi there!

AI:



> Finished chain.

' Hello! How are you today?'

```

```python
```python

output = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")

print(output)

```

```pycon
```pycon

> Entering new chain...

Prompt after formatting:

The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.



Current conversation:



Human: Hi there!

AI:  Hello! How are you today?

Human: I'm doing well! Just having a conversation with an AI.

AI:



> Finished chain.

" That's great! What would you like to talk about?"

```



## 构建语言模型应用-聊天模型


同样，您可以使用聊天模型而不是LLMs。聊天模型是语言模型的一种变体。虽然聊天模型在幕后使用语言模型，但它们公开的接口有些不同，而不是公开一个\"text in, text out\" API，它们公开的接口让\"聊天信息\"成为输入和输出。


聊天模型API还相对较新，因此我们仍在找到正确的抽象。


## 从聊天模型获取消息完成


通过向聊天模型传递一个或多个消息，您可以获得聊天完成。响应将是一条消息。目前在LangChain中支持的消息类型有`AIMessage`, `HumanMessage`, `SystemMessage`,和`ChatMessage` -- `ChatMessage`采用一个任意的角色参数。大多数情况下，您将只处理`HumanMessage`，,`AIMessage`,和`SystemMessage`。

```python
from langchain.chat_models import ChatOpenAI

from langchain.schema import (

    AIMessage,

    HumanMessage,

    SystemMessage

)



chat = ChatOpenAI(temperature=0)

```


通过传递单个消息，您可以获得完成。

```python
chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")])

# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

```


您还可以为OpenAI的gpt-3.5-turbo和gpt-4模型传递多个消息。

```python
messages = [

    SystemMessage(content="You are a helpful assistant that translates English to French."),

    HumanMessage(content="I love programming.")

]

chat(messages)

# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

```


您可以进一步生成多组消息的完成，使用`generate`。这将返回一个带有额外`message`参数的`LLMResult`。
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


您可以从这个LLMResult中恢复诸如令牌使用情况之类的内容。
```
result.llm_output['token_usage']

# -> {'prompt_tokens': 57, 'completion_tokens': 20, 'total_tokens': 77}

```



##聊天提示模板
类似于LLMs，,您可以通过使用`MessagePromptTemplate`来使用模板。您可以从一个或多个`MessagePromptTemplate`构建一个`ChatPromptTemplate`。您可以使用`ChatPromptTemplate`的`format_prompt`--这将返回一个`PromptValue`，您可以根据您是想将格式化的值作为输入用于LLM还是聊天模型而将其转换为字符串或`Message`对象。

为方便起见，该模板上暴露了一个`from_template`方法。如果您要使用此模板，它将如下所示。

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


##具有聊天模型的链
上面部分讨论的`LLMChain`也可以与聊天模型一起使用。

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


## Agents with Chat Models

代理人也可以与聊天模型一起使用，您可以使用“AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION”作为代理人类型进行初始化。


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



> Entering new AgentExecutor chain...

Thought: I need to use a search engine to find Olivia Wilde's boyfriend and a calculator to raise his age to the 0.23 power.

Action:

{

  "action": "Search",

  "action_input": "Olivia Wilde boyfriend"

}



Observation: Sudeikis and Wilde's relationship ended in November 2020. Wilde was publicly served with court documents regarding child custody while she was presenting Don't Worry Darling at CinemaCon 2022. In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling.

Thought:I need to use a search engine to find Harry Styles' current age.

Action:

{

  "action": "Search",

  "action_input": "Harry Styles age"

}



Observation: 29 years

Thought:Now I need to calculate 29 raised to the 0.23 power.

Action:

{

  "action": "Calculator",

  "action_input": "29^0.23"

}



Observation: Answer: 2.169459462491557



Thought:I now know the final answer.

Final Answer: 2.169459462491557



> Finished chain.

'2.169459462491557'

```

## Memory: Add State to Chains and Agents

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



