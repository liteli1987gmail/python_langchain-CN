# Petals花瓣

This page covers how to use the Petals ecosystem within LangChain.本页面介绍如何在LangChain中使用Petals生态系统。
It is broken into two parts: installation and setup, and then references to specific Petals wrappers.它分为两个部分：安装和设置，然后引用特定的Petals包装器。

## Installation and Setup## 安装和设置
- Install with `pip install petals`- 使用`pip install petals`进行安装
- Get a Hugging Face api key and set it as an environment variable (`HUGGINGFACE_API_KEY`)- 获取Hugging Face api密钥并将其设置为环境变量(`HUGGINGFACE_API_KEY`)

## Wrappers## 包装器

### LLM### LLM

There exists an Petals LLM wrapper, which you can access with存在一个Petals LLM包装器，可以通过以下方式访问：
```python

from langchain.llms import Petals

```

