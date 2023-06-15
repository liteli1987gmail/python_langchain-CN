# Apify



本页面介绍如何在 LangChain 中使用 [Apify](https://apify.com)。



## 概述



Apify 是一个云平台，用于网页抓取和数据提取，提供了一个包含超过一千个预制应用程序（称为 *Actors*）的 [生态系统](https://apify.com/store)，可用于各种抓取、爬取和提取用例。



- `Dependents <./dependents.html>`_: 所有使用LangChain的代码仓库.



[![Apify Actors](../_static/ApifyActors.png)](https://apify.com/store)



此集成使您能够在 Apify 平台上运行 Actors，并将它们的结果加载到 LangChain 中，以从网页、博客或知识库等内容生成答案。







## 安装和设置



- 使用 `pip install apify-client` 安装 Python 的 Apify API 客户端。

- 获取您的 [Apify API token](https://console.apify.com/account/integrations) 并将其设置为环境变量 (`APIFY_API_TOKEN`)，或者在构造函数中将其传递给 `ApifyWrapper`，名称为 `apify_api_token`。





## 包装器



### 实用工具



您可以使用 `ApifyWrapper` 在 Apify 平台上运行 Actors。



`from langchain.utilities import ApifyWrapper`



```python

关于此包装器的更详细说明，请参阅 [此 notebook](../modules/agents/tools/examples/apify.ipynb)。

```







### 装载器



您还可以使用我们的 `ApifyDatasetLoader` 从 Apify 数据集中获取数据。



`from langchain.document_loaders import ApifyDatasetLoader`

```python



```

关于此加载器的更详细说明，请参阅 [此 notebook](../modules/indexes/document_loaders/examples/apify_dataset.ipynb)。

For a more detailed walkthrough of this loader, see [this notebook](../modules/indexes/document_loaders/examples/apify_dataset.ipynb).

