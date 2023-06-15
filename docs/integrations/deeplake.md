# 深湖

本页面介绍如何在LangChain中使用深湖生态系统。



## 为什么选择深湖？

- 不仅是一个（多模态）向量存储库。您还可以使用数据集来对自己的LLM模型进行微调。

- 不仅存储嵌入向量，还自动进行版本控制的原始数据。

- 完全无服务器。不需要其他服务，并可与主要云提供商（AWS S3，GCS等）一起使用。



## 更多资源

1. [LangChain和深湖终极指南：构建用于回答您的金融数据问题的ChatGPT](https://www.activeloop.ai/resources/ultimate-guide-to-lang-chain-deep-lake-build-chat-gpt-to-answer-questions-on-your-financial-data/)

2. [使用深湖进行Twitter算法代码基础分析](../use_cases/code/twitter-the-algorithm-analysis-deeplake.ipynb)

3. 这是[白皮书](https://www.deeplake.ai/whitepaper)和[学术论文](https://arxiv.org/pdf/2209.10785.pdf)的链接，介绍了深湖。

4. 这是一组可供查阅的附加资源：[Deep Lake](https://github.com/activeloopai/deeplake)，[入门指南](https://docs.activeloop.ai/getting-started)和[Tutorials](https://docs.activeloop.ai/hub-tutorials)



## 安装和设置

- 使用 `pip install deeplake` 命令安装Python包



## Wrappers



### VectorStore



存在一个关于深湖的包装器，它是一个用于深度学习应用程序的数据湖，可以将其用作向量存储库（目前仅限语义搜索或示例选择）。



导入此向量存储库的方法如下:

```python

from langchain.vectorstores import DeepLake

```





有关深湖包装器的更详细步骤，请参阅[此笔记本](../modules/indexes/vectorstores/examples/deeplake.ipynb)

