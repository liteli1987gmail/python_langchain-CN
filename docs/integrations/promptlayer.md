# PromptLayer



>[PromptLayer](https://docs.promptlayer.com/what-is-promptlayer/wxpF9EZkUwvdkwvVE9XEvC/how-promptlayer-works/dvgGSxNe6nB1jj8mUVbG8r) 

> 是一款开发工具，可以跟踪、管理和共享您的 GPT prompt 工程。 

> 作为您的代码和 OpenAI 的 python 库之间的中间件，可以记录您的所有 API 请求

> 并保存相关元数据，以便在 [PromptLayer](https://www.promptlayer.com) 仪表板中轻松浏览和搜索。



## 安装和设置



- 安装 `promptlayer` python 库

```bash

pip install promptlayer

```

- 创建 PromptLayer 账户

- 创建 api token 并将其设置为环境变量 (`PROMPTLAYER_API_KEY`)





## LLM



```python

from langchain.llms import PromptLayerOpenAI

```



### 示例



要为您的请求添加标签，请在实例化 LLM 时使用参数 `pl_tags`

```python

from langchain.llms import PromptLayerOpenAI

llm = PromptLayerOpenAI(pl_tags=["langchain-requests", "chatbot"])

```



要获取 PromptLayer 请求 ID，请在实例化 LLM 时使用参数 `return_pl_id`

```python

from langchain.llms import PromptLayerOpenAI

llm = PromptLayerOpenAI(return_pl_id=True)

```

这将在使用 `.generate` 或 `.agenerate` 时，在 `Generation` 的 `generation_info` 字段中添加 PromptLayer 请求 ID



例如：

```python

llm_results = llm.generate(["hello world"])

for res in llm_results.generations:

    print("pl request id: ", res[0].generation_info["pl_request_id"])

```

您可以使用 PromptLayer 请求 ID 向请求中添加提示、分数或其他元数据。[在此处阅读更多](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9)。



此 LLM 与 [OpenAI LLM](./openai.md) 相同，区别在于

- 所有请求都会记录到您的 PromptLayer 账户

- 您可以在实例化时添加 `pl_tags` 来标记 PromptLayer 上的请求

- 您可以在实例化时添加 `return_pl_id` 来返回 PromptLayer 请求 ID 以便进行[跟踪请求](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9)。



## 聊天模型



```python

from langchain.chat_models import PromptLayerChatOpenAI

```



查看 [使用示例](../modules/models/chat/integrations/promptlayer_chatopenai.ipynb)。



