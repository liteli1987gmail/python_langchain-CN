# Hugging Face

本页介绍如何在LangChain内使用Hugging Face生态系统（包括[Hugging Face Hub]（https://huggingface.co））。
它分为两部分:安装和设置,然后是对特定的Hugging Face包装器的引用。

## 安装和设置

如果您想使用Hugging Face Hub:
- 使用`pip install huggingface_hub`安装Hub客户端库
- 创建一个Hugging Face帐户（免费！）
- 创建一个[访问令牌](https://huggingface.co/docs/hub/security-tokens)并将其设置为环境变量（`HUGGINGFACEHUB_API_TOKEN`）

如果您想使用Hugging Face Python库:
- 安装`pip install transformers`以使用模型和标记器
- 安装`pip install datasets`以使用数据集

## 包装器

### LLM

存在两个Hugging Face LLM包装器分别用于本地管道和托管在Hugging Face Hub上的模型。
请注意，这些包装器仅适用于支持以下任务的模型: [`text2text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text2text-generation&sort=downloads), [`text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text-classification&sort=downloads)

使用本地管道包装器:
```python
from langchain.llms import HuggingFacePipeline

```


使用托管在Hugging Face Hub上的模型的包装器:
```python
from langchain.llms import HuggingFaceHub

```

有关Hugging Face Hub包装器的更详细演练，请参见[此笔记本](../modules/models/llms/integrations/huggingface_hub.ipynb)


### 嵌入


有两个Hugging Face嵌入式包装器，一个用于本地模型，另一个用于托管在Hugging Face Hub上的模型。
请注意，这些包装器仅适用于[`sentence-transformers` models](https://huggingface.co/models?library=sentence-transformers&sort=downloads)。


要使用本地pipeline包装器：
```python
from langchain.embeddings import HuggingFaceEmbeddings

```



要使用Hugging Face Hub托管的模型的包装器：
```python
from langchain.embeddings import HuggingFaceHubEmbeddings

```

有关更详细的演练，请参见[此笔记本电脑](../modules/models/text_embedding/examples/huggingface_hub.ipynb)


### 分词器


您可以通过`transformers`包中的多个位置使用标记化器。
默认情况下，它用于计算所有LLM的标记数。


您还可以在使用以下代码片段将文档拆分时使用Tokenizer：
```python
from langchain.text_splitter import CharacterTextSplitter

CharacterTextSplitter.from_huggingface_tokenizer(...)

```

有关更详细的演练，请参见[此笔记本电脑](../modules/indexes/text_splitters/examples/huggingface_length_function.ipynb)




### 数据集


Hugging Face Hub有许多伟大的[数据集](https://huggingface.co/datasets)，可用于评估LLM链。


For a detailed walkthrough of how to use them to do so, see [this notebook](../use_cases/evaluation/huggingface_datasets.ipynb)

