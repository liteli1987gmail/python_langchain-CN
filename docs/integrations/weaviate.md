# Weaviate（Weaviate）

This page covers how to use the Weaviate ecosystem within LangChain.（本页介绍如何在 LangChain 中使用 Weaviate 生态系统。）

What is Weaviate?（什么是 Weaviate？）

**Weaviate in a nutshell:**（简介:）
- Weaviate is an open-source ​database of the type ​vector search engine.（Weaviate 是一种开源的矢量搜索引擎数据库。）
- Weaviate allows you to store JSON documents in a class property-like fashion while attaching machine learning vectors to these documents to represent them in vector space.（Weaviate 允许你以类属性方式存储 JSON 文档，同时将机器学习向量附加到这些文档上，以在向量空间中表示它们。）
- Weaviate can be used stand-alone (aka bring your vectors) or with a variety of modules that can do the vectorization for you and extend the core capabilities.（Weaviate 可以独立使用（也就是带上你的向量），也可以与多种模块配合使用，这些模块可以为你进行向量化操作并扩展核心功能。）
- Weaviate has a GraphQL-API to access your data easily.（Weaviate 拥有 GraphQL-API，可以轻松访问您的数据。）
- We aim to bring your vector search set up to production to query in mere milliseconds (check our [open source benchmarks](https://weaviate.io/developers/weaviate/current/benchmarks/) to see if Weaviate fits your use case).（我们旨在使您的矢量搜索设置能够在毫秒级别内查询生产环境（检查我们的开源基准测试，以查看 Weaviate 是否适合您的用例）。）
- Get to know Weaviate in the [basics getting started guide](https://weaviate.io/developers/weaviate/current/core-knowledge/basics.html) in under five minutes.（在五分钟内，通过 [基础入门指南](https://weaviate.io/developers/weaviate/current/core-knowledge/basics.html) 了解 Weaviate。）

**Weaviate in detail:**（详细介绍 :）

Weaviate is a low-latency vector search engine with out-of-the-box support for different media types (text, images, etc.). It offers Semantic Search, Question-Answer Extraction, Classification, Customizable Models (PyTorch/TensorFlow/Keras), etc. Built from scratch in Go, Weaviate stores both objects and vectors, allowing for combining vector search with structured filtering and the fault tolerance of a cloud-native database. It is all accessible through GraphQL, REST, and various client-side programming languages.（Weaviate 是一种低延迟的矢量搜索引擎，具有内置支持不同媒体类型（文本，图像等）的功能。它提供了语义搜索，问答提取，分类，可定制模型（PyTorch/TensorFlow/Keras）等功能。Weaviate 是从头开始使用 Go 构建的，并存储对象和向量，可以将向量搜索与结构化过滤和云原生数据库的容错性相结合。它可以通过 GraphQL、REST 和各种客户端编程语言进行访问。）

## Installation and Setup（安装和设置）
- Install the Python SDK with `pip install weaviate-client`（使用 `pip install weaviate-client` 安装 Python SDK。）
## Wrappers（封装器）

### VectorStore（矢量存储）


Weaviate索引周围存在一个包装器，允许您将其用作向量存储，无论是用于语义搜索还是示例选择。
注意: 该行没有需要翻译的文本。
注意: 该行没有需要翻译的文本。
要导入这个向量存储: 
```python
from langchain.vectorstores import Weaviate

```

注意: 该行没有需要翻译的文本。
For a more detailed walkthrough of the Weaviate wrapper, see [this notebook](../modules/indexes/vectorstores/examples/weaviate.ipynb)

