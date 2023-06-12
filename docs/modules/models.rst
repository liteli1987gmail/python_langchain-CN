模型
==========================

.. note::
   `Conceptual Guide <https://docs.langchain.com/docs/components/models>`_


文档的这一部分涉及 LangChain 中使用的不同类型的模型。
在这个页面上，我们将在较高层次上介绍模型类型，但我们为每种模型类型提供了单独的页面。
这些页面包含使用该模型的更详细的“操作方法”指南，以及不同模型提供商的列表。

**LLMs**

大语言模型(LLMs)是我们要介绍的第一类模型。
模型输入的是字符串，返回的也是字符串。


**Chat 模型(Chat Models)**

Chat 模型是我们要介绍的第二类模型。
这类模型的底层是由language model来支持，API会更加结构后一些。
具体来说，这些模型将Chat Message列表作为输入，并返回Chat Message。

**预置文本模型(Text Embedding Models)**

预置文本模型(Text Embedding Models)是我们要介绍的第三类模型。
这类模型输入文本，返回floats列表。


Go Deeper
---------

.. toctree::
   :maxdepth: 1

   ./models/llms.rst
   ./models/chat.rst
   ./models/text_embedding.rst
