# Diffbot（Diffbot）

>[Diffbot](https://docs.diffbot.com/docs) is a service to read web pages. Unlike traditional web scraping tools, （Diffbot是一项阅读网页的服务，与传统的网页抓取工具不同）
> `Diffbot` doesn't require any rules to read the content on a page.（Diffbot不需要任何规则就能读取页面上的内容。）
>It starts with computer vision, which classifies a page into one of 20 possible types. Content is then interpreted by a machine learning model trained to identify the key attributes on a page based on its type.（它从计算机视觉开始，将页面归类为可能的20种类型之一。 然后，通过训练好的机器学习模型来解释页面上的关键属性，以此来解释页面上的内容。）
>The result is a website transformed into clean-structured data (like JSON or CSV), ready for your application.（结果是将网站转换为干净结构化的数据（如JSON或CSV），可供您的应用程序使用。

## Installation and Setup（安装和设置）

Read [instructions](https://docs.diffbot.com/reference/authentication) how to get the Diffbot API Token.（阅读[说明](https://docs.diffbot.com/reference/authentication)了解如何获取Diffbot API令牌。）

## Document Loader（文档加载器）

See a [usage example](../modules/indexes/document_loaders/examples/diffbot.ipynb).（请参考[用法示例](../modules/indexes/document_loaders/examples/diffbot.ipynb)。）

```python

from langchain.document_loaders import DiffbotLoader

```

