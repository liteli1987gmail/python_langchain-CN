# Diffbot 安装和设置


>[Diffbot](https://docs.diffbot.com/docs) 是一个用于读取网页的服务。与传统的网络爬虫工具不同，
> `Diffbot` 无需任何规则即可读取页面上的内容。

>它首先使用计算机视觉将页面分类为20种可能的类型之一。然后，基于页面类型，机器学习模型对内容进行解析，以识别关键属性。

>结果是将网站转化为干净结构化的数据（如JSON或CSV），可供您的应用程序使用。



## 安装和设置 安装和设置



阅读 [说明](https://docs.diffbot.com/reference/authentication) 如何获取Diffbot API令牌。



文档加载器 文档加载器



查看 [使用示例](../modules/indexes/document_loaders/examples/diffbot.ipynb)。



```python

from langchain.document_loaders import DiffbotLoader

```

