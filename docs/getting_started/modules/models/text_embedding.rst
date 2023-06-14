文本嵌入模型

==========================



注意：

   `概念指南<https://docs.langchain.com/docs/components/models/text-embedding-model>`_





本文档介绍如何在 LangChain 中使用 Embedding 类。



Embedding 类是一个为嵌入提供接口的类。有许多嵌入提供商（OpenAI、Cohere、Hugging Face 等）-这个类旨在为所有这些提供商提供标准接口。



嵌入创建文本的向量表示。这很有用，因为这意味着我们可以在向量空间中思考文本，并进行语义搜索，寻找在向量空间中最相似的文本片段。



LangChain 中的基本 Embedding 类公开了两种方法：`embed_documents`和`embed_query`。最大的区别在于这两种方法具有不同的接口：一个适用于多个文档，而另一个适用于单个文档。此外，将这些方法作为两个单独的方法之一的另一个原因是，一些嵌入提供商针对文档（要搜索的文档）和查询（搜索查询本身）具有不同的嵌入方法。



以下文本嵌入的集成存在。



.. toctree::

   :maxdepth: 1

   ：glob：



   ./text_embedding/examples/*

