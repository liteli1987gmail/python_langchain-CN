# Hugging Face致力于


本页面介绍了如何在LangChain中使用Hugging Face生态系统（包括[Hugging Face Hub](https://huggingface.co)）。

分为两个部分：安装和设置，以及对特定Hugging Face包装器的引用。



## 安装和设置



如果您想使用Hugging Face Hub：

- 使用`pip install huggingface_hub`安装Hub客户端库

- 创建Hugging Face账户（免费！）

- 创建[access token](https://huggingface.co/docs/hub/security-tokens)并将其设置为环境变量（`HUGGINGFACEHUB_API_TOKEN`）



如果您想使用Hugging Face Python库：

- 使用`pip install transformers`安装用于处理模型和分词器的库

- 使用`pip install datasets`安装用于处理数据集的库



## 包装器



### LLM



Hugging Face存在两个LLM包装器，一个用于本地pipeline，一个用于在Hugging Face Hub上托管的模型。

请注意，这些包装器仅适用于支持以下任务的模型：[`text2text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text2text-generation&sort=downloads)，[`text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text-classification&sort=downloads)



要使用本地pipeline包装器：

```python

from langchain.llms import HuggingFacePipeline

```



要使用在Hugging Face Hub上托管的模型的包装器：

```python

from langchain.llms import HuggingFaceHub

```

有关Hugging Face Hub包装器的更详细操作，请参见[此笔记本](../modules/models/llms/integrations/huggingface_hub.ipynb)





### Embeddings



Hugging Face存在两个Embeddings包装器，一个用于本地模型，一个用于在Hugging Face Hub上托管的模型。

请注意，这些包装器仅适用于[`sentence-transformers`模型](https://huggingface.co/models?library=sentence-transformers&sort=downloads)。



要使用本地pipeline包装器：

```python

from langchain.embeddings import HuggingFaceEmbeddings

```



要使用在Hugging Face Hub上托管的模型的包装器：

```python

from langchain.embeddings import HuggingFaceHubEmbeddings

```

有关此操作的更详细介绍，请参见[此笔记本](../modules/models/text_embedding/examples/huggingface_hub.ipynb)



### Tokenizer



您可以在`transformers`包中的几个位置使用标记器。

默认情况下，它用于计算LLMs的所有标记。



您还可以在拆分文档时使用它来计算标记

```python

from langchain.text_splitter import CharacterTextSplitter

CharacterTextSplitter.from_huggingface_tokenizer(...)

```

有关此操作的更详细介绍，请参见[此笔记本](../modules/indexes/text_splitters/examples/huggingface_length_function.ipynb)





### 数据集



Hugging Face Hub有许多出色的[数据集](https://huggingface.co/datasets)，可用于评估LLM链。



有关如何使用它们进行评估的详细介绍，请参见[此笔记本](../use_cases/evaluation/huggingface_datasets.ipynb)

