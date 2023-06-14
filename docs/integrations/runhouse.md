Runhouse（运行之家）


本页面介绍如何在LangChain中使用Runhouse生态系统。
它分为三个部分：安装和设置、LLMs和嵌入。


安装和设置
- 使用`pip install runhouse`安装Python SDK
- 如果您想使用按需集群，请使用`sky check`检查您的云凭据


自托管LLMs
对于基本的自托管LLM，您可以使用`SelfHostedHuggingFaceLLM`类。对于更多自定义的LLM，您可以使用`SelfHostedPipeline`父类。
custom LLMs, you can use the `SelfHostedPipeline` parent class.



```python

from langchain.llms import SelfHostedPipeline, SelfHostedHuggingFaceLLM

```



有关自托管LLMs的更详细步骤，请参阅此笔记本](../modules/models/llms/integrations/runhouse.ipynb)


自托管嵌入
通过Runhouse，您可以以多种方式在LangChain中使用自托管嵌入。


对于来自Hugging Face Transformers模型的基本自托管嵌入，您可以使用`SelfHostedEmbedding`类。
the `SelfHostedEmbedding` class.

```python

from langchain.llms import SelfHostedPipeline, SelfHostedHuggingFaceLLM

```



有关自托管嵌入的更详细步骤，请参阅此笔记本](../modules/models/text_embedding/examples/self-hosted.ipynb)
