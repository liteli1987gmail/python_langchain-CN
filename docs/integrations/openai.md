OpenAI（人工智能研究实验室）


OpenAI是一家美国人工智能(AI)研究实验室[1]，由非盈利OpenAI Incorporated和其盈利子公司OpenAI Limited Partnership组成。
> consisting of the non-profit `OpenAI Incorporated`

> and its for-profit subsidiary corporation `OpenAI Limited Partnership`. 

OpenAI进行AI研究，以促进和发展友好的AI为声明意图。
OpenAI系统运行在Microsoft的Azure基于的超级计算平台上。


OpenAI API由一组具有不同能力和价格点的多样模型提供支持。
> 

ChatGPT是OpenAI开发的人工智能聊天机器人。


安装和设置
使用以下命令安装Python SDK
```bash

pip install openai

```

- Get an OpenAI api key and set it as an environment variable (`OPENAI_API_KEY`)

如果您想使用OpenAI的分词器(仅适用于Python 3.9+)，请进行安装。
```bash

pip install tiktoken

```





LLM


用以下命令进行安装。
from langchain.llms import OpenAI

```



如果您正在使用托管在Azure上的模型，应使用不同的包装器。
```python

from langchain.llms import AzureOpenAI

```

有关Azure包装器的更详细演练，请参见此笔记本。




文本嵌入模型


```python

from langchain.embeddings import OpenAIEmbeddings

```

有关详细步骤，请参见此笔记本。




聊天模型


```python

from langchain.chat_models import ChatOpenAI

```

有关详细步骤，请参见此笔记本。




## Tokenizer



你可以在几个地方使用`tiktoken`分词器。默认情况下，它用于计算OpenAI LLM中的标记数。（There are several places you can use the `tiktoken` tokenizer. By default, it is used to count tokens for OpenAI LLMs.）
for OpenAI LLMs.



您还可以在使用Python时将其用于拆分文档。
```python

from langchain.text_splitter import CharacterTextSplitter

CharacterTextSplitter.from_tiktoken_encoder(...)

```

有关更详细的说明，请参阅此笔记本（../modules/indexes/text_splitters/examples/tiktoken.ipynb）。(For a more detailed walkthrough of this, see [this notebook](../modules/indexes/text_splitters/examples/tiktoken.ipynb))


## 链


查看一个[用法示例](../modules/chains/examples/moderation.ipynb)。(See a [usage example](../modules/chains/examples/moderation.ipynb))


```python

from langchain.chains import OpenAIModerationChain

```



## 文档加载器


查看一个[用法示例](../modules/indexes/document_loaders/examples/chatgpt_loader.ipynb)。(See a [usage example](../modules/indexes/document_loaders/examples/chatgpt_loader.ipynb))


```python

from langchain.document_loaders.chatgpt import ChatGPTLoader

```



## Retriever


See a [usage example](../modules/indexes/retrievers/examples/chatgpt-plugin.ipynb).



```python

from langchain.retrievers import ChatGPTPluginRetriever

```

