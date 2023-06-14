Argilla
说明


!Argilla - LLM的开源数据平台](https://argilla.io/og.png)



>Argilla](https://argilla.io/) 是一个面向LLM的开源数据整理平台。

>使用Argilla，每个人都能通过更快的数据整理来构建健壮的语言模型
备注：Using Argilla, everyone can build robust language models through faster data curation 
>使用人工和机器反馈，在MLOps周期的每个步骤都提供支持
备注：We provide support for each step in the MLOps cycle
>从数据标注到模型监控。
备注：from data labeling to model monitoring.


安装和设置



首先，您需要按照以下方式安装 `argilla` Python包:



```bash

pip install argilla --upgrade

```



如果您已经运行了一个Argilla服务器，那么您可以直接开始使用；但如果没有

您可以按照下面的步骤安装它。



如果没有，您可以参考【Argilla -🚀快速入门】(https://docs.argilla.io/en/latest/getting_started/quickstart.html#Running-Argilla-Quickstart) 在HuggingFace Spaces、本地或服务器上部署Argilla。



跟踪



查看 `ArgillaCallbackHandler`](../modules/callbacks/examples/examples/argilla.ipynb) 的使用示例。



```python

from langchain.callbacks import ArgillaCallbackHandler

```

