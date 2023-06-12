C转换器


本页面介绍如何在LangChain中使用[C Transformers](https://github.com/marella/ctransformers)库。
它分为两部分：安装和设置，然后引用特定的C转换器包装器。


安装和设置


- 使用`pip install ctransformers`安装Python包
- 下载支持的[GGML模型](https://huggingface.co/TheBloke) (参见[受支持的模型](https://github.com/marella/ctransformers#supported-models))


包装器


LLM


存在一个CTransformers LLM包装器，您可以使用以下方式访问:


```python

from langchain.llms import CTransformers

```



它为所有模型提供了统一的接口:


```python

llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2')



print(llm('AI is going to'))

```



如果遇到`illegal instruction`错误，请尝试使用`lib='avx'`或`lib='basic'`:


```py
llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2', lib='avx')

```



它可以与Hugging Face Hub上托管的模型一起使用:


```py
llm = CTransformers(model='marella/gpt-2-ggml')

```



如果一个模型repo有多个模型文件（`.bin`文件），请使用以下方式指定一个模型文件:


```py
llm = CTransformers(model='marella/gpt-2-ggml', model_file='ggml-model.bin')

```



可以使用`config`参数传递其他参数:


```py
config = {'max_new_tokens': 256, 'repetition_penalty': 1.1}



llm = CTransformers(model='marella/gpt-2-ggml', config=config)

```



有关可用参数的列表，请参见[文档](https://github.com/marella/ctransformers#config)。


For a more detailed walkthrough of this, see [this notebook](../modules/models/llms/integrations/ctransformers.ipynb).

