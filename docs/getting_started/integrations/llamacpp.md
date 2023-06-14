# Llama.cpp
短毛驼.cpp


This page covers how to use [llama.cpp](https://github.com/ggerganov/llama.cpp) within LangChain.
这个页面介绍了如何在LangChain中使用[短毛驼.cpp](https://github.com/ggerganov/llama.cpp)。
It is broken into two parts: installation and setup, and then references to specific Llama-cpp wrappers.
它分为两个部分：安装和设置，然后引用特定的短毛驼.cpp包装器。


## Installation and Setup
安装和设置
- Install the Python package with `pip install llama-cpp-python`
- 使用`pip install llama-cpp-python`安装Python包
- Download one of the [supported models](https://github.com/ggerganov/llama.cpp#description) and convert them to the llama.cpp format per the [instructions](https://github.com/ggerganov/llama.cpp)
- 下载[支持的模型](https://github.com/ggerganov/llama.cpp#description)之一，并根据[说明](https://github.com/ggerganov/llama.cpp)将它们转换为短毛驼.cpp格式


## Wrappers
包装器


### LLM



There exists a LlamaCpp LLM wrapper, which you can access with 
存在一个短毛驼.cpp LLM包装器，你可以通过它访问
```python

from langchain.llms import LlamaCpp

```

For a more detailed walkthrough of this, see [this notebook](../modules/models/llms/integrations/llamacpp.ipynb)
有关更详细的步骤，请参阅[此笔记本](../modules/models/llms/integrations/llamacpp.ipynb)


### Embeddings



There exists a LlamaCpp Embeddings wrapper, which you can access with 
存在一个短毛驼.cpp Embeddings包装器，你可以通过它访问
```python

from langchain.embeddings import LlamaCppEmbeddings

```

For a more detailed walkthrough of this, see [this notebook](../modules/models/text_embedding/examples/llamacpp.ipynb)
有关更详细的步骤，请参阅[此笔记本](../modules/models/text_embedding/examples/llamacpp.ipynb)
