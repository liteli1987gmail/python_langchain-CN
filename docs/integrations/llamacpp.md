# Llama.cpp


本页介绍了如何在LangChain中使用[llama.cpp](https://github.com/ggerganov/llama.cpp)。

它分为两个部分：安装和设置，以及具体的Llama-cpp封装的引用。



## 安装和设置

- 使用`pip install llama-cpp-python`命令安装Python包

- 下载其中一个[支持的模型](https://github.com/ggerganov/llama.cpp#description)，并按照[说明](https://github.com/ggerganov/llama.cpp)将其转换为llama.cpp格式



## 封装



### LLM



存在一个名为LlamaCpp LLM的封装，您可以使用以下方式访问

```python

from langchain.llms import LlamaCpp

```

要了解更详细的步骤，请参阅[此笔记本](../modules/models/llms/integrations/llamacpp.ipynb)



### 嵌入



存在一个名为LlamaCpp Embeddings的封装，您可以使用以下方式访问

```python

from langchain.embeddings import LlamaCppEmbeddings

```

要了解更详细的步骤，请参阅[此笔记本](../modules/models/text_embedding/examples/llamacpp.ipynb)

