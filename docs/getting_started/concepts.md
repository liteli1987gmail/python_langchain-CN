# 概念



这些是开发LLM应用程序常用的概念和术语。

其中包含了对首次引入该概念的外部论文或来源的参考

以及在LangChain中使用该概念的位置。



## 思维链



`思维链（CoT）`是一种提示技术，用于鼓励模型生成一系列中间推理步骤。

一种更不正式的诱导此行为的方法是在提示中包含“让我们一步一步地思考”。



- [`思维链`论文](https://arxiv.org/pdf/2201.11903.pdf)

- [`逐步思考`论文](https://arxiv.org/abs/2112.00114)



## 行动计划生成



`行动计划生成`是一种使用语言模型生成要执行的行动的提示技术。

这些行动的结果可以再次馈送到语言模型中生成后续的行动。



- [`WebGPT`论文](https://arxiv.org/pdf/2112.09332.pdf)

- [`SayCan`论文](https://say-can.github.io/assets/palm_saycan.pdf)



## ReAct



`ReAct`是将思维链提示与行动计划生成相结合的一种提示技术。

这使模型思考要采取的行动，然后采取行动。



- [论文](https://arxiv.org/pdf/2210.03629.pdf)

- [LangChain示例](../modules/agents/agents/examples/react.ipynb)



## 自问



`自问`是在思维链提示的基础上构建的一种提示方法。

在该方法中，模型明确向自己提出后续问题，然后由外部搜索引擎进行回答。



- [论文](https://ofir.io/self-ask.pdf)

- [LangChain示例](../modules/agents/agents/examples/self_ask_with_search.ipynb)



## 提示链



`提示链`是将多个LLM调用组合在一起，其中一步的输出成为下一步的输入。



- [`PromptChainer`论文](https://arxiv.org/pdf/2203.06566.pdf)

- [`语言模型级联`](https://arxiv.org/abs/2207.10342)

- [`ICE Primer`图书](https://primer.ought.org/)

- [`Socratic Models`](https://socraticmodels.github.io/)



## 文化代理



`文化代理`是鼓励LLM以一定方式进行响应，通过以模型熟悉的上下文来构建讨论框架，

从而导致特定类型的响应。

例如，将其视为学生和教师之间的对话。



- [论文](https://arxiv.org/pdf/2102.07350.pdf)

- [Paper](https://arxiv.org/pdf/2102.07350.pdf)



## 自洽



`自洽`是一种解码策略，它对推理路径进行多样化采样，然后选择最一致的答案。

在与思维链提示相结合时效果最好。



- [论文](https://arxiv.org/pdf/2203.11171.pdf)



## Inception



`Inception`也称为`第一人称指导`。

通过在提示中包含模型响应的开头，鼓励模型以某种方式进行思考。



- [示例](https://twitter.com/goodside/status/1583262455207460865?s=20&t=8Hz7XBnK1OF8siQrxxCIGQ)



## MemPrompt



`MemPrompt`保持错误和用户反馈的记忆，并使用它们防止重复错误。



- [论文](https://memprompt.com/)

