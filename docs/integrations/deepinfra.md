# DeepInfra深度基础设施



本页面介绍如何在LangChain中使用DeepInfra生态系统。

它分为两部分：安装和设置，以及对特定DeepInfra包装器的引用。



## 安装和设置

- 从此链接[这里](https://deepinfra.com/)获取您的DeepInfra API密钥。

- 获取DeepInfra API密钥并将其设置为环境变量（`DEEPINFRA_API_TOKEN`）



## 可用模型



DeepInfra提供了一系列可供部署的开源LLM模型。

您可以在[此处](https://deepinfra.com/models?type=text-generation)列出支持的模型。

google/flan\*模型可以在[此处](https://deepinfra.com/models?type=text2text-generation)查看。



您可以在[此处](https://deepinfra.com/databricks/dolly-v2-12b#API)查看请求和响应参数的列表。



## 包装器



### LLM



存在一个DeepInfra LLM包装器，您可以通过以下方式访问

```python

from langchain.llms import DeepInfra

```

