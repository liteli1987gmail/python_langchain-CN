# Anyscale


本页面介绍如何在LangChain中使用Anyscale生态系统。

它分为两个部分：安装和设置，然后是具体Anyscale包装器的参考。


## 安装和设置

-获取Anyscale服务URL，路由和API密钥，并将它们设置为环境变量（ANYSCALE_SERVICE_URL，ANYSCALE_SERVICE_ROUTE，ANYSCALE_SERVICE_TOKEN）。

-有关更多详细信息，请参阅[Anyscale文档]（https://docs.anyscale.com/productionize/services-v2/get-started）。



## 包装器



### LLM



存在一个Anyscale LLM包装器，您可以使用以下代码访问

```python

from langchain.llms import Anyscale

```

