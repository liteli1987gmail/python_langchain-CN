GPT4All# 全面了解GPT4All


本页介绍如何在LangChain中使用GPT4All包装器。本教程分为两部分：安装和设置，以及通过示例使用。


## 安装和设置


- 使用`pip install pyllamacpp`安装Python包
- 下载[GPT4All模型](https://github.com/nomic-ai/pyllamacpp#supported-model)并将其放置在所需目录中


## 使用


### GPT4All


要使用GPT4All包装器，您需要提供预训练模型文件的路径和模型的配置。


```pythonfrom pyllamacpp.gpt4all import Gpt4Allmodel_path = 'path/to/model'config_path = 'path/to/config'model = Gpt4All()model.load(model_path, config_path)prompts = ['prompt 1', 'prompt 2']for prompt in prompts:    output, state = model.generate(prompt, length=20)    print(output)```
from langchain.llms import GPT4All



# Instantiate the model. Callbacks support token-wise streaming

model = GPT4All(model="./models/gpt4all-model.bin", n_ctx=512, n_threads=8)



# Generate text

response = model("Once upon a time, ")

```



您还可以自定义生成参数，例如n_predict、temp、top_p、top_k等。


要流式传输模型的预测，请添加CallbackManager。


```pythonfrom pyllamacpp.callbacks import CallbackManagerfrom pyllamacpp.gpt4all import Gpt4Allmodel_path = 'path/to/model'config_path = 'path/to/config'model = Gpt4All()model.load(model_path, config_path)prompts = ['prompt 1', 'prompt 2']with CallbackManager(model, verbose=True) as callbacks:    for prompt in prompts:        output, state = model.generate(prompt, length=20)        print(output)```
from langchain.llms import GPT4All

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler



# There are many CallbackHandlers supported, such as

# from langchain.callbacks.streamlit import StreamlitCallbackHandler



callbacks = [StreamingStdOutCallbackHandler()]

model = GPT4All(model="./models/gpt4all-model.bin", n_ctx=512, n_threads=8)



# Generate text. Tokens are streamed through the callback manager.

model("Once upon a time, ", callbacks=callbacks)

```



## 模型文件


您可以在[pyllamacpp](https://github.com/nomic-ai/pyllamacpp)存储库中找到模型文件下载链接。


For a more detailed walkthrough of this, see [this notebook](../modules/models/llms/integrations/gpt4all.ipynb)

