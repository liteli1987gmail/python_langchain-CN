# Helicone 涡轮


本页面介绍如何在LangChain中使用[Helicone](https://helicone.ai)生态系统。



## Helicone 是什么？



Helicone是一个[开放源代码](https://github.com/Helicone/helicone)的可观测性平台，代理您的OpenAI流量并为您提供有关开销、延迟和使用情况的重要见解。



![Helicone 涡轮](../_static/HeliconeDashboard.png)



## 快速入门



使用您的LangChain环境，您只需添加以下参数。



```bash

export OPENAI_API_BASE="https://oai.hconeai.com/v1"

```



现在转到[helicone.ai](https://helicone.ai/onboarding?step=2)创建您的帐户，并在我们的控制面板中添加您的OpenAI API密钥以查看日志。



![Helicone 涡轮](../_static/HeliconeKeys.png)



## 如何启用 Helicone 缓存



```python

from langchain.llms import OpenAI

import openai

openai.api_base = "https://oai.hconeai.com/v1"



llm = OpenAI(temperature=0.9, headers={"Helicone-Cache-Enabled": "true"})

text = "什么是涡轮？"

print(llm(text))

```



[Helicone 缓存文档](https://docs.helicone.ai/advanced-usage/caching)



## 如何使用 Helicone 自定义属性



```python

from langchain.llms import OpenAI

import openai

openai.api_base = "https://oai.hconeai.com/v1"



llm = OpenAI(temperature=0.9, headers={

        "Helicone-Property-Session": "24",

        "Helicone-Property-Conversation": "support_issue_2",

        "Helicone-Property-App": "mobile",

      })

text = "什么是涡轮？"

print(llm(text))

```



[Helicone 自定义属性文档](https://docs.helicone.ai/advanced-usage/custom-properties)

