欢迎使用LangChain
==========================



| **LangChain** 是一个开发由语言模型驱动的应用程序框架。我们相信，最强大和不同的应用程序不仅会调用语言模型，还将是：1. *数据智能*：将语言模型连接到其他数据源2. *代理能力*：允许语言模型与其环境交互
1. *Data-aware*: connect a language model to other sources of data

2. *Agentic*: allow a language model to interact with its environment



| LangChain框架是根据这些原则设计的。


| 这是关于Python的具体部分。有关LangChain的纯概念指南，请参见`此处 <https://docs.langchain.com/docs/>`_。有关JavaScript文档，请参见`此处 <https://js.langchain.com/docs/>`_。


入门指南
----------------



| 如何开始使用LangChain创建语言模型应用程序。


- `快速入门指南 <./getting_started/getting_started.html>`_


| 概念和术语。


- `概念和术语 <./getting_started/concepts.html>`_


| 社区专家创建并在YouTube上介绍的教程


- `教程 <./getting_started/tutorials.html>`_


.. toctree::

   :maxdepth: 2

   :caption: Getting Started

   :name: getting_started

   :hidden:



   getting_started/getting_started.md

   getting_started/concepts.md

   getting_started/tutorials.md





模块
-----------



| 这些模块是我们认为任何LLM驱动应用程序的构建块的核心抽象。对于每个模块，LangChain都提供标准、可扩展的接口。LangChain还提供外部集成甚至预制的端到端实现。
For each module LangChain provides standard, extendable interfaces. LangChain also provides external integrations and even end-to-end implementations for off-the-shelf use.



| 每个模块的文档都包含快速入门示例、操作指南、参考文档和概念指南。


| 这些模块（从最简单到最复杂）如下：


- `模型 <./modules/models.html>`_：支持的模型类型和集成。


- `提示 <./modules/prompts.html>`_：提示管理、优化和序列化。


- `Memory <./modules/memory.html>`_: Memory refers to state that is persisted between calls of a chain/agent.



- `Indexes <./modules/indexes.html>`_: 语言模型结合应用程序特定的数据更加强大，该模块包含用于加载、查询和更新外部数据的接口和集成。


- `Chains <./modules/chains.html>`_: 链是调用（到LLM或不同的实用程序）的结构化序列。


- `Agents <./modules/agents.html>`_: 代理是指LLM在高级指令和一组工具的情况下，重复决策、执行操作并观察结果，直到完成高级指令的链。


- `Callbacks <./modules/callbacks/getting_started.html>`_: 回调允许您记录和流式传输任何链的中间步骤，使得观察、调试和评估应用程序的内部变得容易。


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


- `自主代理 <./use_cases/autonomous_agents.html>`_: 自主代理是长时间运行的代理，需要执行许多步骤以完成目标。示例包括AutoGPT和BabyAGI。


- `代理模拟 <./use_cases/agent_simulations.html>`_: 将代理置于沙盒中，观察它们相互交互和对事件的反应，可以有效地评估它们的长距离推理和规划能力。


- `个人助手 <./use_cases/personal_assistants.html>`_: 其中一个主要的LangChain用例。个人助手需要采取行动、记住交互并具有关于您的数据的知识。


- `问答 <./use_cases/question_answering.html>`_: 另一个常见的LangChain用例。仅利用这些文档中的信息来构建答案，回答特定文件中的问题。


- `Chatbots <./use_cases/chatbots.html>`_: Language models love to chat, making this a very natural use of them.



- `查询表格数据<./use_cases/tabular.html>`_:如果您想使用语言模型查询结构化数据（CSV、SQL、数据框等），建议阅读。


- `代码理解<./use_cases/code.html>`_:如果您想使用语言模型分析代码，建议阅读。


- `与API互动<./use_cases/apis.html>`_:使语言模型与API互动非常强大。它使它们可以访问最新的信息并允许它们采取行动。


- `数据提取<./use_cases/extraction.html>`_:从文本中提取结构化信息。


- `摘要<./use_cases/summarization.html>`_:压缩较长的文档。数据增强生成的一种类型。


- `评估<./use_cases/evaluation.html>`_:使用传统指标评估生成模型很困难。一种有前途的方法是使用语言模型本身进行评估。




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




- `LangChain安装<./reference/installation.html>`_


- `参考文档<./reference.html>`_


.. toctree::

   :maxdepth: 1

   :caption: Reference

   :name: reference

   :hidden:



   ./reference/installation.md

   ./reference.rst





生态系统
------------



| LangChain 集成了许多不同的 LLM、系统和产品。| 从另一方面来看，许多系统和产品依赖于 LangChain。| 它创造了一个充满活力和蓬勃发展的生态系统。
| From the other side, many systems and products depend on LangChain.

| It creates a vibrant and thriving ecosystem.





- `集成<./integrations.html>`_:指南，介绍如何将其他产品与 LangChain 配合使用。


- `依赖项<./dependents.html>`_:使用 LangChain 的存储库列表。


- `部署<./ecosystem/deployments.html>`_:一系列部署 LangChain 应用程序的说明、代码片段和模板存储库。




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



| Additional resources we think may be useful as you develop your application!



- `LangChainHub <https://github.com/hwchase17/langchain-hub>`_: LangChainHub是一个共享和探索其他提示、链式和代理的地方。#The LangChainHub is a place to share and explore other prompts, chains, and agents.


- `Gallery <https://github.com/kyrolabs/awesome-langchain>`_: 一个收集使用Langchain的优秀项目的集合，由`Kyrolabs <https://kyrolabs.com>`_编译。有助于寻找灵感和示例实现。#A collection of great projects that use Langchain, compiled by the folks at `Kyrolabs <https://kyrolabs.com>`_. Useful for finding inspiration and example implementations.


- `Deploying LLMs in Production <./additional_resources/deploy_llms.html>`_: 有关在生产中部署LLMs的最佳实践和教程的集合。#A collection of best practices and tutorials for deploying LLMs in production.


- `Tracing <./additional_resources/tracing.html>`_: 使用跟踪在LangChain中可视化链式和代理的执行的指南。#A guide on using tracing in LangChain to visualize the execution of chains and agents.


- `Model Laboratory <./additional_resources/model_laboratory.html>`_: 尝试使用不同的提示、模型和链式是开发最佳应用程序的重要部分。ModelLaboratory使这个过程变得容易。#Experimenting with different prompts, models, and chains is a big part of developing the best possible application. The ModelLaboratory makes it easy to do so.


- `Discord <https://discord.gg/6adMQxSpJS>`_: 加入我们的Discord，讨论有关LangChain的所有事情！#Join us on our Discord to discuss all things LangChain!


- `YouTube <./additional_resources/youtube.html>`_: LangChain教程和视频的集合。#A collection of the LangChain tutorials and videos.


- `Production Support <https://forms.gle/57d8AmXBYp8PP8tZA>`_: As you move your LangChains into production, we'd love to offer more comprehensive support. Please fill out this form and we'll set up a dedicated support Slack channel.





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

