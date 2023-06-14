GPT4All


本页面介绍如何在LangChain中使用GPT4All包装器。本教程分为两个部分：安装和设置，以及使用示例。


安装和设置


- 使用`pip install pyllamacpp`命令安装Python软件包
- 下载GPT4All模型](https://github.com/nomic-ai/pyllamacpp#supported-model)并将其放置在所需目录中


使用方法


GPT4All


要使用GPT4All包装器，您需要提供预训练模型文件的路径和模型的配置。


```python

from langchain.llms import GPT4All



# Instantiate the model. Callbacks support token-wise streaming

model = GPT4All(model="./models/gpt4all-model.bin", n_ctx=512, n_threads=8)



# Generate text

response = model("Once upon a time, ")

```



您还可以自定义生成参数，如n_predict、temp、top_p、top_k等。


如果要流式传输模型的预测结果，请添加CallbackManager。


```python

from langchain.llms import GPT4All

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler



# There are many CallbackHandlers supported, such as

# from langchain.callbacks.streamlit import StreamlitCallbackHandler



callbacks = [StreamingStdOutCallbackHandler()]

model = GPT4All(model="./models/gpt4all-model.bin", n_ctx=512, n_threads=8)



# Generate text. Tokens are streamed through the callback manager.

model("Once upon a time, ", callbacks=callbacks)

```



模型文件


您可以在pyllamacpp](https://github.com/nomic-ai/pyllamacpp)存储库中找到模型文件下载链接。


有关更详细的介绍，请参阅此笔记本](../modules/models/llms/integrations/gpt4all.ipynb)
