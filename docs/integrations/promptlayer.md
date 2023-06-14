提示层



>提示层](https://docs.promptlayer.com/what-is-promptlayer/wxpF9EZkUwvdkwvVE9XEvC/how-promptlayer-works/dvgGSxNe6nB1jj8mUVbG8r) 

> 是一个开发工具，允许您跟踪、管理和共享您的GPT提示工程。

> 它充当您的代码和OpenAI的Python库之间的中间件，记录所有的API请求

> 并保存相关的元数据，以便在提示层](https://www.promptlayer.com)仪表盘中轻松进行探索和搜索。



安装和设置



- 安装 `promptlayer` Python库

```bash

pip install promptlayer

```

- 创建一个PromptLayer账户

- 创建一个API令牌并将其设置为环境变量（`PROMPTLAYER_API_KEY`）





LLM



```python

from langchain.llms import PromptLayerOpenAI

```



示例



要为您的请求添加标签，请在实例化LLM时使用`pl_tags`参数

```python

from langchain.llms import PromptLayerOpenAI

llm = PromptLayerOpenAI(pl_tags=["langchain-requests", "chatbot"])

```



要获取PromptLayer请求ID，请在实例化LLM时使用`return_pl_id`参数

```python

from langchain.llms import PromptLayerOpenAI

llm = PromptLayerOpenAI(return_pl_id=True)

```

这将在使用`.generate`或`.agenerate`时将PromptLayer请求ID添加到`Generation`的`generation_info`字段中



例如:

```python

llm_results = llm.generate(["hello world"])

for res in llm_results.generations:

    print("pl request id: ", res[0].generation_info["pl_request_id"])

```

您可以使用PromptLayer请求ID为请求添加提示、分数或其他元数据。在此处阅读更多信息](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9)。



此LLM与OpenAI LLM](./openai.md)相同，不同之处在于

- 您的所有请求将被记录到您的PromptLayer账户中

- 您可以在实例化时添加`pl_tags`来标记您在PromptLayer上的请求

- 您可以在实例化时添加`return_pl_id`来返回PromptLayer请求ID，以便在跟踪请求](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9)时使用



聊天模型



```python

from langchain.chat_models import PromptLayerChatOpenAI

```



查看使用示例](../modules/models/chat/integrations/promptlayer_chatopenai.ipynb)。



