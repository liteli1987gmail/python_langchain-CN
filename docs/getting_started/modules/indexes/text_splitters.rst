文本分割器

==========================



.. 注意::

   `概念指南 <https://docs.langchain.com/docs/components/indexing/text-splitters>`_





当您想处理长篇文本时，需要将文本拆分成块。

尽管听起来很简单，但这里可能存在很多潜在的复杂性。理想情况下，您希望将语义相关的文本片段放在一起。"语义相关"的含义可能取决于文本类型。

本笔记本演示了几种做法。



在高层次上，文本分割器的工作原理如下：



1. 将文本分成小的、语义相关的块 (通常是句子)。

2. 开始将这些小块合并成较大的块，直到达到某个大小 (通过某些函数测量)。

3. 一旦达到了这个大小，将该块作为它自己的文本，然后开始创建一个新的文本块，其中包含一些重叠 (以保持块之间的上下文)。



这意味着有两个不同的轴可以自定义您的文本分割器：



1. 如何拆分文本

2. 如何测量块的大小



有关默认文本分割器和通用功能的介绍请参见：





.. toctree::

   :maxdepth: 1

   :glob:



   ./text_splitters/getting_started.ipynb





文本分割器的使用示例：



- `字符 <./text_splitters/examples/character_text_splitter.html>`_

- `代码 (包括 HTML、Markdown、Latex、Python 等) <./text_splitters/examples/code_splitter.html>`_

- `NLTK <./text_splitters/examples/nltk.html>`_

- `递归字符 <./text_splitters/examples/recursive_text_splitter.html>`_

- `spaCy <./text_splitters/examples/spacy.html>`_

- `tiktoken (OpenAI) <./text_splitters/examples/tiktoken_splitter.html>`_





.. toctree::

   :maxdepth: 1

   :caption: 文本分割器

   :name: text_splitters

   :hidden:



   ./text_splitters/examples/character_text_splitter.ipynb

   ./text_splitters/examples/code_splitter.ipynb

   ./text_splitters/examples/nltk.ipynb

   ./text_splitters/examples/recursive_text_splitter.ipynb

   ./text_splitters/examples/spacy.ipynb

   ./text_splitters/examples/tiktoken_splitter.ipynb





大多数LLM都受到可以传递的令牌数量的限制，这与字符数不同。

为了获得更准确的估计，我们可以使用分词器来计算文本中的标记数。

我们在 `..TextSplitter` 类的 `from_<tokenizer>` 方法中使用这个数字。

这实现为 `..TextSplitter` 类的 `from_<tokenizer>` 方法：



- `Hugging Face 分词器 <./text_splitters/examples/huggingface_length_function.html>`_

- `tiktoken (OpenAI) 分词器 <./text_splitters/examples/tiktoken.html>`_



.. toctree::

   :maxdepth: 1

   :caption: 基于令牌的文本分割器

   :name: text_splitter_with_tokens

   :hidden:



   ./text_splitters/examples/huggingface_length_function.ipynb

   ./text_splitters/examples/tiktoken.ipynb
