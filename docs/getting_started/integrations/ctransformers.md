C Transformers中文说明书

本页介绍如何在LangChain中使用C Transformers](https://github.com/marella/ctransformers)库。
它分为两部分：安装和设置，然后引用特定的C Transformers包装器。

安装和设置

- 使用`pip install ctransformers`安装Python包
- 下载支持的GGML模型](https://huggingface.co/TheBloke)（参见支持的模型](https://github.com/marella/ctransformers#supported-models)）

包装器

LLM

存在一个CTransformers LLM包装器，您可以通过以下方式访问：

```python

from langchain.llms import CTransformers

```


它为所有模型提供了一个统一的接口：

```python

llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2')



print(llm('AI is going to'))

```


如果出现`illegal instruction`错误，请尝试使用`lib='avx'`或`lib='basic'`：

```py

llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2', lib='avx')
```


它可以与在Hugging Face Hub上托管的模型一起使用：

```py

llm = CTransformers(model='marella/gpt-2-ggml')
```


如果模型仓库有多个模型文件（`.bin`文件），请使用以下方式指定模型文件：

```py

llm = CTransformers(model='marella/gpt-2-ggml', model_file='ggml-model.bin')
```


可以使用`config`参数传递其他参数：

```py

config = {'max_new_tokens': 256, 'repetition_penalty': 1.1}

llm = CTransformers(model='marella/gpt-2-ggml', config=config)
```


有关可用参数列表，请参阅文档](https://github.com/marella/ctransformers#config)。

有关更详细的演示，请参阅此笔记本](../modules/models/llms/integrations/ctransformers.ipynb)。
