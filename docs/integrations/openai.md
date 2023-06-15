# Obsidian 收藏夹



> [Obsidian 收藏夹](https://obsidian.md/) 是一个功能强大且可扩展的知识库

，它基于您的本地文件夹中的纯文本文件进行工作。



## 安装和设置



以下是所有的操作指南示例。



## 文档加载器





请参阅 [使用示例](../modules/indexes/document_loaders/examples/obsidian.ipynb)。





pip install openai

from langchain.document_loaders import ObsidianLoader

- Get an OpenAI api key and set it as an environment variable (`OPENAI_API_KEY`)



```bash

pip install tiktoken

```





## LLM



```python

from langchain.llms import OpenAI

```



If you are using a model hosted on `Azure`, you should use different wrapper for that:

```python

from langchain.llms import AzureOpenAI

```

For a more detailed walkthrough of the `Azure` wrapper, see [this notebook](../modules/models/llms/integrations/azure_openai_example.ipynb)





## Text Embedding Model



```python

from langchain.embeddings import OpenAIEmbeddings

```

For a more detailed walkthrough of this, see [this notebook](../modules/models/text_embedding/examples/openai.ipynb)





## Chat Model



```python

from langchain.chat_models import ChatOpenAI

```

For a more detailed walkthrough of this, see [this notebook](../modules/models/chat/integrations/openai.ipynb)





## Tokenizer



There are several places you can use the `tiktoken` tokenizer. By default, it is used to count tokens

for OpenAI LLMs.



You can also use it to count tokens when splitting documents with 

```python

from langchain.text_splitter import CharacterTextSplitter

CharacterTextSplitter.from_tiktoken_encoder(...)

```

For a more detailed walkthrough of this, see [this notebook](../modules/indexes/text_splitters/examples/tiktoken.ipynb)



## Chain



See a [usage example](../modules/chains/examples/moderation.ipynb).



```python

from langchain.chains import OpenAIModerationChain

```



## Document Loader



See a [usage example](../modules/indexes/document_loaders/examples/chatgpt_loader.ipynb).



```python

from langchain.document_loaders.chatgpt import ChatGPTLoader

```



## Retriever



See a [usage example](../modules/indexes/retrievers/examples/chatgpt-plugin.ipynb).



```python

from langchain.retrievers import ChatGPTPluginRetriever

```

