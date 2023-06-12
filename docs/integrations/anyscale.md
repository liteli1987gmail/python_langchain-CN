# Anyscale安速苑

This page covers how to use the Anyscale ecosystem within LangChain.此页面介绍了如何在LangChain中使用Anyscale生态系统。
It is broken into two parts: installation and setup, and then references to specific Anyscale wrappers.它分为两个部分：安装和设置，然后引用特定的Anyscale wrappers。

## Installation and Setup安装和设置
- Get an Anyscale Service URL, route and API key and set them as environment variables (`ANYSCALE_SERVICE_URL`,`ANYSCALE_SERVICE_ROUTE`, `ANYSCALE_SERVICE_TOKEN`). - 获取Anyscale Service URL和路由和API密钥，并将它们设置为环境变量(`ANYSCALE_SERVICE_URL`，`ANYSCALE_SERVICE_ROUTE`，`ANYSCALE_SERVICE_TOKEN`)。
- Please see [the Anyscale docs](https://docs.anyscale.com/productionize/services-v2/get-started) for more details.- 更多详情请参阅[Anyscale文档](https://docs.anyscale.com/productionize/services-v2/get-started)。

## Wrappers包装器

### LLMLLM

There exists an Anyscale LLM wrapper, which you can access with 存在一个Anyscale LLM wrapper，您可以使用以下方式访问它
```python

from langchain.llms import Anyscale

```

