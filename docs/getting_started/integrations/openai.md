# OpenAI



>[OpenAI](https://en.wikipedia.org/wiki/OpenAI)是美国的人工智能（AI）研究实验室

>由非盈利机构'OpenAI Incorporated'和其营利性附属公司'OpenAI Limited Partnership'组成

>'OpenAI'进行AI研究并声明促进和发展友好AI

>'OpenAI'系统在'Microsoft'的基于'Azure'的超级计算平台上运行





>[OpenAI API](https://platform.openai.com/docs/models)由各种能力和价格不同的模型驱动



>'OpenAI'开发的人工智能（AI）聊天机器人[ChatGPT](https://chat.openai.com)



## 安装和设置

- 使用以下命令安装Python SDK

```bash

pip install openai

```

- 获取OpenAI api密钥并将其设置为环境变量（`OPENAI_API_KEY`）

- 如果您想使用OpenAI的分词器（仅适用于Python 3.9+），请安装它

```bash

pip install tiktoken

```





## LLM



```python

from langchain.llms import OpenAI

```



如果您正在使用托管在'Azure'上的模型，您应该使用不同的封装器:

```python

from langchain.llms import AzureOpenAI

```

有关'Azure'封装器的详细演练，请参见[此笔记本](../modules/models/llms/integrations/azure_openai_example.ipynb)





## 文本嵌入模型



```python

from langchain.embeddings import OpenAIEmbeddings

```

有关此详细步骤，请参见[此笔记本](../modules/models/text_embedding/examples/openai.ipynb)





## 聊天模型



```python

from langchain.chat_models import ChatOpenAI

```

有关此详细步骤，请参见[此笔记本](../modules/models/chat/integrations/openai.ipynb)





## 分词器



您可以在多个地方使用'tiktoken'分词器。默认情况下，它用于计算OpenAI LLMs的标记数





您还可以将其用于在拆分文档时计算标记数

```python

from langchain.text_splitter import CharacterTextSplitter

CharacterTextSplitter.from_tiktoken_encoder(...)

```

有关此详细步骤，请参见[此笔记本](../modules/indexes/text_splitters/examples/tiktoken.ipynb)



## 链



查看[使用示例](../modules/chains/examples/moderation.ipynb)



```python

from langchain.chains import OpenAIModerationChain

```



## 文档加载器



查看[使用示例](../modules/indexes/document_loaders/examples/chatgpt_loader.ipynb)



```python

from langchain.document_loaders.chatgpt import ChatGPTLoader

```



## 检索器



查看[使用示例](../modules/indexes/retrievers/examples/chatgpt-plugin.ipynb)



```python

from langchain.retrievers import ChatGPTPluginRetriever

```

