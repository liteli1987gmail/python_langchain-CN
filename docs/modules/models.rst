模型

==========================



注释：

   `概念指南 <https://docs.langchain.com/docs/components/models>`_





本文档的这一部分涉及LangChain中使用的不同类型的模型。

在此页面上，我们将高层次地介绍模型类型，

但我们为每种模型类型都单独提供了页面。

这些页面包含了更详细的使用该模型的“如何”指南，

以及不同模型提供商的列表。



|

- `入门 <./models/getting_started.html>`_：模型概述。





模型类型

-----------



- `LLMs <./models/llms.html>`_：**Large Language Models (LLMs)**将文本字符串作为输入并返回文本字符串作为输出。



- `聊天模型 <./models/chat.html>`_：**Chat Models**通常由语言模型支持，但它们的API更加结构化。

  具体而言，这些模型将聊天消息列表作为输入，然后返回聊天消息。



- `文本嵌入模型 <./models/text_embedding.html>`_：**Text embedding models**将文本作为输入并返回浮点数列表。





.. toctree::

   :maxdepth: 1

   :caption: 模型

   :name: models

   :hidden:



   ./models/getting_started.html

   ./models/llms.rst

   ./models/chat.rst

   ./models/text_embedding.rst

