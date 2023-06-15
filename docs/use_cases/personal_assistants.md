# Agents



> [概念指南](https://docs.langchain.com/docs/use-cases/personal-assistants)





代理可以用于各种任务。

代理结合了语言模型的决策能力和工具，以创建一个可以代表您执行和实现解决方案的系统

在继续阅读之前，强烈建议您阅读`agent`模块中的文档，以更好地理解与代理相关的概念。

特别是，在继续阅读之前，您应该熟悉`agent`，`tool`和`agent executor`的抽象概念。



- [代理文档](../modules/agents.rst) (用于与外部世界进行交互)



## 创建您自己的代理



在阅读了那份文档后，您应该准备好创建自己的代理了。

那具体涉及哪些内容呢？

以下是我们推荐创建自己代理的步骤：



### 第1步：创建工具



代理的定义很大程度上取决于它可以使用的工具。

如果您有特定的任务要求代理完成，您必须给代理提供合适的工具。

我们在LangChain中提供了许多原生工具，因此您首先应该查看是否有任何工具符合您的需求。

但是我们还可以轻松定义自定义工具，所以如果您需要自定义工具，绝对可以这样做。



### （可选）第2步：修改代理



内置的LangChain代理类型被设计为在一般情况下可以很好地工作，

但是通过修改代理实现，您可能能够提高性能。

您可以通过以下几种方式来实现这一点：



1. 修改基本提示。这可用于给代理提供更多上下文信息以指导其行为等。

2. 修改输出解析器。如果代理在解析语言模型输出方面遇到问题，则需要进行修改。



### （可选）第3步：修改代理执行器



通常不需要进行此步骤，因为这是相当通用的逻辑。

您可能希望修改此部分的原因包括添加不同的停止条件或处理错误。



## 示例



代理的具体示例包括：



- [AI插件](agents/custom_agent_with_plugin_retrieval.ipynb)：一个实现了能够使用所有AI插件的代理。

- [Plug-and-PlAI（插件数据库）](agents/custom_agent_with_plugin_retrieval_using_plugnplai.ipynb)：一个实现了能够使用从PlugNPlAI检索的所有AI插件的代理。

- [Wikibase代理](agents/wikibase_agent.ipynb)：一个与Wikibase进行交互的代理的实现。

- [Sales GPT](agents/sales_agent_with_context.ipynb)：这个笔记本演示了一个上下文感知的AI销售代理的实现。

- [多模态输出代理](agents/multi_modal_output_agent.ipynb)：一个能够生成文本和图像的多模态输出代理的实现。

- [Multi-Modal Output Agent](agents/multi_modal_output_agent.ipynb): an implementation of a multi-modal output agent that can generate text and images.

