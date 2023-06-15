# Azure OpenAI



>[Microsoft Azure](https://en.wikipedia.org/wiki/Microsoft_Azure)，通常被称为 `Azure`，是由 `Microsoft` 运营的云计算平台，通过全球数据中心提供应用程序和服务的访问、管理和开发。它提供了一系列的功能，包括软件即服务（SaaS）、平台即服务（PaaS）和基础设施即服务（IaaS）。`Microsoft Azure` 支持许多编程语言、工具和框架，包括微软特定的和第三方的软件和系统。





>[Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) 是一个基于 `Azure` 的服务，其中包含来自 `OpenAI` 的强大语言模型，包括用于内容生成、摘要、语义搜索和自然语言转代码的 `GPT-3`、`Codex` 和 `Embeddings模型` 系列。





## 安装和设置



```bash

pip install openai

pip install tiktoken

```





设置环境变量以访问 `Azure OpenAI` 服务。



```python

import os



os.environ["OPENAI_API_TYPE"] = "azure"

os.environ["OPENAI_API_BASE"] = "https://<your-endpoint.openai.azure.com/"

os.environ["OPENAI_API_KEY"] = "你的 AzureOpenAI 密钥"

os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"

```



## LLM



查看 [使用示例](../modules/models/llms/integrations/azure_openai_example.ipynb)。



```python

from langchain.llms import AzureOpenAI

```



## 文本嵌入模型



查看 [使用示例](../modules/models/text_embedding/examples/azureopenai.ipynb)



```python

from langchain.embeddings import OpenAIEmbeddings

```



## 聊天模型



查看 [使用示例](../modules/models/chat/integrations/azure_chat_openai.ipynb)



```python

from langchain.chat_models import AzureChatOpenAI

```

