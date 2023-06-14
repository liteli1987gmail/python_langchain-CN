Cohere



Cohere是一家加拿大初创公司，提供自然语言处理模型

，帮助企业改善人机交互。



安装和设置

- 安装Python SDK:

```bash

pip install cohere

```



获取Cohere api key](https://dashboard.cohere.ai/)并将其设置为环境变量（`COHERE_API_KEY`）





LLM



存在Cohere LLM包装器，可以通过以下方式访问

查看用法示例](../modules/models/llms/integrations/cohere.ipynb)。



```python

from langchain.llms import Cohere

```



文本嵌入模型



存在Cohere嵌入模型，可以通过以下方式访问

```python

from langchain.embeddings import CohereEmbeddings

```

有关详细步骤，请参阅此笔记本](../modules/models/text_embedding/examples/cohere.ipynb)



检索器



查看用法示例](../modules/indexes/retrievers/examples/cohere-reranker.ipynb)。



```python

from langchain.retrievers.document_compressors import CohereRerank

```

