Redis简介


本页面介绍如何在LangChain中使用Redis生态系统。
分为两部分：安装和设置，以及特定的Redis包装器的参考。


安装和设置
使用`pip install redis`安装Redis Python SDK。


包装器


缓存


缓存包装器允许将Redis用作远程、低延迟、内存中的LLM提示和响应缓存。


标准缓存
标准缓存是Redis在生产中既用于开源用户又用于企业用户的核心用例。


导入此缓存:
```python

from langchain.cache import RedisCache

```



将此缓存用于您的LLM:
```python

import langchain

import redis



redis_client = redis.Redis.from_url(...)

langchain.llm_cache = RedisCache(redis_client)

```



语义缓存
语义缓存允许用户根据用户输入和先前缓存结果之间的语义相似性检索缓存的提示。在底层，它将Redis同时作为缓存和向量存储进行混合。


导入此缓存:
```python

from langchain.cache import RedisSemanticCache

```



将此缓存用于您的LLM:
```python

import langchain

import redis



# use any embedding provider...

from tests.integration_tests.vectorstores.fake_embeddings import FakeEmbeddings



redis_url = "redis://localhost:6379"



langchain.llm_cache = RedisSemanticCache(

    embedding=FakeEmbeddings(),

    redis_url=redis_url

)

```



向量存储


向量存储包装器将Redis转化为用于语义搜索或LLM内容检索的低延迟向量数据库。


导入此向量存储:
```python

from langchain.vectorstores import Redis

```



有关Redis向量存储包装器的更详细演示，请参阅此笔记本。


检索器


Redis向量存储检索器包装器将向量存储类概括为执行低延迟文档检索的类。要创建检索器，只需在基本向量存储类上调用`.as_retriever()`。


内存
Redis可用于持久化LLM对话。


向量存储检索器内存


有关`VectorStoreRetrieverMemory`包装器的更详细演示，请参阅此笔记本。


聊天消息历史内存
有关使用Redis缓存对话消息历史的详细示例，请参阅此笔记本。
