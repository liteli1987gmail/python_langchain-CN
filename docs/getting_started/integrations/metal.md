金属


本页面介绍如何在LangChain中使用金属](https://getmetal.io)。


什么是金属？


金属是一个专为生产环境而建立的托管检索和内存平台。您可以轻松将数据索引到`金属`中，并对其进行语义搜索和检索。


!金属](../_static/MetalDash.png)


快速入门


通过创建一个金属账户](https://app.getmetal.io/signup)来开始。


接下来，您可以轻松地利用`MetalRetriever`类来开始检索数据，进行语义搜索，提示上下文等。该类接受一个`金属`实例和一个参数字典，用于传递给金属API。


```python

from langchain.retrievers import MetalRetriever

from metal_sdk.metal import Metal





metal = Metal("API_KEY", "CLIENT_ID", "INDEX_ID");

retriever = MetalRetriever(metal, params={"limit": 2})



docs = retriever.get_relevant_documents("search term")

```

