# scikit-learn
独钢学



This page covers how to use the scikit-learn package within LangChain.
此页面介绍了如何在LangChain中使用scikit-learn包。

It is broken into two parts: installation and setup, and then references to specific scikit-learn wrappers.
它分为两个部分：安装和设置，然后引用特定的scikit-learn包装器。



## Installation and Setup
安装和设置



- Install the Python package with `pip install scikit-learn`
使用`pip install scikit-learn`安装Python包



## Wrappers
包装器



### VectorStore
向量存储



`SKLearnVectorStore` provides a simple wrapper around the nearest neighbor implementation in the
`SKLearnVectorStore`提供了一个简单的包装器，将最近邻算法实现在

scikit-learn package, allowing you to use it as a vectorstore.
scikit-learn包中，允许您将其作为向量存储使用。



To import this vectorstore:
导入此向量存储：



```python

from langchain.vectorstores import SKLearnVectorStore

```



For a more detailed walkthrough of the SKLearnVectorStore wrapper, see [this notebook](../modules/indexes/vectorstores/examples/sklearn.ipynb).
有关SKLearnVectorStore包装器的更详细演示，请参阅[此笔记本](../modules/indexes/vectorstores/examples/sklearn.ipynb)。

