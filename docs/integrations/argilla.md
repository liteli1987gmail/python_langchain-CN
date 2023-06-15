# Argilla 粘土


![Argilla - LLMs的开源数据平台](https://argilla.io/og.png)



>[Argilla](https://argilla.io/)是一个用于LLMs的开源数据整理平台。

> 通过使用Argilla，每个人都可以通过更快的数据整理构建强大的语言模型

> 使用人工和机器反馈来支持MLOps周期中的每个步骤

> 从数据标记到模型监控。



## 安装和设置



首先，您需要按照以下步骤安装`argilla` Python包:



```bash

pip install argilla --upgrade

```



如果您已经运行了Argilla服务器，则可以开始使用；但如果您

没有，请按照下面的步骤安装它。



如果您没有，可以参考[Argilla - 🚀快速入门](https://docs.argilla.io/en/latest/getting_started/quickstart.html#Running-Argilla-Quickstart) 在HuggingFace Spaces、本地或服务器上部署Argilla。



## 追踪



请参阅[ArgillaCallbackHandler的使用示例](../modules/callbacks/examples/examples/argilla.ipynb)。



```python

from langchain.callbacks import ArgillaCallbackHandler

```

