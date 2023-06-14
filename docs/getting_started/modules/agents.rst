代理
==========================



注意：
   `概念指南 <https://docs.langchain.com/docs/components/agents>`_




某些应用程序不仅需要对LLMs/其他工具进行预定调用的链路，
而且可能需要一个依赖用户输入的未知链路。
在这些类型的链路中，有一个 **代理** 可以访问一组 **工具**。
基于用户输入，代理可以决定是否需要调用这些工具中的任何一个。


目前，代理主要分两种类型：


1. **动作代理**：这些代理决定要执行哪些操作并一次执行一个操作。
2. **计划和执行代理**：这些代理首先决定要执行的行动计划，然后逐个执行这些行动。


在什么情况下使用每种代理? 动作代理更为传统，适用于小型任务。
对于更复杂或长时间运行的任务，最初的规划步骤有助于实现长期目标和重点。
然而，这是以通常需要更多的调用和更高的延迟为代价的。
这两个代理也不是互相排斥的——事实上，通常最好由动作代理负责执行计划和执行代理。
的执行。


动作代理
-------------



动作代理的高层伪代码：


- 接收 **用户输入**
- **代理** 决定是否使用哪个 **工具**，以及 **工具输入** 应该是什么
- 然后使用 **工具输入** 调用那个 **工具**，并记录一个 **观察结果** (这个调用的输出)
- 将 **工具**、**工具输入** 和 **观察结果** 的历史记录传回 **代理**，然后它决定下一步该做什么
- 重复以上步骤，直到 **代理** 决定不再需要使用 **工具**，然后直接回应用户。




代理涉及的不同抽象为：


- **代理**：这是应用程序的逻辑所在的地方。代理公开一个接口，该接口接收用户输入
    以及代理采取的先前步骤列表，并返回 **AgentAction** 或 **AgentFinish**


    - **AgentAction** 对应于要使用的工具和该工具的输入
      - **AgentFinish** 表示代理已经完成，有关应返回给用户的信息也已经确定了
    - **工具**：这是代理可以执行的操作。你给代理提供什么样的工具与你想让代理做什么有极大关系
    - **工具包**：这是专为特定用例设计的工具集。例如，为了让代理以最佳方式与SQL数据库进行交互，它可能需要访问一个工具以执行查询和一个工具以检查表
    - **代理执行器**：这将代理和工具列表进行封装。它负责循环运行代理，直到满足停止条件为止。
  - **AgentFinish** means the agent is done, and has information around what to return to the user

- **Tools**: these are the actions an agent can take. What tools you give an agent highly depend on what you want the agent to do

- **Toolkits**: these are groups of tools designed for a specific use case. For example, in order for an agent to

  interact with a SQL database in the best way it may need access to one tool to execute queries and another tool to inspect tables.

- **Agent Executor**: this wraps an agent and a list of tools. This is responsible for the loop of running the agent

  iteratively until the stopping criteria is met.





|
- `入门指南 <./agents/getting_started.html>`_：代理的概述。它涵盖了如何使用与代理相关的所有内容，从整体上介绍。




|
**代理构建：**


尽管代理可以以多种方式构建，但构建代理的典型方法是使用：


- **PromptTemplate**：它负责获取用户输入和先前步骤，并构建一个提示文本以发送给语言模型

- **语言模型**：它接受由 PromptTemplate 构建的提示文本并返回一些输出

- **输出解析器**：它将语言模型的输出解析为 **AgentAction** 或 **AgentFinish** 对象。

- **Output Parser**: this takes the output of the Language Model and parses it into an **AgentAction** or **AgentFinish** object.





|
**附加文档：**




- `工具 <./agents/tools.html>`_：LangChain 支持的不同类型的 **工具**。我们也介绍了如何添加你自己的工具。



- `代理 <./agents/agents.html>`_：LangChain 支持的不同类型的 **代理**。我们还介绍了如何修改和创建您自己的代理。

- `工具包 <./agents/toolkits.html>`_：LangChain 支持的各种 **工具包**，以及如何从它们创建代理。



- `代理执行器 <./agents/agent_executors.html>`_：负责调用代理和工具形成循环。我们介绍了不同的自定义方法，以及可以用于更精细控制的选项。

  create an agent from them.



- `Agent Executor <./agents/agent_executors.html>`_: The **Agent Executor** class, which is responsible for calling

  the agent and tools in a loop. We go over different ways to customize this, and options you can use for more control.





计划和执行代理
-----------------------

**计划和执行代理** 的高层伪代码：


- 接收 **用户输入**
- **规划者** 列出要执行的步骤

- **执行者** 逐个执行步骤



最典型的实现方式是让规划者成为语言模型，执行者成为动作代理。


|
- `计划和执行代理 <./agents/plan_and_execute.html>`_





.. toctree::

   :maxdepth: 1

   :hidden:



   ./agents/getting_started.ipynb

   ./agents/tools.rst

   ./agents/agents.rst

   ./agents/toolkits.rst

   ./agents/agent_executors.rst

   ./agents/plan_and_execute.ipynb



