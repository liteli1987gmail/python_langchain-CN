＃ Jina（谷娜）

此页介绍如何在LangChain中使用Jina生态系统。
它分为两个部分：安装和设置，然后引用特定的Jina包装器。

## 安装和设置
 - 使用`pip install jina`安装Python SDK
 - 从[这里](https://cloud.jina.ai/settings/tokens)获取Jina AI Cloud授权令牌，并将其设置为环境变量（`JINA_AUTH_TOKEN`）

## 包装器

### 嵌入

存在一个Jina嵌入包装器，您可以使用它
```python
from langchain.embeddings import JinaEmbeddings

```

For a more detailed walkthrough of this, see [this notebook](../modules/models/text_embedding/examples/jina.ipynb)

