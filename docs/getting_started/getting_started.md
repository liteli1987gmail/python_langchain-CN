# 入门指南

本教程让您快速了解如何使用 LangChain 构建端到端语言模型应用程序。

## 安装

首先，使用以下命令安装 LangChain：

```bash
pip install langchain
# or
conda install langchain -c conda-forge
```

## 设置环境变量

使用 LangChain 通常需要与一个或多个模型提供者、数据存储、api 等集成。

对于这个例子，我们将使用 OpenAI 的 API，所以我们首先需要安装他们的 SDK：

```bash
pip install openai
```

然后我们需要在终端中设置环境变量。

```bash
export OPENAI_API_KEY="..."
```

或者，你也可以从 Jupyter notebook（或 Python 脚本）中执行此操作：

```python
import os
os.environ["OPENAI_API_KEY"] = "..."
```

## 用 LLMs 构建一个语言型应用

之前已经安装了 LangChain 并设置了环境变量，我们可以开始构建我们的语言模型应用了。

LangChain 提供了很多可以用来构建语言模型应用的 modules。这些 modules 可以组合起来创建复杂应用，或者单独创建一个简单应用。

## LLMs: 从语言模型中获取预测

LangChain 最小化应用是在用户输入后直接调用 LLM。咱们通过一个例子来看看怎么创建。

假设我们正在构建一项服务，该服务会根据公司的产品生成公司名称。

为此，我们首先需要导入 LLMs 的封装(wrapper)。

```python
from langchain.llms import OpenAI
```

然后使用参数来初始化 wrapper。
这个例子中，我们希望输出的结果偏随机一些，在初始化的时候就可以把 temperature 设置的高一些。

```python
llm = OpenAI(temperature=0.9)
```

接下来我们带着一个问题调用一下！

```python
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))
```

```pycon
Feetful of Fun
```

有关如何在 LangChain 中使用 LLMs 的更多详细信息，可以查看 [LLMs 入门指南](../modules/models/llms/getting_started.ipynb).

## 提示词模板: 管理 LLM 提示词

调用 LLMs 完成了很好的一步，但也只是个开始。

通常，在应用程序中使用 LLM 时，不会把用户输入的内容直接发送到 LLM。
而是应该通过用户输入构建一个提示词，然后再发给 LLM。

例如，在前面的例子中，我们传递的 text 是硬编码的，要求提供一家生产彩色袜子的公司的名称。

在这个假想的服务中，我们想做的是只接受描述公司所做事情的用户输入，然后把这些信息格式化成提示词。

这个用 LangChain 做起来非常简单。

首先，我们先定义一个提示词模板：

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
```

现在我们看看怎么用起来！我们可以调用 `.format` 方法对其进行格式化。

```python
print(prompt.format(product="colorful socks"))
```

```pycon
What is a good name for a company that makes colorful socks?
```

想看更多细节，可以查看 [提示词入门指南](../modules/prompts/chat_prompt_template.ipynb)。

## Chains: 把 LLMs 和提示词组合成多步工作流

到目前为止，我们已经单独使用了提示词模板和原生 LLM 调用。不过，真正的应用程序肯定不能只是简单调用原生 LLM，而应该是它们的组合。

LangChain 中的 chain 是由 links 组成的，链接可以是一个原生 LLM，也可以是其它 chain。

最核心的链类型是 LLMChain，它由一个提示词模板和一个 LLM 组成。

扩展一下之前的例子，我们构建一个 LLMChain，它接受用户输入，使用提示词模板格式化一下，再把结果发给 LLM。

```python
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
```

我们现在可以创建一个非常简单的 chain 先接受用户输入，然后格式化提示词，然后将它发送到 LLM：

```python
from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)
```

Now we can run that chain only specifying the product!

```python
chain.run("colorful socks")
# -> '\n\nSocktastic!'
```

运行一下吧！这是我们的第一个 Chain，一个 LLMChain。

这是一种很简单的 chain，不过有了这个基础，后面会更容易掌握复杂一点的 chain。

想了解更多细节，可以查看 [Chains 入门指南](../modules/chains/getting_started.ipynb)。

## Agents: 基于用户输入动态调用 Chains

目前为止，我们看到 chains 是按预定顺序调用的。

Agents 不再这么干了：先调用 LLM 来约定使用哪个 action 来执行，以及执行的顺序是怎样的。一个 action 可以使用 tool 并观察其输出，也可以返回给用户。

如果使用得当，Agents 会非常强大。在这个教程中，我们会给你展示怎么通过最简单、最高阶的 API 轻松使用 Agents。

想要加载 Agents，你需要理解这么几个概念：

- Tool: 执行特定任务的功能。这可以是：Google 搜索、数据库查找、Python REPL、其他链。tool 的接口目前是一个函数，传入字符串，返回字符串。
- LLM: 控制 agent 的大语言模型。
- Agent: 字符串类型，执行要使用哪个 agent 类。由于这个教程侧重于最简单、最高阶的 API，因此仅涵盖使用标准支持的 Agents。如果你想实现一个自定义 agent，请参阅自定义 agents 的文档（在路上了）。

**Agents**: 关于现有 agents 及其参数表，可以查看 [这里](../modules/agents/agents.md)。

**Tools**: 关于现有 tools 及其参数表，可以查看 [这里](../modules/agents/tools.md).

下面这个例子，需要先安装一下 SerpAPI 的 Python 包

```bash
pip install google-search-results
```

然后设置一下所需的环境变量。

```python
import os
os.environ["SERPAPI_API_KEY"] = "..."
```

现在就可以运行了！

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

## 记忆: 为 Chains 和 Agents 添加状态

目前为止，我们用的所有 Chains 和 Agents 都是无状态的。但通常，你可能希望 Chains 或 Agents 有“记忆”，以便它能记起之前的交互内容。这方面最清楚、最简单的例子是在设计聊天机器人时：你肯定希望它记住以前的消息，这样它就可以利用其中的上下文进行更好的对话。这需要一种“短期记忆”。在更复杂的场景下，一个 chain 或 agent 会需要记住更长时间的关键信息片段 —— 这将是一种“长期记忆”。关于长期记忆的更多具体想法，请参阅[这篇很棒的论文](https://memprompt.com/)。

LangChain 提供了几个专门为此目的创建的 chains。接下来我们会用一下 `ConversationChain`，它同时使用了长短两种不同类型 menory。

默认情况下，`ConversationChain` 有一种简单类型的记忆，可以记住所有以前的输入/输出并将它们添加到上下文中。咱们一起来看看使用这个链（设置 `verbose=True` 以便我们可以看到提示）。

```python
from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.predict(input="Hi there!")
print(output)
```

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
output = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
print(output)
```

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

## 构建语言模型应用: Chat 模型(Chat Models)

同样，你可以使用聊天模型而不是 LLMs。聊天模型 是语言模型的一个变体。虽然聊天模型底层用的是语言模型，但它们暴露的接口略有区别：它的 API 不是输入文本、返回文本，而是暴露了一个“聊天消息”的输入和输出。

Chat 模型是个新 API，我们还在探索怎么更好地抽象。

## 在 Chat 模型中补全对话(Message Completions)

你可以通过将一条或多条消息传递给聊天模型来补全对话。返回结果是一条消息。LangChain 目前支持的消息类型有 `AIMessage`, `HumanMessage`, `SystemMessage` 和 `ChatMessage` -- `ChatMessage` 接受任意角色参数。大多数时候，使用 `HumanMessage`, `AIMessage` 和 `SystemMessage` 就可以了。

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=0)
```

你可以通过传递一条消息来补全对话。

```python
chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})
```

你也可以传多条消息给 OpenAI 的 gpt-3.5-turbo 或 gpt-4 模型。

```python
messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Translate this sentence from English to French. I love programming.")
]
chat(messages)
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})
```

你可以进一步，使用 `generate` 为多组消息生成补全补全对话。返回结果是一个带有附加 `message` 参数的 `LLMResult`：

```python
batch_messages = [
    [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="Translate this sentence from English to French. I love programming.")
    ],
    [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="Translate this sentence from English to French. I love artificial intelligence.")
    ],
]
result = chat.generate(batch_messages)
result
# -> LLMResult(generations=[[ChatGeneration(text="J'aime programmer.", generation_info=None, message=AIMessage(content="J'aime programmer.", additional_kwargs={}))], [ChatGeneration(text="J'aime l'intelligence artificielle.", generation_info=None, message=AIMessage(content="J'aime l'intelligence artificielle.", additional_kwargs={}))]], llm_output={'token_usage': {'prompt_tokens': 71, 'completion_tokens': 18, 'total_tokens': 89}})
```

你可以从 LLMResult 获取到 token 使用量等信息：

```
result.llm_output['token_usage']
# -> {'prompt_tokens': 71, 'completion_tokens': 18, 'total_tokens': 89}
```

## 聊天提示词模板

你可以通过 `MessagePromptTemplate` 来使用模板。
你可以从一个或多个 `MessagePromptTemplate` 来构建一个 `ChatPromptTemplate`。
你可以用 `ChatPromptTemplate` 的 `format_prompt`(返回一个 `PromptValue`)，它能转换成字符串或者 `Message` 对象 —— 取决于你是要格式化成 llm 的输入还是传到 Chat 模型。

template 暴露了一个 `from_template` 方法，可以像下面这样用：

```python
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

chat = ChatOpenAI(temperature=0)

template="You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# get a chat completion from the formatted messages
chat(chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages())
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})
```

## 带 Chat 模型的 Chains

前面提到的 `LLMChain` 也可以和 Chat 模型一起使用：

```python
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

chat = ChatOpenAI(temperature=0)

template="You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chain = LLMChain(llm=chat, prompt=chat_prompt)
chain.run(input_language="English", output_language="French", text="I love programming.")
# -> "J'aime programmer."
```

## 带 Chat 模型的 Agents

Agents 也可以与聊天模型一起使用，你可以带着 `AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION` 参数初始化一个 agent。

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

## 记忆: 给 Chains 和 Agents 添加状态

你可以把 Memory 和 Chat 模型一起传入到 Chains 和 Agents 中。这么调用和 Memory for LLMs 的区别在于：它们可以作为一个独立可操作的 Memory 对象存在，而不是把之前的消息摘要成一个字符串。

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
