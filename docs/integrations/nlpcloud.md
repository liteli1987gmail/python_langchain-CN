# NLPCloud


本页面介绍了如何在LangChain中使用NLPCloud生态系统。

它分为两部分：安装和设置，以及对特定NLPCloud包装器的引用。



## 安装和设置

- 使用 `pip install nlpcloud` 安装Python SDK

- 获取一个NLPCloud的API密钥，并将其设置为环境变量 (`NLPCLOUD_API_KEY`)



## 包装器



### LLM



存在一个NLPCloud LLM包装器，您可以通过以下方式访问

```python

from langchain.llms import NLPCloud

```

