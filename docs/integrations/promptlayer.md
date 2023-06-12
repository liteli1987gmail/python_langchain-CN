# PromptLayer提示层

>[PromptLayer](https://docs.promptlayer.com/what-is-promptlayer/wxpF9EZkUwvdkwvVE9XEvC/how-promptlayer-works/dvgGSxNe6nB1jj8mUVbG8r) 是一个开发工具，允许您跟踪、管理和共享您的GPT提示工程。
> 它作为您的代码和OpenAI的Python库之间的中间件，记录所有您的API请求并保存相关元数据，以便在[提示层](https://www.promptlayer.com)仪表板中进行易于探索和搜索。
> 它作为您的代码和OpenAI的Python库之间的中间件，记录所有您的API请求并保存相关元数据，以便在[提示层](https://www.promptlayer.com)仪表板中进行易于探索和搜索。
> 它作为您的代码和OpenAI的Python库之间的中间件，记录所有您的API请求并保存相关元数据，以便在[提示层](https://www.promptlayer.com)仪表板中进行易于探索和搜索。

## Installation and Setup安装和设置

- Install the `promptlayer` python library 安装`promptlayer` Python库
```bash
pip install promptlayer

```

- Create a PromptLayer account创建一个PromptLayer账户
- Create an api token and set it as an environment variable (`PROMPTLAYER_API_KEY`)创建一个API token，并将其设置为环境变量（`PROMPTLAYER_API_KEY`）


## LLM

```python
from langchain.llms import PromptLayerOpenAI

```


### Example

To tag your requests, use the argument `pl_tags` when instantiating the LLM实例化LLM时，使用`pl_tags`来标记您的请求
```python
from langchain.llms import PromptLayerOpenAI

llm = PromptLayerOpenAI(pl_tags=["langchain-requests", "chatbot"])

```


To get the PromptLayer request id, use the argument `return_pl_id` when instantiating the LLM在实例化LLM时，使用参数`return_pl_id`来获取PromptLayer请求ID
```python
from langchain.llms import PromptLayerOpenAI

llm = PromptLayerOpenAI(return_pl_id=True)

```

This will add the PromptLayer request ID in the `generation_info` field of the `Generation` returned when using `.generate` or `.agenerate`使用`.generate`或`.agenerate`返回的`Generation`对象的`generation_info`字段中添加PromptLayer请求ID

For example:例如
```python
llm_results = llm.generate(["hello world"])

for res in llm_results.generations:

    print("pl request id: ", res[0].generation_info["pl_request_id"])

```

You can use the PromptLayer request ID to add a prompt, score, or other metadata to your request. [Read more about it here](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9).您可以使用PromptLayer请求ID向您的请求中添加提示,评分或其他元数据。[在此处阅读更多](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9)。

This LLM is identical to the [OpenAI LLM](./openai.md), except that这个LLM与[OpenAI LLM](./openai.md)几乎相同，不同的是
- all your requests will be logged to your PromptLayer account您的所有请求都将记录在您的PromptLayer账户中
- you can add `pl_tags` when instantiating to tag your requests on PromptLayer

- 在实例化时可以添加 `return_pl_id`，以返回一个 PromptLayer 请求 ID 供使用 [跟踪请求](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9)。


## 聊天模型


```python
from langchain.chat_models import PromptLayerChatOpenAI

```



See a [usage example](../modules/models/chat/integrations/promptlayer_chatopenai.ipynb).



