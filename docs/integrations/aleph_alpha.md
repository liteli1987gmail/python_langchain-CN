# 爱利夫·阿尔法（Aleph Alpha）



> Aleph Alpha](https://docs.aleph-alpha.com/)成立于2019年，致力于研究和构建强人工智能时代的基础技术。这个由国际科学家、工程师和创新者组成的团队研究、开发和部署变革性人工智能，如大型语言和多模态模型，并运行着欧洲最快速的商业人工智能集群。



> Luminous 系列](https://docs.aleph-alpha.com/docs/introduction/luminous/)是一系列大型语言模型。



## 安装和设置



```bash

使用以下命令安装爱利夫·阿尔法客户端：pip install aleph-alpha-client

```



您必须创建一个新令牌。请参阅说明](https://docs.aleph-alpha.com/docs/account/#create-a-new-token)。



```python

from getpass import getpass



ALEPH_ALPHA_API_KEY = getpass()

```





## LLM



请查看使用示例](../modules/models/llms/integrations/aleph_alpha.ipynb)。



```python

from langchain.llms import AlephAlpha

```



## 文本嵌入模型



请查看使用示例](../modules/models/text_embedding/examples/aleph_alpha.ipynb)。



```python

from langchain.embeddings import AlephAlphaSymmetricSemanticEmbedding, AlephAlphaAsymmetricSemanticEmbedding

```

