# Argilla（选用注释）


![Argilla - LLMs的开源数据平台](https://argilla.io/og.png)


> [Argilla](https://argilla.io/)是一款开源的数据筛选平台，专为LLMs而设计。
> 使用Argilla，每个人都可以通过更快的数据筛选构建坚固的语言模型，同时利用人工和机器反馈。我们为MLOps周期的每个步骤提供支持，从数据标记到模型监控。
> using both human and machine feedback. We provide support for each step in the MLOps cycle, 

> from data labeling to model monitoring.



## 安装和设置


首先，您需要按如下方式安装`argilla` Python软件包


```bash
pip install argilla --upgrade

```



如果您已经运行了Argilla服务器，那么您可以开始了；但是如果没有，请按照接下来的步骤安装它。
you don't, follow the next steps to install it.



如果没有，请参阅[Argilla-🚀快速入门](https://docs.argilla.io/en/latest/getting_started/quickstart.html#Running-Argilla-Quickstart)在HuggingFace Spaces、本地或服务器上部署Argilla。


## 追踪


请参阅[`ArgillaCallbackHandler`的用法示例](../modules/callbacks/examples/examples/argilla.ipynb)。


```python

from langchain.callbacks import ArgillaCallbackHandler

```

