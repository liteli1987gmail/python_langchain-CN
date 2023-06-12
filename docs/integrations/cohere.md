# Cohere（连结）


> [Cohere](https://cohere.ai/about)是一家加拿大初创公司，提供自然语言处理模型，帮助企业改善人机交互。
>


## 安装和设置
- 安装 Python SDK :
```bash
pip install cohere

```



获取[Cohere API密钥](https://dashboard.cohere.ai/)并将其设置为环境变量(`COHERE_API_KEY`)




## LLM


存在一个 Cohere LLM 包装器，你可以使用它
查看用例 [使用示例](../modules/models/llms/integrations/cohere.ipynb).


```python
from langchain.llms import Cohere

```



## 文本嵌入模型


存在一个 Cohere 嵌入模型，你可以使用它
```python
from langchain.embeddings import CohereEmbeddings

```

要了解更详细的步骤，请查看[此笔记本电脑](../modules/models/text_embedding/examples/cohere.ipynb)


## 检索器


查看用例 [使用示例](../modules/indexes/retrievers/examples/cohere-reranker.ipynb).


```python

from langchain.retrievers.document_compressors import CohereRerank

```

