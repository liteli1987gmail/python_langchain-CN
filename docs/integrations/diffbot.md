Diffbot

>Diffbot](https://docs.diffbot.com/docs) 是一个用于阅读网页的服务。与传统的网页抓取工具不同，
> `Diffbot` 不需要任何规则来阅读页面上的内容。
> 它从计算机视觉开始，将页面分类为20种可能的类型之一。然后，根据页面的类型，机器学习模型解释内容并识别关键属性。
> 结果是将网站转换为结构清晰的数据（如JSON或CSV），可以供您的应用程序使用。

安装和设置

阅读 说明](https://docs.diffbot.com/reference/authentication) 了解如何获取 Diffbot API 令牌。

文档加载器

查看一个 使用示例](../modules/indexes/document_loaders/examples/diffbot.ipynb)。

```python

from langchain.document_loaders import DiffbotLoader

```

