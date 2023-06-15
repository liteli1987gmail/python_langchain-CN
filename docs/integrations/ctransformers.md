# C Transformers C 转换器



This page covers how to use the [C Transformers](https://github.com/marella/ctransformers) library within LangChain. 本页介绍如何在LangChain中使用[C Transformers](https://github.com/marella/ctransformers)库。

It is broken into two parts: installation and setup, and then references to specific C Transformers wrappers. 它分为两个部分：安装和设置，然后引用特定的C Transformers封装。



## Installation and Setup 安装和设置



- Install the Python package with `pip install ctransformers` 用`pip install ctransformers`安装Python包

- Download a supported [GGML model](https://huggingface.co/TheBloke) (see [Supported Models](https://github.com/marella/ctransformers#supported-models)) 下载支持的[GGML模型](https://huggingface.co/TheBloke) (参见[支持的模型](https://github.com/marella/ctransformers#supported-models))



## Wrappers 封装器



### LLM



There exists a CTransformers LLM wrapper, which you can access with: 存在一个CTransformers LLM封装器，您可以通过以下方式访问:



```python

from langchain.llms import CTransformers

```



It provides a unified interface for all models: 它为所有模型提供了一个统一的接口:



```python

llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2')



print(llm('AI is going to'))

```



If you are getting `illegal instruction` error, try using `lib='avx'` or `lib='basic'`: 如果出现`illegal instruction`错误，请尝试使用`lib='avx'`或`lib='basic'`:



```py

llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2', lib='avx')

```



It can be used with models hosted on the Hugging Face Hub: 它可以与托管在Hugging Face Hub上的模型一起使用:



```py

llm = CTransformers(model='marella/gpt-2-ggml')

```



If a model repo has multiple model files (`.bin` files), specify a model file using: 如果模型仓库有多个模型文件（`.bin`文件），请使用以下方式指定模型文件:



```py

llm = CTransformers(model='marella/gpt-2-ggml', model_file='ggml-model.bin')

```



Additional parameters can be passed using the `config` parameter: 可以使用`config`参数传递附加参数:



```py

config = {'max_new_tokens': 256, 'repetition_penalty': 1.1}



llm = CTransformers(model='marella/gpt-2-ggml', config=config)

```



See [Documentation](https://github.com/marella/ctransformers#config) for a list of available parameters. 有关可用参数的列表，请参阅[文档](https://github.com/marella/ctransformers#config)。



For a more detailed walkthrough of this, see [this notebook](../modules/models/llms/integrations/ctransformers.ipynb). 有关更详细的说明，请参阅[此笔记本](../modules/models/llms/integrations/ctransformers.ipynb)。

