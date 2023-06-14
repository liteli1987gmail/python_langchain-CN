提示信息

==========================



注意：

   `概念指南 <https://docs.langchain.com/docs/components/prompts>`_





新的编程模型需要使用提示信息。

**提示信息** 指向模型输入。

这个输入通常是由多个组件构成的。

**PromptTemplate** 负责构建这个输入。

LangChain 提供了几个类和函数来方便地构建和使用提示信息。



|

- `入门指南 <./prompts/getting_started.html>`_: 提示信息的概述。





- `LLM 提示模板 <./prompts/prompt_templates.html>`_: 如何使用 PromptTemplates 提供语言模型提示。





- `聊天提示模板 <./prompts/chat_prompt_template.html>`_: 如何使用 PromptTemplates 提供聊天模型提示。





- `示例选择器 <./prompts/example_selectors.html>`_: 在提示信息中包含示例通常很有用。

  这些示例可以动态选择。本节介绍示例选择。





- `输出解析器 <./prompts/output_parsers.html>`_: 语言模型（和聊天模型）输出文本。

  但是很多时候，您可能想要获取更多结构化信息。这就是输出解析器的作用。

  输出解析器：



  - 指示模型应该如何格式化输出，
   - 解析输出到所需的格式中（包括必要时重试）。

  - parse output into the desired formatting (including retrying if necessary).







.. toctree::

   :maxdepth: 1

   :caption: 提示信息

   :name: prompts

   :hidden:



   ./prompts/getting_started.html

   ./prompts/prompt_templates.rst

   ./prompts/chat_prompt_template.html

   ./prompts/example_selectors.rst

   ./prompts/output_parsers.rst

