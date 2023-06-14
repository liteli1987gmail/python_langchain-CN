# NLPCloud



本页面介绍如何在LangChain中使用NLPCloud生态系统。

它分为两个部分：安装和设置，然后参考特定的NLPCloud封装。



## 安装和设置

- 使用`pip install nlpcloud`命令安装Python SDK

- 获取一个NLPCloud API密钥，并将其设置为环境变量（`NLPCLOUD_API_KEY`）



## 封装器



### LLM



存在一个NLPCloud LLM封装器，可以通过以下方式访问

```python

from langchain.llms import NLPCloud

```

