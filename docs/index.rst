欢迎使用LangChain
==========================


| **LangChain** 是一个由语言模型驱动的应用程序开发框架。我们相信，最强大和独特的应用程序不仅仅调用语言模型，还会具备以下特点：
1. *数据感知*：将语言模型与其他数据源进行连接
2. *主动性*：允许语言模型与其环境进行交互

| LangChain框架是根据这些原则设计的。


| 这是关于Python的具体部分。有关LangChain的纯概念指南，请参见`here <https://docs.langchain.com/docs/>`_。有关JavaScript文档，请参见`此处 <https://js.langchain.com/docs/>`_。


入门指南
----------------



| 如何开始使用LangChain创建语言模型应用程序。


- `Quickstart Guide <./getting_started/getting_started.html>`_

| 概念和术语。


- `Concepts and terminology <./getting_started/concepts.html>`_


| 社区专家创建并在YouTube上介绍的教程


- `Tutorials <./getting_started/tutorials.html>`_


.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :name: getting_started
   :hidden:

   getting_started/getting_started.md
   getting_started/concepts.md
   getting_started/tutorials.md


Modules
-----------



| 这些模块是我们认为任何LLM驱动应用程序的构建块的核心抽象。对于每个模块，LangChain都提供标准、可扩展的接口。LangChain还提供外部集成甚至预制的端到端实现。




| 每个模块的文档都包含快速入门示例、操作指南、参考文档和概念指南。


| 这些模块（从最简单到最复杂）如下：


- `Models <./modules/models.html>`_: Supported model types and integrations.

- `Prompts <./modules/prompts.html>`_: Prompt management, optimization, and serialization.

- `Memory <./modules/memory.html>`_: Memory refers to state that is persisted between calls of a chain/agent.

- `Indexes <./modules/indexes.html>`_: Language models become much more powerful when combined with application-specific data - this module contains interfaces and integrations for loading, querying and updating external data.

- `Chains <./modules/chains.html>`_: Chains are structured sequences of calls (to an LLM or to a different utility).

- `Agents <./modules/agents.html>`_: An agent is a Chain in which an LLM, given a high-level directive and a set of tools, repeatedly decides an action, executes the action and observes the outcome until the high-level directive is complete.

- `Callbacks <./modules/callbacks/getting_started.html>`_: Callbacks let you log and stream the intermediate steps of any chain, making it easy to observe, debug, and evaluate the internals of an application.


.. toctree::

   :maxdepth: 1

   :caption: Modules

   :name: modules

   :hidden:



   ./modules/models.rst

   ./modules/prompts.rst

   ./modules/memory.md

   ./modules/indexes.md

   ./modules/chains.md

   ./modules/agents.md

   ./modules/callbacks/getting_started.ipynb



用例
----------



|用于常见LangChain用例的最佳实践和内置实现：




- `Autonomous Agents <./use_cases/autonomous_agents.html>`_: 自主代理是长时间运行的代理程序，它们采取许多步骤以尝试实现目标。例如AutoGPT和BabyAGI。

- `Agent Simulations <./use_cases/agent_simulations.html>`_: 将代理程序放入沙箱中，观察它们如何相互作用和对事件做出反应，可以是一种评估其长期推理和规划能力的有效方法。

- `Personal Assistants <./use_cases/personal_assistants.html>`_: LangChain的主要用例之一。个人助手需要采取行动，记住交互，并了解您的数据。

- `Question Answering <./use_cases/question_answering.html>`_: 另一个常见的LangChain用例。回答特定文档上的问题，仅利用这些文档中的信息构建答案。

- `Chatbots <./use_cases/chatbots.html>`_: 语言模型喜欢聊天，这使得它们成为非常自然的用途。

- `Querying Tabular Data <./use_cases/tabular.html>`_: 如果您想使用语言模型查询结构化数据（CSV、SQL、数据框等），建议阅读此文。

- `Code Understanding <./use_cases/code.html>`_: 如果您想使用语言模型分析代码，请阅读此文。

- `Interacting with APIs <./use_cases/apis.html>`_: 使语言模型能够与API交互非常强大。它为它们提供了访问最新信息并采取行动的能力。

- `Extraction <./use_cases/extraction.html>`_: 从文本中提取结构化信息。

- `Summarization <./use_cases/summarization.html>`_: 压缩更长的文档。数据增强生成的一种类型。

- `Evaluation <./use_cases/evaluation.html>`_: 使用传统度量方法很难评估生成模型。一种有前途的方法是使用语言模型本身进行评估。




.. toctree::

   :maxdepth: 1

   :caption: Use Cases

   :name: use_cases

   :hidden:



   ./use_cases/autonomous_agents.md

   ./use_cases/agent_simulations.md

   ./use_cases/personal_assistants.md

   ./use_cases/question_answering.md

   ./use_cases/chatbots.md

   ./use_cases/tabular.rst

   ./use_cases/code.md

   ./use_cases/apis.md

   ./use_cases/extraction.md

   ./use_cases/summarization.md

   ./use_cases/evaluation.rst





参考文档
---------------



| LangChain 的所有方法、类、安装方法和集成设置的完整文档。




- `LangChain Installation <./reference/installation.html>`_

- `Reference Documentation <./reference.html>`_


.. toctree::
   :maxdepth: 1
   :caption: Reference
   :name: reference
   :hidden:

   ./reference/installation.md
   ./reference.rst







生态系统
------------



| LangChain 集成了许多不同的 LLM、系统和产品。
| 从另一方面来看，许多系统和产品依赖于 LangChain。
| 它创造了一个充满活力和蓬勃发展的生态系统。






- `Integrations <./integrations.html>`_: 如何使用LangChain与其他产品集成的指南。

- `Dependents <./dependents.html>`_: 使用LangChain的存储库列表。

- `Deployments <./ecosystem/deployments.html>`_: 部署LangChain应用的指南、代码片段和模板存储库合集。


.. toctree::
   :maxdepth: 2
   :glob:
   :caption: Ecosystem
   :name: ecosystem
   :hidden:

   ./integrations.rst
   ./dependents.md
   ./ecosystem/deployments.md




其他资源
---------------------

| 额外的资源，我们认为在您开发应用程序时可能会有用！


- `LangChainHub <https://github.com/hwchase17/langchain-hub>`_: LangChainHub是一个共享和探索其他提示、链式和代理的地方。

- `Gallery <https://github.com/kyrolabs/awesome-langchain>`_: 一个收集使用Langchain的优秀项目的集合，由`Kyrolabs <https://kyrolabs.com>`_编译。有助于寻找灵感和示例实现。

- `Deploying LLMs in Production <./additional_resources/deploy_llms.html>`_: 有关在生产中部署LLMs的最佳实践和教程的合集。

- `Tracing <./additional_resources/tracing.html>`_: 使用跟踪在LangChain中可视化链式和代理的执行的指南。

- `Model Laboratory <./additional_resources/model_laboratory.html>`_: 尝试使用不同的提示、模型和链式是开发最佳应用程序的重要部分。ModelLaboratory使这个过程变得容易。

- `Discord <https://discord.gg/6adMQxSpJS>`_: 加入我们的Discord，讨论有关LangChain的所有事情！

- `YouTube <./additional_resources/youtube.html>`_: LangChain教程和视频的集合。

- `Production Support <https://forms.gle/57d8AmXBYp8PP8tZA>`_: 当您将LangChains移至生产环境时，我们很乐意提供更全面的支持。请填写此表格，我们将建立一个专门的支持Slack频道。


.. toctree::
   :maxdepth: 1
   :caption: Additional Resources
   :name: resources
   :hidden:

   LangChainHub <https://github.com/hwchase17/langchain-hub>
   ./additional_resources/deployments.md
   ./additional_resources/deploy_llms.rst
   Gallery <https://github.com/kyrolabs/awesome-langchain>
   ./additional_resources/tracing.md
   ./additional_resources/model_laboratory.ipynb
   Discord <https://discord.gg/6adMQxSpJS>
   ./additional_resources/youtube.md
   Production Support <https://forms.gle/57d8AmXBYp8PP8tZA>