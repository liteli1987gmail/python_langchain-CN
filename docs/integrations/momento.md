Momento


Momento缓存] 是世界上第一个真正无服务器的缓存服务。它提供即时弹性、可缩放到零
能力和极快的性能。
使用Momento缓存，您可以获取SDK，获取一个终点，将几行代码输入到您的代码中，然后您就可以运行了。


本页面介绍如何在LangChain中使用Momento生态系统]。


安装和设置


- 在此处]注册免费帐户，并获取认证令牌
- 使用`pip install momento`安装Momento Python SDK




缓存


缓存包装器允许Momento]用作无服务器、分布式、低延迟的LLM提示和响应缓存。




标准缓存是Momento]用户在任何环境中使用的首选用例。


导入缓存的方法如下


```python

from langchain.cache import MomentoCache

```



并进行如下设置


```python

from datetime import timedelta

from momento import CacheClient, Configurations, CredentialProvider

import langchain



# Instantiate the Momento client

cache_client = CacheClient(

    Configurations.Laptop.v1(),

    CredentialProvider.from_environment_variable("MOMENTO_AUTH_TOKEN"),

    default_ttl=timedelta(days=1))



# Choose a Momento cache name of your choice

cache_name = "langchain"



# Instantiate the LLM cache

langchain.llm_cache = MomentoCache(cache_client, cache_name)

```



内存


Momento可用作LLM的分布式内存存储。


聊天消息历史内存


查看此笔记本]，了解如何将Momento用作聊天消息历史的内存存储。
