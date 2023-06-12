# NLPCloud（NLPCloud）


This page covers how to use the NLPCloud ecosystem within LangChain.（此页面介绍如何在LangChain中使用NLPCloud生态系统。）
It is broken into two parts: installation and setup, and then references to specific NLPCloud wrappers.（它分为两部分：安装和设置，然后引用特定的NLPCloud包装器。）


## Installation and Setup（## 安装和设置）
- Install the Python SDK with `pip install nlpcloud`（- 使用`pip install nlpcloud`安装Python SDK）
- Get an NLPCloud api key and set it as an environment variable (`NLPCLOUD_API_KEY`)（- 获取NLPCloud api密钥并将其设置为环境变量（`NLPCLOUD_API_KEY`））


## Wrappers（## 包装器）


### LLM（### LLM）


There exists an NLPCloud LLM wrapper, which you can access with （存在一个NLPCloud LLM包装器，您可以通过以下方式访问）
```python

from langchain.llms import NLPCloud

```

