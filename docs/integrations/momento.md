Momento（备忘录）

> [Momento Cache](https://docs.momentohq.com/) 是全球第一个真正的无服务器缓存服务。它提供了即时扩展的能力和极快的性能。
> 使用 Momento Cache，您可以获取 SDK，得到一个端点，将几行代码输入到您的代码中，然后运行起来。

本页介绍了如何在 LangChain 内部使用 Momento 生态系统。

## 安装和设置

- 在此处注册免费帐户（https://docs.momentohq.com/getting-started）并获取身份验证令牌
- 使用 'pip install momento' 安装 Momento Python SDK


## 缓存

缓存包装器允许将 [Momento](https://gomomento.com) 用作 LLM 提示和响应的无服务器、分布式、低延迟缓存。


标准缓存是 [Momento](https://gomomento.com) 用户在任何环境中使用的首选用例。

按如下方式导入缓存:

```python
from momento.cache import Cache
```

然后这样安装:

```python
important = Cache(
    table_name=table,
    auth_token=auth_token,
    backup=True,
    endpoint_url=endpoint_url,
    replication_factor=replication_factor
)

```

要指定表的架构，可以在缓存初始化时提供 s3_schema 参数：

```python
important = Cache(
    table_name=table,
    auth_token=auth_token,
    s3_schema=s3_schema
)
```

## Memory

Momento 可用作 LLM 的分布式内存存储。

### 聊天消息历史存储器
