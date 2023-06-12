大语言模型(LLMs)
==========================

.. note::
   `Conceptual Guide <https://docs.langchain.com/docs/components/models/language-model>`_


大语言模型(LLMs) 是 LangChain 的核心组件。
LangChain 不提供LLMs，而是提供一个标准化接口，你可以通过这些接口与各种 LLM 进行交互。

下面是一些LLMs的文档：

- `入门指南 <./llms/getting_started.html>`_: LangChain LLM 类提供的所有功能的概述。

- `操作指引 <./llms/how_to_guides.html>`_: 操作指引的集合。这些重点介绍了如何使用我们的 LLM 类（streaming、async等）实现各种目标。

- `集成文档 <./llms/integrations.html>`_: 关于如何将不同的大语言模型(OpenAI、Hugging Face 等)与 LangChain 集成的示例集合。

- `Reference <../../reference/modules/llms.html>`_: API reference documentation for all LLM classes.


.. toctree::
   :maxdepth: 1
   :name: LLMs
   :hidden:
   
   ./llms/getting_started.ipynb
   ./llms/how_to_guides.rst
   ./llms/integrations.rst
   Reference<../../reference/modules/llms.rst>
