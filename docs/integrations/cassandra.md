# Cassandra 坎塞拉数据库


>[Cassandra](https://en.wikipedia.org/wiki/Apache_Cassandra)是一个免费且开源的分布式、宽列存储、NoSQL数据库管理系统，旨在处理大量数据并跨多台服务器进行存储，
>提供高可用性且无单点故障。`Cassandra`支持跨多个数据中心的集群，通过异步无主复制实现对所有客户端的低延迟操作。
>`Cassandra`的设计是结合了`Amazon's Dynamo`分布式存储和复制技术以及`Google's Bigtable`数据和存储引擎模型。



## 安装和设置



pip install cassandra-driver





## 内存



查看一个[使用示例](../modules/memory/examples/cassandra_chat_message_history.ipynb)。



from langchain.memory import CassandraChatMessageHistory

## Memory



See a [usage example](../modules/memory/examples/cassandra_chat_message_history.ipynb).



```python

from langchain.memory import CassandraChatMessageHistory

```

