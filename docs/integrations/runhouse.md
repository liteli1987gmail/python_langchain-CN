运行房屋


本页面介绍如何在LangChain中使用[Runhouse](https://github.com/run-house/runhouse)生态系统。
它分为三个部分：安装和设置,LLMs,和嵌入。


## 安装和设置
- 使用`pip install runhouse`安装Python SDK。
- 如果您想使用按需集群，使用`sky check`检查云凭据。


## 自托管LLMs
对于基本的自托管LLM，您可以使用`SelfHostedHuggingFaceLLM`类。 对于更多
自定义LLMs，可以使用`SelfHostedPipeline`父类。


```python

from langchain.llms import SelfHostedPipeline, SelfHostedHuggingFaceLLM

```



有关自托管LLMs的更详细的演练，请参见[此笔记本电脑]( ../ modules / models / llms / integrations / runhouse.ipynb)


## 自托管嵌入
There are several ways to use self-hosted embeddings with LangChain via Runhouse.



通过Runhouse，有几种使用自托管嵌入在LangChain中的方法。
对于来自Hugging Face Transformers模型的基本自托管嵌入，您可以使用
```python

from langchain.llms import SelfHostedPipeline, SelfHostedHuggingFaceLLM

```



For a more detailed walkthrough of the Self-hosted Embeddings, see [this notebook](../modules/models/text_embedding/examples/self-hosted.ipynb)

