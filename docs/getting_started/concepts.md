# 概念


开发LLM应用程序时常用的概念和术语。
它包含了首次引入该概念的外部论文或来源。
以及在LangChain中使用该概念的地方。


## 思维链


“思维链（CoT）”是一种提示技术，用于鼓励模型生成一系列中间推理步骤。
一种较不正式的诱导该行为的方法是在提示中包含“让我们一步一步地思考”。


- [Chain-of-Thought Paper](https://arxiv.org/pdf/2201.11903.pdf)

- [Step-by-Step Paper](https://arxiv.org/abs/2112.00114)



## 行动计划生成


“行动计划生成”是一种使用语言模型生成行动方案的提示技术。
然后可以将这些行动的结果反馈给语言模型以生成随后的行动。


- [WebGPT Paper](https://arxiv.org/pdf/2112.09332.pdf)

- [SayCan Paper](https://say-can.github.io/assets/palm_saycan.pdf)



## ReAct


“ReAct”是将思维链提示与行动计划生成相结合的提示技术。
这使得模型思考要采取的行动，然后采取行动。


- [Paper](https://arxiv.org/pdf/2210.03629.pdf)

- [LangChain Example](../modules/agents/agents/examples/react.ipynb)



## 自问


“自问”是在思维链提示的基础上构建的提示方法。
在这种方法中，模型明确向自己提问后续问题，然后由外部搜索引擎回答。


- [Paper](https://ofir.io/self-ask.pdf)

- [LangChain Example](../modules/agents/agents/examples/self_ask_with_search.ipynb)



## 提示链接


“提示链接”是将多个LLM调用组合在一起，其中一步的输出成为下一步的输入。


- [PromptChainer Paper](https://arxiv.org/pdf/2203.06566.pdf)

- [Language Model Cascades](https://arxiv.org/abs/2207.10342)

- [ICE Primer Book](https://primer.ought.org/)

- [Socratic Models](https://socraticmodels.github.io/)



## Memetic Proxy 模因代理


“模因代理”鼓励LLM以某种方式回应，将讨论框架化为模型所了解并导致该类型响应的上下文。
例如，学生和教师之间的对话。


##  自一致性 Self Consistency
- [Paper](https://arxiv.org/pdf/2102.07350.pdf)


“自一致性”是一种解码策略，它对一组多样化的推理路径进行抽样，然后选择最一致的答案。
与思维链提示结合使用时最有效。


- [Paper](https://arxiv.org/pdf/2203.11171.pdf)



## 启示


“启示”也称为“第一人称指令”。
通过在提示中包含模型回应的开头，鼓励模型以某种方式思考。


- [Example](https://twitter.com/goodside/status/1583262455207460865?s=20&t=8Hz7XBnK1OF8siQrxxCIGQ)



## 记忆提示


“记忆提示”保持错误和用户反馈的记忆，并使用它们来防止重复错误。


- [Paper](https://memprompt.com/)

