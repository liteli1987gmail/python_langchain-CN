代理类型

代理使用LLM确定采取哪些行动以及按什么顺序进行。
一个行动可以是使用工具并观察其输出，或者向用户返回响应。
以下是LangChain中可用的代理。

零-shot-react-description

该代理使用ReAct框架来确定使用哪个工具，仅基于工具的描述。可以提供任意数量的工具。
该代理要求为每个工具提供描述。

react-docstore
## `react-docstore`


该代理使用ReAct框架与文档存储进行交互。必须提供两个工具：一个“搜索”工具和一个“查找”工具（它们的名称必须完全一致）
“搜索”工具应该搜索文档，而“查找”工具应该查找最近找到的文档中的一个术语。

该代理等同于原始的ReAct论文](https://arxiv.org/pdf/2210.03629.pdf)，特别是维基百科的示例。

self-ask-with-search



该代理使用一个名为“Intermediate Answer”的工具。该工具应能够查找问题的事实答案。该代理等同于原始的self ask with search论文](https://ofir.io/self-ask.pdf)，其中提供了Google搜索API作为工具。
This agent utilizes a single tool that should be named `Intermediate Answer`.


conversational-react-description
where a Google search API was provided as the tool.




该代理设计用于会话环境。提示被设计为使代理有帮助且具备对话能力。它使用ReAct框架决定使用哪个工具，并使用内存来记住先前的对话交互。
This agent is designed to be used in conversational settings.

The prompt is designed to make the agent helpful and conversational.

It uses the ReAct framework to decide which tool to use, and uses memory to remember the previous conversation interactions.

