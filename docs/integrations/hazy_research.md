# Hazy Research模糊研究



本页面介绍如何在LangChain中使用Hazy Research生态系统。

它分为两个部分：安装和设置，以及特定Hazy Research封装的参考。



## 安装和设置

- 要使用`manifest`，请使用`pip install manifest-ml`进行安装



## 封装器



### LLM



Hazy Research的`manifest`库周围存在一个LLM封装器。

`manifest`是一个Python库，它本身是许多模型提供商的封装器，并添加了缓存、历史记录等功能。



要使用此封装器：

```python

from langchain.llms.manifest import ManifestWrapper

```

