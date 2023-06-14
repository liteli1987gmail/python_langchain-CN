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
For each module LangChain provides standard, extendable interfaces. LangChain also provides external integrations and even end-to-end implementations for off-the-shelf use.



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


- `Autonomous Agents <./use_cases/autonomous_agents.html>`_: Autonomous agents are long-running agents that take many steps in an attempt to accomplish an objective. Examples include AutoGPT and BabyAGI.

- `Agent Simulations <./use_cases/agent_simulations.html>`_: Putting agents in a sandbox and observing how they interact with each other and react to events can be an effective way to evaluate their long-range reasoning and planning abilities.

- `Personal Assistants <./use_cases/personal_assistants.html>`_: One of the primary LangChain use cases. Personal assistants need to take actions, remember interactions, and have knowledge about your data.

- `Question Answering <./use_cases/question_answering.html>`_: Another common LangChain use case. Answering questions over specific documents, only utilizing the information in those documents to construct an answer.

- `Chatbots <./use_cases/chatbots.html>`_: Language models love to chat, making this a very natural use of them.

- `Querying Tabular Data <./use_cases/tabular.html>`_: Recommended reading if you want to use language models to query structured data (CSVs, SQL, dataframes, etc).

- `Code Understanding <./use_cases/code.html>`_: Recommended reading if you want to use language models to analyze code.

- `Interacting with APIs <./use_cases/apis.html>`_: Enabling language models to interact with APIs is extremely powerful. It gives them access to up-to-date information and allows them to take actions.

- `Extraction <./use_cases/extraction.html>`_: Extract structured information from text.

- `Summarization <./use_cases/summarization.html>`_: Compressing longer documents. A type of Data-Augmented Generation.

- `Evaluation <./use_cases/evaluation.html>`_: Generative models are hard to evaluate with traditional metrics. One promising approach is to use language models themselves to do the evaluation.




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






- `Integrations <./integrations.html>`_: Guides for how other products can be used with LangChain.

- `Dependents <./dependents.html>`_: List of repositories that use LangChain.

- `Deployments <./ecosystem/deployments.html>`_: A collection of instructions, code snippets, and template repositories for deploying LangChain apps.



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