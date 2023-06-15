# Jina



这个页面介绍了如何在LangChain中使用Jina生态系统。

它分为两部分：安装和设置，以及对特定Jina包装器的引用。



## 安装和设置

- 使用 `pip install jina` 安装Python SDK

- 从[这里](https://cloud.jina.ai/settings/tokens)获取Jina AI Cloud授权令牌，并将其设置为环境变量（`JINA_AUTH_TOKEN`）



## 包装器



### 嵌入



存在一个Jina嵌入包装器，您可以通过以下方式访问

```python

from langchain.embeddings import JinaEmbeddings

```

有关更详细的步骤，请参见[此笔记本](../modules/models/text_embedding/examples/jina.ipynb)

