## Metal


本页面介绍在LangChain中如何使用[Metal](https://getmetal.io)。


## 什么是Metal？


Metal是一个用于生产的托管检索和内存平台。将您的数据轻松索引到`Metal`中并在其中进行语义搜索和检索。


![Metal](../_static/MetalDash.png)



## 快速入门


通过[创建Metal帐户](https://app.getmetal.io/signup)开始入门。


Then, you can easily take advantage of the `MetalRetriever` class to start retrieving your data for semantic search, prompting context, etc. This class takes a `Metal` instance and a dictionary of parameters to pass to the Metal API.



```python

from langchain.retrievers import MetalRetriever

from metal_sdk.metal import Metal





metal = Metal("API_KEY", "CLIENT_ID", "INDEX_ID");

retriever = MetalRetriever(metal, params={"limit": 2})



docs = retriever.get_relevant_documents("search term")

```

