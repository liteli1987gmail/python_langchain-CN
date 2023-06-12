# Deep Lake（深度湖）
此页面介绍如何在LangChain内使用Deep Lake生态系统。

## Deep Lake的优势
- 不仅是一个多模式向量储存库，您还可以使用数据集来微调自己的LLM模型。注：LLM模型指语言模型。
- 不仅储存嵌入向量，还提供自动版本控制功能，便于数据管理。
- 真正的无服务器体系结构，不需要另一个服务，并且可以与主要云提供商（如AWS S3、GCS等）一起使用。

## 更多资源
1. [LangChain和Deep Lake建立ChatGPT以回答您的金融数据问题的终极指南](https://www.activeloop.ai/resources/ultimate-guide-to-lang-chain-deep-lake-build-chat-gpt-to-answer-questions-on-your-financial-data/)
2. [Deep Lake分析Twitter算法代码库](../use_cases/code/twitter-the-algorithm-analysis-deeplake.ipynb)
3. 这是Deep Lake的[白皮书](https://www.deeplake.ai/whitepaper)和[学术论文](https://arxiv.org/pdf/2209.10785.pdf)
4. 以下是可供查阅的其他资源:[Deep Lake](https://github.com/activeloopai/deeplake)、[入门指南](https://docs.activeloop.ai/getting-started)和[Tutorials](https://docs.activeloop.ai/hub-tutorials)

## 安装和设置
- 使用`pip install deeplake`命令安装Python包

## 包装器

### 向量储存库(VectorStore)

Deep Lake是一个专门为深度学习应用而设计的数据湖(Datalake)，其中存在一个包装器，允许您将其用作向量储存库(目前仅限于语义搜索或样本选择)。

导入此向量储存库：
```python
from langchain.vectorstores import DeepLake

```



For a more detailed walkthrough of the Deep Lake wrapper, see [this notebook](../modules/indexes/vectorstores/examples/deeplake.ipynb)

