# Azure OpenAI（微软开放人工智能）

> [Microsoft Azure（微软Azure）](https://en.wikipedia.org/wiki/Microsoft_Azure)通常简称为 `Azure`，是由微软运营的云计算平台，通过全球数据中心提供应用和服务的访问、管理和开发。它提供了一系列能力，包括软件即服务（SaaS）、平台即服务（PaaS）和基础架构即服务（IaaS）。`微软Azure`支持许多编程语言、工具和框架，包括微软特定的和第三方软件和系统。


> [Azure OpenAI（微软开放人工智能）](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)是一个带有强大语言模型的 `Azure` 服务，包括 `OpenAI` 的 `GPT-3`、`Codex` 和 `Embeddings model` 系列，用于内容生成、摘要、语义搜索和自然语言转换为代码。


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

os.environ["OPENAI_API_KEY"] = "your AzureOpenAI key"

os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"

```


## LLM

请参阅[使用示例](../modules/models/llms/integrations/azure_openai_example.ipynb)。

```python
from langchain.llms import AzureOpenAI

```


## 文本嵌入模型

请参阅[使用示例](../modules/models/text_embedding/examples/azureopenai.ipynb)

```python
from langchain.embeddings import OpenAIEmbeddings

```


## 聊天模型

请参阅[使用示例](../modules/models/chat/integrations/azure_chat_openai.ipynb)

```python

from langchain.chat_models import AzureChatOpenAI

```

