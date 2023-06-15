# 代理类型



代理使用LLM来确定采取的动作及其顺序。

动作可以是使用工具并观察其输出，也可以是向用户返回响应。

以下是LangChain中可用的代理。



## `zero-shot-react-description` 零射击反应描述



此代理使用ReAct框架来确定使用哪个工具

仅基于工具的描述。可以提供任意数量的工具。

此代理要求为每个工具提供描述。



## `react-docstore` 反应文档存储



此代理使用ReAct框架与文档存储进行交互。必须提供两个工具

一个是`Search`工具，一个是`Lookup`工具（它们的名称必须完全相同）。

`Search`工具应该搜索文档，而`Lookup`工具应该查找

最近找到的文档中的术语。

此代理等同于

原始的[ReAct论文](https://arxiv.org/pdf/2210.03629.pdf)，特别是维基百科示例。



## `self-ask-with-search` 使用搜索进行自问自答



此代理使用一个名为`Intermediate Answer`的工具。

该工具应能够查找问题的实际答案。该代理

等同于原始的[使用搜索进行自问自答的论文](https://ofir.io/self-ask.pdf)，

其中提供了Google搜索API作为工具。



### `conversational-react-description` 对话型反应描述



此代理旨在用于对话环境中。

提示旨在使代理变得有用且具有对话性。

它使用ReAct框架决定使用哪个工具，并使用内存记住以前的对话交互。

