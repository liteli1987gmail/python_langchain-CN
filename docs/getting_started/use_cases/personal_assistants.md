代理人



> 概念指南](https://docs.langchain.com/docs/use-cases/personal-assistants)





代理人能够用于各种任务。

代理人将语言模型的决策能力与工具相结合，以创建一个能够代表你执行和实现解决方案的系统

在继续阅读之前，强烈建议您阅读`agent`模块中的文档，以更好地理解与代理人相关的概念。

具体来说，在继续阅读之前，您应该熟悉`agent`、`tool`和`agent executor`的抽象概念。



- 代理人文档](../modules/agents.rst)（用于与外部世界交互）



## 创建您自己的代理人



在阅读了该文档后，您应该准备好创建自己的代理人了。

那具体包括什么？

以下是我们推荐您开始创建自己的代理人的步骤：



### 第一步：创建工具



代理人的定义很大程度上取决于它可以使用的工具。

如果您有特定的任务希望代理人完成，您必须给它访问正确工具的权限。

LangChain中有许多原生工具，所以您首先应该查看是否有任何工具符合您的需求。

但是如果您需要自定义工具，我们也可以轻松定义自定义工具。



### （可选）第二步：修改代理人



内置的LangChain代理人类型是为通用情况而设计的，

但是通过修改代理人实现，您可能能够提高性能。

有几种方法可以做到这一点：



1. 修改基本提示信息。这可用于为代理人提供更多关于其行为方式的上下文等。

2. 修改输出解析器。如果代理人在解析语言模型输出时遇到问题，这是必要的。



### （可选）第三步：修改代理人执行器



通常情况下，这一步骤是不必要的，因为这是相当通用的逻辑。

您可能希望修改的原因包括添加不同的停止条件或处理错误



## 示例



代理人的具体示例包括：



- AI插件](agents/custom_agent_with_plugin_retrieval.ipynb)：一个能够使用所有AI插件的代理人的实现。

- Plug-and-PlAI (Plugins Database)](agents/custom_agent_with_plugin_retrieval_using_plugnplai.ipynb)：一个能够使用从PlugNPlAI检索的所有AI插件的代理人的实现。

- Wikibase代理人](agents/wikibase_agent.ipynb)：与Wikibase进行交互的代理人的实现。

- 销售GPT](agents/sales_agent_with_context.ipynb)：这个笔记本演示了一个上下文感知的AI销售代理人的实现。

- 多模态输出代理人](agents/multi_modal_output_agent.ipynb)：一个能够生成文本和图像的多模态输出代理人的实现。

- [Multi-Modal Output Agent](agents/multi_modal_output_agent.ipynb): an implementation of a multi-modal output agent that can generate text and images.

