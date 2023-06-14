# Hugging Face



本页面介绍了如何在LangChain中使用Hugging Face生态系统（包括[Hugging Face Hub](https://huggingface.co)）。

它分为两个部分：安装和设置，然后是对特定Hugging Face封装的引用。



## 安装和设置



如果你想使用Hugging Face Hub：

- 使用`pip install huggingface_hub`安装Hub客户端库

- 创建Hugging Face账户（免费！）

- 创建一个[访问令牌](https://huggingface.co/docs/hub/security-tokens)并将其设为环境变量（`HUGGINGFACEHUB_API_TOKEN`）



如果要使用Hugging Face Python库：

- 使用`pip install transformers`安装用于模型和tokenizer的库

- 使用`pip install datasets`安装用于数据集的库



## 封装器



### LLM



存在两种Hugging Face LLM封装器，一种用于本地处理流程，一种用于托管在Hugging Face Hub上的模型。

请注意，这些封装器仅适用于支持以下任务的模型：[`text2text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text2text-generation&sort=downloads), [`text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text-classification&sort=downloads)



要使用本地处理流程封装器：

```python

from langchain.llms import HuggingFacePipeline

```



要使用托管在Hugging Face Hub上的模型封装器：

```python

from langchain.llms import HuggingFaceHub

```

有关Hugging Face Hub封装器的更详细信息，请参阅[此笔记本](../modules/models/llms/integrations/huggingface_hub.ipynb)





### Embeddings



存在两种Hugging Face Embeddings封装器，一种用于本地模型，一种用于托管在Hugging Face Hub上的模型。

请注意，这些封装器仅适用于[`sentence-transformers`模型](https://huggingface.co/models?library=sentence-transformers&sort=downloads)。



要使用本地处理流程封装器：

```python

from langchain.embeddings import HuggingFaceEmbeddings

```



要使用托管在Hugging Face Hub上的模型封装器：

```python

from langchain.embeddings import HuggingFaceHubEmbeddings

```

有关此内容的更详细介绍，请参阅[此笔记本](../modules/models/text_embedding/examples/huggingface_hub.ipynb)



### Tokenizer



您可以在`transformers`包中的许多地方使用tokenizer。

默认情况下，它用于计算LLMs的所有token数。



您还可以使用它在拆分文档时计算token数

```python

from langchain.text_splitter import CharacterTextSplitter

CharacterTextSplitter.from_huggingface_tokenizer(...)

```

有关此内容的更详细介绍，请参阅[此笔记本](../modules/indexes/text_splitters/examples/huggingface_length_function.ipynb)





### 数据集



Hugging Face Hub有许多优秀的[数据集](https://huggingface.co/datasets)，可用于评估LLM链。



有关如何使用它们进行评估的详细介绍，请参阅[此笔记本](../use_cases/evaluation/huggingface_datasets.ipynb)

