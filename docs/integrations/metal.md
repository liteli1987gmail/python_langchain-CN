# 金属



本页面介绍如何在LangChain中使用[金属](https://getmetal.io)。



## 什么是金属？



金属是一个专为生产环境而建的受控检索和内存平台。您可以轻松将数据索引到`Metal`中，并对其进行语义搜索和检索。



![Metal](../_static/MetalDash.png)



## 快速入门



首先，通过[创建一个Metal账号](https://app.getmetal.io/signup)来开始。



然后，您可以轻松地利用`MetalRetriever`类来开始检索语义搜索、提示上下文等数据。该类接受一个`Metal`实例和一个参数字典，将其传递给Metal API。



```python

from langchain.retrievers import MetalRetriever

from metal_sdk.metal import Metal





metal = Metal("API_KEY", "CLIENT_ID", "INDEX_ID");

retriever = MetalRetriever(metal, params={"limit": 2})



docs = retriever.get_relevant_documents("搜索词")

```

