输出解析器

==========================



.. 注意：

   `概念指南 <https://docs.langchain.com/docs/components/prompts/output-parser>`_





语言模型输出文本。但是很多时候，您可能想要获得比文本更结构化的信息。这就是输出解析器的作用。



输出解析器是帮助结构化语言模型响应的类。有两个主要方法，输出解析器必须实现：



- ``get_format_instructions() -> str``: 一种方法，返回一个字符串，其中包含有关如何格式化语言模型的输出的说明。

- ``parse(str) -> Any``: 一种方法，将一个字符串作为输入(假定为语言模型的响应)，并将其解析为某种结构。



然后有一个可选项：



- ``parse_with_prompt(str) -> Any``: 一种方法，它接收一个字符串(假定为语言模型的响应)和一个提示(假定为生成此响应的提示)，并将其解析为某种结构。提示主要是为了在OutputParser希望以某种方式重试或修复输出时提供信息，并需要从提示中获取信息以进行操作。



首先，我们建议您熟悉入门部分



.. toctree::

   :maxdepth: 1



   ./output_parsers/getting_started.md



然后，我们提供了有关所有不同类型的输出解析器的深入介绍。



.. toctree::

   :maxdepth: 1

   :glob:



   ./output_parsers/examples/*
