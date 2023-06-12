# DeepInfra深度基础设施

This page covers how to use the DeepInfra ecosystem within LangChain.本页面介绍了如何在LangChain中使用DeepInfra生态系统。
It is broken into two parts: installation and setup, and then references to specific DeepInfra wrappers.它分为两个部分：安装和设置，然后参考特定的DeepInfra包装器。

## Installation and Setup安装和设置
- Get your DeepInfra api key from this link [here](https://deepinfra.com/).- 在此链接[https://deepinfra.com/]中获取您的DeepInfra API密钥。
- Get an DeepInfra api key and set it as an environment variable (`DEEPINFRA_API_TOKEN`)获取一个DeepInfra API密钥，并将其设置为环境变量(`DEEPINFRA_API_TOKEN`)

## Available Models可用模型

DeepInfra provides a range of Open Source LLMs ready for deployment.DeepInfra提供了一系列可以立即部署的开源LLMs。
You can list supported models [here](https://deepinfra.com/models?type=text-generation).您可以在这里列出受支持的模型[https://deepinfra.com/models?type=text-generation]。
google/flan\\* models can be viewed [here](https://deepinfra.com/models?type=text2text-generation).可以在这里查看google/flan*模型[https://deepinfra.com/models?type=text2text-generation]。

You can view a list of request and response parameters [here](https://deepinfra.com/databricks/dolly-v2-12b#API)您可以在这里查看请求和响应参数列表[https://deepinfra.com/databricks/dolly-v2-12b#API]

## Wrappers包装器

### LLM

There exists an DeepInfra LLM wrapper, which you can access with存在一个DeepInfra LLM包装器，您可以通过它进行访问
```python

from langchain.llms import DeepInfra

```

