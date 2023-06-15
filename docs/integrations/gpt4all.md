# GPT4All 所有GPT4的文档


这个页面说明如何在LangChain中使用`GPT4All`包装器。教程分为两部分：安装和设置，以及使用示例。



## 安装和设置



- 使用 `pip install pyllamacpp` 命令安装Python包

- 下载[GPT4All模型](https://github.com/nomic-ai/pyllamacpp#supported-model)并将其放置在所需目录中



## 使用



### GPT4All



要使用GPT4All包装器，您需要提供预训练模型文件的路径和模型配置。



```python

from langchain.llms import GPT4All



# 实例化模型。回调支持逐标记流式传输

model = GPT4All(model="./models/gpt4all-model.bin", n_ctx=512, n_threads=8)



# 生成文本

response = model("从前有座山，")

```



您还可以自定义生成参数，如n_predict、temp、top_p、top_k等。



要通过回调管理器流式传输模型的预测，请添加回调管理器。



```python

from langchain.llms import GPT4All

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler



# 支持多种回调处理程序，例如

# from langchain.callbacks.streamlit import StreamlitCallbackHandler



callbacks = [StreamingStdOutCallbackHandler()]

model = GPT4All(model="./models/gpt4all-model.bin", n_ctx=512, n_threads=8)



# 生成文本。标记通过回调管理器流式传输

model("从前有座山，", callbacks=callbacks)

```



## 模型文件



您可以在[pyllamacpp](https://github.com/nomic-ai/pyllamacpp)代码仓库中找到模型文件的下载链接。



有关更详细的说明，请参阅[此笔记本](../modules/models/llms/integrations/gpt4all.ipynb)

