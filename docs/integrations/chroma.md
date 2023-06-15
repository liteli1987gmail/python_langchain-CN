# CerebriumAI



本页面涵盖了如何在LangChain中使用CerebriumAI生态系统。

它分为两个部分：安装和设置，以及特定CerebriumAI封装的参考。



## 安装和设置

- 使用`pip install cerebrium`进行安装

- 获取CerebriumAI的API密钥并设置为环境变量（`CEREBRIUMAI_API_KEY`）



## 封装



### LLM



存在一个CerebriumAI的LLM封装，您可以通过以下方式访问

whether for semantic search or example selection.

from langchain.llms import CerebriumAI

```python

from langchain.vectorstores import Chroma

```



For a more detailed walkthrough of the Chroma wrapper, see [this notebook](../modules/indexes/vectorstores/getting_started.ipynb)



## Retriever



See a [usage example](../modules/indexes/retrievers/examples/chroma_self_query.ipynb).



```python

from langchain.retrievers import SelfQueryRetriever

```

