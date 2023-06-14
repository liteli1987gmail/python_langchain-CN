# Weaviate


This page covers how to use the Weaviate ecosystem within LangChain.


What is Weaviate?


Weaviate简介:
- Weaviate是一种开源的向量搜索引擎数据库。
- Weaviate允许您以类似于类属性的方式存储JSON文档，同时附加机器学习向量来表示这些文档在向量空间中。
- Weaviate可以独立使用（也可带上您的向量），或者与各种模块一起使用，这些模块可以为您进行矢量化，并扩展核心功能。
- Weaviate具有GraphQL-API，可轻松访问您的数据。
- 我们的目标是使您的向量搜索设置能够在几毫秒内进行生产查询（请查看我们的开源基准测试](https://weaviate.io/developers/weaviate/current/benchmarks/)，以了解Weaviate是否适合您的用例）。
- 在不到五分钟的时间内，通过基础入门指南](https://weaviate.io/developers/weaviate/current/core-knowledge/basics.html)了解Weaviate。


Weaviate详细信息：


Weaviate是一个低延迟的向量搜索引擎，支持不同的媒体类型（文本、图像等）。它提供语义搜索、问答提取、分类、可定制模型（PyTorch/TensorFlow/Keras）等功能。Weaviate从头开始构建，可以同时存储对象和向量，允许将向量搜索与结构化过滤和云原生数据库的容错性相结合。通过GraphQL、REST和各种客户端编程语言都可以访问。


安装和设置
- 通过`pip install weaviate-client`安装Python SDK
包装器


VectorStore


已经存在一个围绕Weaviate索引的包装器，使您可以将其用作向量存储，
无论是用于语义搜索还是示例选择。


要导入此向量存储：
```python

from langchain.vectorstores import Weaviate

```



有关Weaviate包装器的更详细操作说明，请参阅此笔记本](../modules/indexes/vectorstores/examples/weaviate.ipynb)
