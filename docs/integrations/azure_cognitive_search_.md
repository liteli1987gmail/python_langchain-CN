# Azure认知搜索



>Azure认知搜索](https://learn.microsoft.com/zh-cn/azure/search/search-what-is-azure-search)（曾被称为`Azure Search`）是一种云搜索服务，为开发人员提供基础设施、API和工具，用于构建丰富的搜索体验，包括对Web、移动和企业应用中的私有异构内容进行搜索。



>搜索是向用户呈现文本的任何应用程序的基础，常见场景包括目录或文档搜索、在线零售应用或对专有内容进行数据探索。创建搜索服务时，您将使用以下功能：

>- 全文搜索引擎，用于对包含用户拥有的内容的搜索索引进行全文搜索

>- 丰富的索引，包括词法分析和可选的AI增强，用于内容提取和转换

>- 用于文本搜索、模糊搜索、自动完成、地理搜索等的丰富查询语法

>- 通过Azure SDK中的REST API和客户端库进行编程

>- 数据层、机器学习层和AI（认知服务）中的Azure集成





## 安装和设置



参见设置说明](https://learn.microsoft.com/zh-cn/azure/search/search-create-service-portal)。





## 检索器



参见使用示例](../modules/indexes/retrievers/examples/azure_cognitive_search.ipynb)。



```python

from langchain.retrievers import AzureCognitiveSearchRetriever

```

