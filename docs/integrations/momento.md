# Momento



>[Momento Cache](https://docs.momentohq.com/) 是全球首个真正的无服务器缓存服务。它提供即时弹性、零间隙扩展能力和惊人的性能。

> 使用 Momento Cache，您获取 SDK，获得一个端点，在您的代码中输入几行代码，即可立即使用。





本页面介绍如何在LangChain中使用 [Momento](https://gomomento.com) 生态系统。



## 安装和设置



- 在此处免费注册账户[here](https://docs.momentohq.com/getting-started) 并获得身份验证令牌

- 使用 `pip install momento` 命令安装 Momento Python SDK





## 缓存



缓存包装器允许将 [Momento](https://gomomento.com) 用作 LLM prompts 和 responses 的服务器无缝缓存。





标准缓存是 [Momento](https://gomomento.com) 用户在任何环境中使用的首选用例。



按照以下方式导入缓存：



```python

from langchain.cache import MomentoCache

```



并进行如下设置：



```python

from datetime import timedelta

from momento import CacheClient, Configurations, CredentialProvider

import langchain



# 实例化 Momento 客户端

cache_client = CacheClient(

    Configurations.Laptop.v1(),

    CredentialProvider.from_environment_variable("MOMENTO_AUTH_TOKEN"),

    default_ttl=timedelta(days=1))



# 选择您喜欢的 Momento 缓存名称

cache_name = "langchain"



# 实例化 LLM 缓存

langchain.llm_cache = MomentoCache(cache_client, cache_name)

```



## 内存



Momento 可用作 LLM 的分布式内存存储。



### 聊天消息历史内存



请参阅 [此笔记本](../modules/memory/examples/momento_chat_message_history.ipynb) 了解如何将 Momento 用作聊天消息历史的内存存储。

