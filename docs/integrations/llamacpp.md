# Llama.cpp


This page covers how to use [llama.cpp](https://github.com/ggerganov/llama.cpp) within LangChain.
It is broken into two parts: installation and setup, and then references to specific Llama-cpp wrappers.


## 安装和设置
- 用 `pip install llama-cpp-python` 安装Python包
- 下载任何一个[支持的模型](https://github.com/ggerganov/llama.cpp#description)，并按照[instructions](https://github.com/ggerganov/llama.cpp) 转换为llama.cpp格式


## Wrappers


### LLM


存在一个LlamaCpp LLM wrapper，可以用以下方式访问 
```python
from langchain.llms import LlamaCpp

```

有关此项操作的更详细步骤，请参见[此笔记本电脑](../modules/models/llms/integrations/llamacpp.ipynb)


### Embeddings


存在一个LlamaCpp Embeddings wrapper，可以用以下方式访问 
```python
from langchain.embeddings import LlamaCppEmbeddings

```

For a more detailed walkthrough of this, see [this notebook](../modules/models/text_embedding/examples/llamacpp.ipynb)

