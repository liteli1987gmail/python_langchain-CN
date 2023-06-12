代理人

> [概念指南](https://docs.langchain.com/docs/use-cases/personal-assistants)


代理人可用于各种任务。 
代理人将语言模型的决策能力与工具相结合，创建一个系统能够代表您执行和实现解决方案。在继续阅读之前,非常建议您阅读“代理”模块中的文档，以了解有关代理人概念的更多内容。
具体来说，,在阅读更多内容之前，您应该先了解“代理人”,“工具”和“代理人执行器”抽象的概念。

- [代理人文档](../modules/agents.rst)（与外部世界的交互）

## 创建您自己的代理

一旦您阅读了那篇文档，您就应该准备创建自己的代理。 
那具体涉及什么？
以下是我们建议开始创建自己的代理程序的方法:

### 第一步: 创建工具

代理人主要由其所能使用的工具定义。
如果您有特定的任务需要代理人完成，您必须为其提供访问正确工具的权限。
我们在LangChain中已经有很多原生工具，因此您应该首先查看是否有任何工具能够满足您的需求。
但是，我们也可以轻松定义自定义工具，因此，如果您需要自定义工具，绝对可以这样做。

### （可选）第二步: 修改代理人

LangChain内置的代理人类型设计用于在通用情况下工作良好，
但是您可能可以通过修改代理人执行方式来提高性能。
有几种方法可以实现这一点：
but you may be able to improve performance by modifying the agent implementation.

There are several ways you could do this:



1. 修改基本提示。这可以用来给代理程序更多上下文信息，以确定它应该如何行事等等。# Modify the base prompt. This can be used to give the agent more context on how it should behave, etc.
2. 修改输出解析器。如果代理程序在解析语言模型输出方面遇到问题，这是必需的。# Modify the output parser. This is necessary if the agent is having trouble parsing the language model output.


### （可选）第三步：修改代理执行器。# (Optional) Step 3: Modify Agent Executor


此步骤通常不是必需的，因为这是相当通用的逻辑。# This step is usually not necessary, as this is pretty general logic.
您想要修改的可能原因包括添加不同的停止条件或处理错误。# Possible reasons you would want to modify this include adding different stopping conditions, or handling errors


## 示例。# ## Examples


代理的具体示例包括:。# Specific examples of agents include:


- [AI插件](agents/custom_agent_with_plugin_retrieval.ipynb):是一个实现代理程序的示例，旨在能够使用所有AI插件。
- [Plug-and-PlAI（插件数据库）](agents/custom_agent_with_plugin_retrieval_using_plugnplai.ipynb):是一个实现代理程序的示例，旨在能够使用从PlugNPlAI检索的所有AI插件。
- [Wikibase代理程序](agents/wikibase_agent.ipynb):是一个与Wikibase交互的代理实现。
- [销售GPT](agents/sales_agent_with_context.ipynb):，本笔记演示了一个上下文感知的AI销售代理的实现。
- [Multi-Modal Output Agent](agents/multi_modal_output_agent.ipynb): an implementation of a multi-modal output agent that can generate text and images.

