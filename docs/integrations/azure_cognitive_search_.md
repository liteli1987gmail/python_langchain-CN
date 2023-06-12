# Azure Cognitive Search

>[Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search)（之前称为`Azure Search`）是一项云搜索服务，能够为开发人员提供基础架构、API和工具，以在 Web、移动和企业应用中构建丰富的搜索体验，涵盖私有的异构内容。

>搜索是向用户展示文本的任何应用程序的基础，常见的场景包括目录或文档搜索、在线零售应用程序或对专有内容进行数据探索。当创建搜索服务时，您将使用以下功能：
>- 用于全文搜索的搜索引擎，用于搜索包含用户拥有的内容的搜索索引
>- 丰富的索引，包括词汇分析和可选择的 AI 丰富内容提取和转换
>- 用于文本搜索、模糊搜索、自动完成、地理搜索等的丰富查询语法
>- 通过 REST API 和 Azure SDK 中的客户端库实现可编程性
>- 数据层、机器学习层和 AI（认知服务）的 Azure 集成


## 安装和设置

请参阅[设置说明](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal)。


## 检索器

请参阅[使用示例](../modules/indexes/retrievers/examples/azure_cognitive_search.ipynb)。

```python

from langchain.retrievers import AzureCognitiveSearchRetriever

```

