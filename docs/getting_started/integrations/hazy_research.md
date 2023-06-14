模糊研究



本页面介绍如何在LangChain中使用模糊研究生态系统。

它分为两个部分：安装和设置，以及对特定模糊研究封装的参考。



安装和设置

- 要使用`manifest`，请使用`pip install manifest-ml`进行安装



封装



LLM



Hazy Research的`manifest`库存在一个LLM封装。

`manifest`是一个Python库，它本身是对许多模型提供商的封装，并添加了缓存、历史记录等功能。



要使用此封装：

```python

from langchain.llms.manifest import ManifestWrapper

```

