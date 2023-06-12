# 概念


这些是开发LLM应用程序时常用的概念和术语。
它包含了最初引入该概念的外部论文或来源,
以及在LangChain中使用该概念的地方。


## 思维链


`思维链（CoT）`是一种提示技术，用于鼓励模型生成一系列中间推理步骤。
一种较不正式的诱导这种行为的方法是在提示中包含“让我们逐步思考”


- [Chain-of-Thought论文](https://arxiv.org/pdf/2201.11903.pdf)
- [逐步论文](https://arxiv.org/abs/2112.00114)


## 行动计划生成


`行动计划生成`是一种提示技术，使用语言模型生成要采取的行动。
然后，这些行动的结果可以反馈到语言模型中，以生成随后的行动。


- [WebGPT论文](https://arxiv.org/pdf/2112.09332.pdf)
- [SayCan论文](https://say-can.github.io/assets/palm_saycan.pdf)


## ReAct


`ReAct`是一种将思维链提示与行动计划生成相结合的提示技术。
这迫使模型考虑采取什么行动，,然后采取行动。


- [论文](https://arxiv.org/pdf/2210.03629.pdf)
- [LangChain示例](../modules/agents/agents/examples/react.ipynb)


## 自问


`自问`是建立在思维链提示之上的提示方法。
在这种方法中，,模型明确地问自己后续问题，,然后由外部搜索引擎回答。


- [Paper](https://ofir.io/self-ask.pdf)

- [LangChain Example](../modules/agents/agents/examples/self_ask_with_search.ipynb)

## Prompt Chaining

Prompt Chaining 是将多个 LLM 调用组合起来，其中一个步骤的输出成为下一个步骤的输入。

- [PromptChainer Paper](https://arxiv.org/pdf/2203.06566.pdf)
- [Language Model Cascades](https://arxiv.org/abs/2207.10342)
- [ICE Primer Book](https://primer.ought.org/)
- [Socratic Models](https://socraticmodels.github.io/)

## Memetic Proxy

Memetic Proxy 鼓励 LLM 以某种方式进行响应，并将讨论框架置于模型所知道的上下文中，从而导致该类型的响应。
例如，作为学生和老师之间的对话。

- [Paper](https://arxiv.org/pdf/2102.07350.pdf)

## Self Consistency

Self Consistency 是一种解码策略，它采样多种推理路径，然后选择最一致的答案。
与 Chain-of-thought 提示相结合时最有效。

- [Paper](https://arxiv.org/pdf/2203.11171.pdf)

## Inception

Inception 又称 First Person Instruction。
它通过在提示中包含模型响应的开头来鼓励模型以某种方式思考。

- [Example](https://twitter.com/goodside/status/1583262455207460865?s=20&t=8Hz7XBnK1OF8siQrxxCIGQ)

## MemPrompt

MemPrompt 维护错误和用户反馈的记忆，并使用它们来防止重复错误。

`MemPrompt` maintains a memory of errors and user feedback, and uses them to prevent repetition of mistakes.



- [Paper](https://memprompt.com/)

