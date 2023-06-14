指南

=============



本节中有三种示例类型：



1. 代理概述：通用代理功能的说明书

2. 代理工具包：特定代理工具包（针对与某个资源交互进行了优化的代理）的说明书

3. 代理类型：不同代理类型的说明书



代理概述

---------------



本部分如何指南的第一类涵盖了关于代理管理特定部分的内容。



`从 Hub 加载 <./examples/load_from_hub.html>`_：此笔记本介绍如何从 `LangChainHub <https://github.com/hwchase17/langchain-hub>`_ 加载代理。



`自定义工具 <./examples/custom_tools.html>`_：如何创建代理可以使用的自定义工具。



`带有向量存储的代理 <./examples/agent_vectorstore.html>`_：如何将向量存储与代理一起使用。



`中间步骤 <./examples/intermediate_steps.html>`_：如何访问和使用中间步骤以更深入了解代理的内部。



`自定义代理 <./examples/custom_agent.html>`_：如何创建自定义代理（特别是自定义 LLM + 提示以驱动该代理）。



`多输入工具 <./examples/multi_input_tool.html>`_：如何使用需要多个输入的工具与代理一起使用。



`搜索工具 <./examples/search_tools.html>`_：如何使用 LangChain 支持的不同类型的搜索工具。



`最大迭代次数 <./examples/max_iterations.html>`_：如何将代理限制为一定数量的迭代次数。



`异步 <./examples/async_agent.html>`_：涵盖异步功能。





.. toctree::

   :maxdepth: 1

   :glob:

   :hidden:



   ./agents/examples/*





代理工具包

---------------



下一组示例涵盖具有工具包的代理。

与上面的示例相反，这些示例旨在展示应用于特定用例的代理，

而不是展示代理“类型”。



`SQLDatabase 代理 <./toolkits/sql_database.html>`_：此笔记本涵盖如何使用代理与任意 SQL 数据库进行交互。



`JSON 代理 <./toolkits/json.html>`_：此笔记本涵盖如何使用代理与 JSON 字典进行交互。



`OpenAPI 代理 <./toolkits/openapi.html>`_：此笔记本涵盖如何使用代理与任意 OpenAPI 端点进行交互。



`VectorStore 代理 <./toolkits/vectorstore.html>`_：本笔记本涵盖使用代理与 VectorStores 进行交互的方法。



`Python 代理 <./toolkits/python.html>`_：此笔记本涵盖如何生成和执行 Python 代码以使用代理。



`Pandas DataFrame 代理 <./toolkits/pandas.html>`_：此笔记本涵盖如何在 Pandas 数据框架上进行问答，并使用代理。在底层，这调用了 Python 代理。



`CSV 代理 <./toolkits/csv.html>`_：此笔记本涵盖如何在 csv 文件上进行问答。在底层，这调用了 Pandas DataFrame 代理。



.. toctree::

   :maxdepth: 1

   :glob:

   :hidden:



   ./toolkits/*





代理类型

---------------



最后一组示例都是不同代理类型的端到端示例。

在所有示例中，都有一个具有特定工具集的代理。



- 工具：工具可以是任何接受字符串并返回字符串的内容。这意味着您可以使用本文档中找到的 `这里 <../chains.html>`_ 中的基本工具和链。LangChain 还提供了一系列易于加载的工具。有关详细信息，请参阅 `此文档 <./tools.html>`_

- 代理：代理使用 LLMChain 确定要使用的工具。有关所有可用代理类型的列表，请参见此处<./agents.html>。



**MRKL**
备注：MRKL是一种基于元语学习的后处理语言模型，用于对产生的错误进行后处理。依据：https://arxiv.org/pdf/2205.00445.pdf



- **使用的工具**：搜索，SQLDatabaseChain，LLMMathChain

- **使用的代理**：`zero-shot-react-description`

- `论文 <https://arxiv.org/pdf/2205.00445.pdf>`_

- **备注**：这是最通用的示例，因此，如果您要使用具有任意工具的代理，请从这里开始。

- `示例笔记本 <./implementations/mrkl.html>`_



**用搜索自问自答**
备注：Self-Ask-With-Search是一种用于自然语言处理问答的架构, 以实现文本数据的自问、自答和自学习。依据：https://ofir.io/self-ask.pdf



- **使用的工具**：搜索

- **使用的代理**：`self-ask-with-search`

- `论文 <https://ofir.io/self-ask.pdf>`_

- `示例笔记本 <./implementations/self_ask_with_search.html>`_



**ReAct**
备注：ReAct 是一种用于自然语言处理的句子分化系统，用于生成完整的问题-答案对，以支持问答式推理。依据：https://arxiv.org/pdf/2210.03629.pdf



- **使用的工具**：Wikipedia Docstore

- **使用的代理**：`react-docstore`

- `论文 <https://arxiv.org/pdf/2210.03629.pdf>`_

- `示例笔记本 <./implementations/react.html>`_











.. toctree::

   :maxdepth: 1

   :glob:

   :hidden:



   ./implementations/*





