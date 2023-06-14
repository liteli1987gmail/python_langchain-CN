Jina


这个页面介绍了在LangChain中如何使用Jina生态系统。
它分为两个部分：安装和设置，然后引用特定的Jina包装器。


安装和设置
使用 `pip install jina` 安装Python SDK
从这里](https://cloud.jina.ai/settings/tokens)获取Jina AI Cloud的身份验证令牌，并将其设置为环境变量（`JINA_AUTH_TOKEN`）


包装器


嵌入


存在一个Jina嵌入包装器，您可以通过以下方式访问
```python

from langchain.embeddings import JinaEmbeddings

```

有关更详细的步骤，请参见此笔记本](../modules/models/text_embedding/examples/jina.ipynb)
