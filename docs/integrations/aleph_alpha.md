# Aleph Alpha 安福阿尔法



> [Aleph Alpha](https://docs.aleph-alpha.com/)成立于2019年，旨在研究和构建强化人工智能时代的基础技术。这个由国际科学家、工程师和创新者组成的团队进行深度研究、开发和部署具有变革性的人工智能技术，如大型语言模型和多模态模型，并运行最快的欧洲商业人工智能集群。



> [Luminous系列](https://docs.aleph-alpha.com/docs/introduction/luminous/)是一系列大型语言模型。



## 安装和设置



```bash

pip install aleph-alpha-client

```



您需要创建一个新的令牌。请参阅[说明](https://docs.aleph-alpha.com/docs/account/#create-a-new-token)。



```python

from getpass import getpass



ALEPH_ALPHA_API_KEY = getpass()

```





## LLM



查看[用法示例](../modules/models/llms/integrations/aleph_alpha.ipynb)。



```python

from langchain.llms import AlephAlpha

```



## 文本嵌入模型



查看[用法示例](../modules/models/text_embedding/examples/aleph_alpha.ipynb)。



```python

from langchain.embeddings import AlephAlphaSymmetricSemanticEmbedding, AlephAlphaAsymmetricSemanticEmbedding

```

