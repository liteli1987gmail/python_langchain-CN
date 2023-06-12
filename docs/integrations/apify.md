# Apify（Apify）

本页面介绍如何在LangChain中使用[Apify]（https://apify.com）。

## 概述

Apify是用于网络爬取和数据提取的云平台，提供了一千多个预制的应用程序（称为*Actors*）用于各种爬取、爬行和提取用例。
这些应用程序构成了一个[生态系统]（https://apify.com/store）。
 
[![Apify Actors]（../_static/ApifyActors.png）]（https://apify.com/store）

此集成使您能够在Apify平台上运行Actors，并将其结果加载到LangChain中，以从网站、文档、博客或知识库中获取文档和数据，并生成答案。


## 安装和设置

- 使用'pip install apify-client'安装Python的Apify API客户端
- 获取您的[Apify API令牌]（https://console.apify.com/account/integrations），并将其设置为


## 封套

### 实用工具

您可以使用'ApifyWrapper'在Apify平台上运行Actors。

```python

有关此封套的更详细说明，请参见[此笔记本电脑]（../modules/agents/tools/examples/apify.ipynb）。


### 加载器

您还可以使用我们的'ApifyDatasetLoader'从Apify数据集中获取数据。

```python

### Loader



You can also use our `ApifyDatasetLoader` to get data from Apify dataset.



```python

from langchain.document_loaders import ApifyDatasetLoader

```



For a more detailed walkthrough of this loader, see [this notebook](../modules/indexes/document_loaders/examples/apify_dataset.ipynb).

