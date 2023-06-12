# Tair（Tair）


This page covers how to use the Tair ecosystem within LangChain.（本页面介绍如何在LangChain内使用Tair生态系统。）


## Installation and Setup（安装和设置）


Install Tair Python SDK with `pip install tair`.（使用 `pip install tair` 安装Tair Python SDK。）


## Wrappers（封装器）


### VectorStore（矢量存储器）


There exists a wrapper around TairVector allowing you to use it as a vectorstore whether for semantic search or example selection.（TairVector周围存在一个封装器，使您可以将其用作矢量存储器，无论是用于语义搜索还是示例选择。）
whether for semantic search or example selection.（无论是用于语义搜索还是示例选择。）


To import this vectorstore:（要导入此矢量存储器:）


```python（```python）
from langchain.vectorstores import Tair

```



For a more detailed walkthrough of the Tair wrapper, see [this notebook](../modules/indexes/vectorstores/examples/tair.ipynb)

