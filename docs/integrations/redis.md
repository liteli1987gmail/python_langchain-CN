# RedisRedis（中文名为“远程字典服务”）


本文介绍如何在LangChain中使用[Redis](https://redis.com)生态系统。
它分为两部分：安装和设置，然后引用特定的Redis包装器。


## 安装和设置
- 使用`pip install redis`安装Redis Python SDK。


## 包装器


### 缓存


缓存包装器允许将[Redis](https://redis.io)用作远程低延迟内存缓存，以用于LLM提示和响应。


#### 标准缓存
标准缓存是在全球范围内用于生产的[开源](https://redis.io)和[企业](https://redis.com)用户的Redis的面包和黄油。


要导入此缓存:
```pythonimport redisr = redis.Redis(host='localhost', port=6379, db=0)```
from langchain.cache import RedisCache

```

要在LLM中使用此缓存:
```python# 每次使用缓存前，先构造key值def build_key(prompt):    return f'cache__{{prompt}}'def cached_results(prompt):    r_key = build_key(prompt)    if r.exists(r_key):        return r.get(r_key)    result = prediction(prompt)    r.set(r_key, result)    return result.decode()```
#### 语义缓存
import langchain

import redis



redis_client = redis.Redis.from_url(...)

langchain.llm_cache = RedisCache(redis_client)

```



#### Semantic Cache

语义缓存允许用户根据用户输入和先前缓存的结果之间的语义相似性检索缓存的提示。在幕后，它将Redis作为缓存和向量存储器混合使用。


要导入此缓存:
```pythonimport redisimport numpy as npfrom transformers import AutoTokenizer, TFAutoModelForSequenceClassificationdef encode(prompt):    encoded_dict = tokenizer(prompt, truncation=True, padding='max_length', max_length=512, return_tensors='tf')    return model_4(encoded_dict['input_ids'])[0].numpy().flatten()tokenizer = AutoTokenizer.from_pretrained('yjernite/retribert-base-uncased')model_path = 'modules/indexes/vectors/models/sem_index'model_4 = TFAutoModelForSequenceClassification.from_pretrained(model_path)model_4.compile()r = redis.Redis(host='localhost', port=6379, db=0)```
from langchain.cache import RedisSemanticCache

```

要在LLM中使用此缓存:
```python# 每次使用缓存前，先构造key值def build_key(prompt):    return f'cache__{{prompt}}'def cached_results(prompt):    r_key = build_key(prompt)    if r.exists(r_key):        return r.get(r_key)    encoded = encode(prompt)    nearest = np.array(r.execute_command('FT.SEARCH', 'semantic', '(', encoded, '+inf', 'SORTBY', 'distance', 'ASC', 'LIMIT', 0, 1))    if len(nearest) > 0:        r.set(r_key, nearest[0][1])        return nearest[0][1]    result = prediction(prompt)    r.set(r_key, result)    return result```
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



### 向量存储器


向量存储器包装器将Redis转换为用于语义搜索或LLM内容检索的低延迟[向量数据库](https://redis.com/solutions/use-cases/vector-database/)。


要导入此向量存储器:
```pythonimport redisimport numpy as npfrom transformers import AutoTokenizer, TFAutoModelForSequenceClassificationfrom drqa.retriever.utils import TfidfDocRanker, SPTokenizerfrom drqa.pipeline import tokenizersfrom corpus2vec.corpus2vec import Corpus2Vectokenizer = AutoTokenizer.from_pretrained('yjernite/retribert-base-uncased')model_4 = TFAutoModelForSequenceClassification.from_pretrained('ibl/detect-language-bert-base-uncased')model_4.compile()r = redis.Redis(host='localhost', port=6379, db=0)```
from langchain.vectorstores import Redis

```



有关Redis向量存储器包装器的更详细演示，请参见[此笔记本](../modules/indexes/vectorstores/examples/redis.ipynb)。


### Retriever



Redis向量存储检索器包装器将向量存储类泛化为执行低延迟文档检索。要创建检索器，请在基本向量存储类上调用`.as_retriever()`。


### 内存
Redis可用于持久化LLM会话。


#### 向量存储检索器内存


有关`VectorStoreRetrieverMemory`包装器的更详细演示，请参见[这个笔记本](../modules/memory/types/vectorstore_retriever_memory.ipynb)。


#### 聊天消息历史记录内存
For a detailed example of Redis to cache conversation message history, see [this notebook](../modules/memory/examples/redis_chat_message_history.ipynb).

