# 代理类型

代理使用LLM确定采取哪些行动以及顺序。
行动可以是使用工具并观察其输出，也可以是向用户返回响应。
下面是LangChain中可用的代理。

## `零-shot-react-description`(ReAct框架中的Agent类型)

该代理使用ReAct框架根据工具的描述来确定使用哪个工具，且可以提供任意数量的工具。
该代理需要为每个工具提供描述。

## `react-docstore`(ReAct框架中的Agent类型)

该代理使用ReAct框架与docstore交互。必须提供两个工具，一个“搜索”工具和一个“查找”工具（它们必须被准确命名）。
“搜索”工具应该搜索文档，而“查找”工具应该在最近找到的文档中查找一个术语。
该代理与原始的[ReAct论文](https://arxiv.org/pdf/2210.03629.pdf)等价，具体是关于维基百科的例子。

## `self-ask-with-search`(自我查询论文中的Agent类型)

该代理利用一个名为“中间答案”的工具。该工具应该能够查找事实性问题的答案。该代理与原始的[self ask with search论文](https://ofir.io/self-ask.pdf)等价，其中提供了Google搜索API作为工具。

### `会话式-react-description`(ReAct框架中的Agent类型)

该代理设计用于会话式环境。提示旨在使代理具有帮助性和交谈性。它使用ReAct框架来决定使用哪个工具，并使用记忆来记住先前的交互。








It uses the ReAct framework to decide which tool to use, and uses memory to remember the previous conversation interactions.

