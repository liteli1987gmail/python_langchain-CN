聊天模型
==========================



注意：
   `概念指南 <https://docs.langchain.com/docs/components/models/chat-model>`_





聊天模型是语言模型的一种变体。
虽然聊天模型在后台使用语言模型，但它们所暴露的接口略有不同。
它们暴露了一个接口，其中“聊天消息”是输入和输出，而不是暴露“文本输入，文本输出”的 API。


聊天模型的 API 相当新，因此我们仍在研究正确的抽象。


提供以下文档部分：


- `入门指南 <./chat/getting_started.html>`_: LangChain LLM 类提供的所有功能的概述。


- `操作指南 <./chat/how_to_guides.html>`_: 操作指南的集合。这些突出了如何使用我们的 LLM 类实现各种目标（流式传输、异步等）。


- `集成 <./chat/integrations.html>`_: 不同的 LLM 提供商如何与 LangChain 集成的示例集合（OpenAI、Hugging Face 等）。




.. toctree::

   :maxdepth: 1
   :name: LLMs
   :hidden:


   ./chat/getting_started.ipynb
   ./chat/how_to_guides.rst
   ./chat/integrations.rst
