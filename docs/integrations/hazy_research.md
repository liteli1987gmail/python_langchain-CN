# Hazy Research（模糊研究）


This page covers how to use the Hazy Research ecosystem within LangChain.（本页面介绍如何在LangChain中使用Hazy Research生态系统。）
It is broken into two parts: installation and setup, and then references to specific Hazy Research wrappers.（它分为两部分：安装和设置，然后引用特定的Hazy Research包装器。）


## Installation and Setup（## 安装和设置）
- To use the `manifest`, install it with `pip install manifest-ml`（- 要使用`manifest`，请使用`pip install manifest-ml`进行安装）


## Wrappers（## 包装器）


### LLM（### LLM）


There exists an LLM wrapper around Hazy Research's `manifest` library. （存在一个LLM包装器封装了Hazy Research的`manifest`库。）
`manifest` is a python library which is itself a wrapper around many model providers, and adds in caching, history, and more.（`manifest`是一个Python库，它本身是许多模型提供商的包装器，还添加了缓存，历史记录等功能。）


To use this wrapper:（要使用这个包装器:）
```python

from langchain.llms.manifest import ManifestWrapper

```

