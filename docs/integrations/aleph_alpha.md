# Aleph Alpha（阿列夫·阿尔法）


>[Aleph Alpha](https://docs.aleph-alpha.com/)是一家成立于2019年的公司，旨在研究和构建强人工智能时代的基础技术。团队由国际科学家、工程师和创新者组成，研究、开发和部署像大型语言和多模态模型这样的变革性AI，并运行最快的欧洲商业AI集群。


>[Luminous系列](https://docs.aleph-alpha.com/docs/introduction/luminous/)是一系列大型语言模型。


## 安装和设置


```bash

pip install aleph-alpha-client

```



您必须创建一个新的令牌。请查看[说明](https://docs.aleph-alpha.com/docs/account/#create-a-new-token)。


```python

from getpass import getpass



ALEPH_ALPHA_API_KEY = getpass()

```





## LLM


请参阅[使用示例](../modules/models/llms/integrations/aleph_alpha.ipynb)。


```python

from langchain.llms import AlephAlpha

```



## 文本嵌入模型


See a [usage example](../modules/models/text_embedding/examples/aleph_alpha.ipynb).



```python

from langchain.embeddings import AlephAlphaSymmetricSemanticEmbedding, AlephAlphaAsymmetricSemanticEmbedding

```

