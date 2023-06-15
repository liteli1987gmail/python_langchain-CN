# Runhouse室


本页面介绍如何在LangChain中使用[Runhouse](https://github.com/run-house/runhouse)生态系统。

它分为三个部分：安装和设置、LLMs和Embeddings。



## 安装和设置

- 使用`pip install runhouse`安装Python SDK

- 如果您想使用按需集群，请使用`sky check`检查您的云凭据



## 自托管LLMs

对于基本的自托管LLM，您可以使用`SelfHostedHuggingFaceLLM`类。对于更多自定义的LLMs，您可以使用`SelfHostedPipeline`父类。





```python

from langchain.llms import SelfHostedPipeline，SelfHostedHuggingFaceLLM

```



有关自托管LLMs的更详细步骤，请参阅[此笔记本](../modules/models/llms/integrations/runhouse.ipynb)



## 自托管Embeddings

通过Runhouse，有几种方法可以使用LangChain的自托管Embeddings。



对于来自Hugging Face Transformers模型的基本自托管嵌入，您可以使用`SelfHostedEmbedding`类。



```python

from langchain.llms import SelfHostedPipeline，SelfHostedHuggingFaceLLM

```



有关自托管Embeddings的更详细步骤，请参阅[此笔记本](../modules/models/text_embedding/examples/self-hosted.ipynb)

