内存

==========================



。。。注意：

   `概念指南 <https://docs.langchain.com/docs/components/memory>`_





默认情况下，Chains和Agents是无状态的，

这意味着它们独立地对待每个传入的查询（就像底层的LLMs和聊天模型一样）。

在一些应用程序中（聊天机器人是一个很好的例子），记住之前的交互非常重要，不仅在短期内，而且在长期的层面上。

 **内存** 正好做到了这一点。

The **Memory** does exactly that.



LangChain以两种形式提供内存组件。

首先，LangChain提供了管理和操作以前的聊天消息的帮助程序。

这些被设计为模块化并且在如何使用它们方面是有用的。

其次，LangChain提供了将这些实用程序轻松整合到链中的方法。



|

- `入门指南 <./memory/getting_started.html>`_：介绍不同类型的内存。



- `操作指南 <./memory/how_to_guides.html>`_：包含不同类型内存的操作指南以及如何在链中使用内存的指南。







.. toctree::

   :maxdepth: 1

   :caption: Memory

   :name: Memory

   :hidden:



   ./memory/getting_started.html

   ./memory/how_to_guides.rst

