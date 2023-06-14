深湖

本页介绍如何在LangChain中使用深湖生态系统。



为什么选择深湖？

- 不仅仅是一个（多模态）向量存储。您还可以使用数据集来微调自己的LLM模型。

- 不仅存储嵌入向量，还具有自动版本控制的原始数据。

- 真正无服务器。不需要另一个服务，可以与主要的云提供商（AWS S3、GCS等）一起使用。



更多资源

1. LangChain和深湖终极指南：构建ChatGPT以回答有关您的金融数据的问题](https://www.activeloop.ai/resources/ultimate-guide-to-lang-chain-deep-lake-build-chat-gpt-to-answer-questions-on-your-financial-data/)

2. 使用Deep Lake进行Twitter算法代码分析](../use_cases/code/twitter-the-algorithm-analysis-deeplake.ipynb)

3. 这里是白皮书](https://www.deeplake.ai/whitepaper)和学术论文](https://arxiv.org/pdf/2209.10785.pdf)关于深湖

4. 以下是一套额外的资源可供查阅：Deep Lake](https://github.com/activeloopai/deeplake)，入门指南](https://docs.activeloop.ai/getting-started)和Tutorials](https://docs.activeloop.ai/hub-tutorials)



安装和设置

- 使用`pip install deeplake`安装Python包



包装器



向量存储



存在一个围绕Deep Lake的包装器，用于深度学习应用的数据湖，您可以将其用作向量存储（目前），无论是用于语义搜索还是示例选择。



要导入此向量存储：

```python

from langchain.vectorstores import DeepLake

```





有关深湖包装器的更详细演示，请参阅此笔记本](../modules/indexes/vectorstores/examples/deeplake.ipynb)

