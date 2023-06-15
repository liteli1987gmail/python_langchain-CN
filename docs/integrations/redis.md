# Redis



本页面介绍如何在LangChain中使用[Redis](https://redis.com)生态系统。

它分为两个部分：安装和设置，然后引用特定的Redis包装器。



## 安装和设置

- 使用`pip install redis`安装Redis Python SDK



## 包装器



### 缓存



缓存包装器允许将[Redis](https://redis.io)用作远程、低延迟、内存中的LLM提示和响应缓存。



#### 标准缓存

标准缓存是Redis在生产中用于[开源](https://redis.io)和[企业](https://redis.com)用户的基本用例。



要导入此缓存:

```python

from langchain.cache import RedisCache

```



要将此缓存用于您的LLM:

```python

import langchain

import redis



redis_client = redis.Redis.from_url(...)

langchain.llm_cache = RedisCache(redis_client)

```



#### 语义缓存

语义缓存允许用户根据用户输入和先前缓存结果之间的语义相似性检索缓存的提示。在内部，它将Redis作为缓存和向量存储同时使用。



要导入此缓存:

```python

from langchain.cache import RedisSemanticCache

```



要将此缓存用于您的LLM:

```python

import langchain

import redis



# 使用任何嵌入提供者...

from tests.integration_tests.vectorstores.fake_embeddings import FakeEmbeddings



redis_url = "redis://localhost:6379"



langchain.llm_cache = RedisSemanticCache(

    embedding=FakeEmbeddings(),

    redis_url=redis_url

)

```



### 向量存储



向量存储包装器将Redis转换为用于语义搜索或LLM内容检索的低延迟[向量数据库](https://redis.com/solutions/use-cases/vector-database/)。



要导入此向量存储:

```python

from langchain.vectorstores import Redis

```



有关Redis向量存储包装器的更详细说明，请参见[此笔记本](../modules/indexes/vectorstores/examples/redis.ipynb)。



### 检索器



Redis向量存储的检索器包装器将向量存储类泛化为执行低延迟文档检索的类。只需在基本的向量存储类上调用`.as_retriever()`即可创建检索器。



### 存储

Redis可以用于持久化LLM对话。



#### 向量存储检索器存储



有关`VectorStoreRetrieverMemory`包装器的更详细说明，请参见[此笔记本](../modules/memory/types/vectorstore_retriever_memory.ipynb)。



#### 聊天消息历史记录存储

有关使用Redis进行缓存对话消息历史记录的详细示例，请参见[此笔记本](../modules/memory/examples/redis_chat_message_history.ipynb)。

