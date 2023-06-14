评估

==========



.. 注意：

   `概念指南 <https://docs.langchain.com/docs/use-cases/evaluation>`_





本文档的本节介绍了我们如何处理和思考LangChain中的评估。

评估内部链/代理的同时，也介绍了我们如何建议在LangChain上构建的人们如何评估。



问题

-----------



评估LangChain链和代理可以非常困难。

这有两个主要原因：



**＃1：缺乏数据**



在启动项目之前，通常不会有大量用于评估链/代理的数据。

这通常是因为大型语言模型（大多数链/代理的核心）是令人惊异的少量和零配置学习器，

这意味着您几乎总能开始处理特定任务（文本到SQL，问答等）而不需要

大量的例子数据集。

这非常不同于传统的机器学习，您必须先收集一堆数据点

才能开始使用模型。



**＃2：缺乏指标**



大多数链/代理执行的任务的性能评估指标都不太好。

例如，最常见的用例之一是生成某种形式的文本。

评估生成的文本比评估分类预测或数字预测要复杂得多。



解决方案

------------



LangChain试图解决这两个问题。

到目前为止，我们所拥有的都是解决方案的初步措施 - 我们认为我们没有完美的解决方案。

因此，我们非常欢迎反馈，贡献，整合和对此的想法。



对于每个问题，我们目前的解决方案如下：



**＃1：缺乏数据**



我们已经开始了`LangChainDatasets <https://huggingface.co/LangChainDatasets>`_，这是Hugging Face上的社区空间。

我们打算将其变成一个用于评估常见的链和代理的开源数据集的集合。

我们已经贡献了五个属于我们自己的数据集，但是我们非常希望这将成为一个社区努力。

为了贡献数据集，您只需要加入社区，然后就可以上传数据集。



我们还旨在使人们尽可能轻松地创建自己的数据集。

作为第一次尝试，我们添加了一个QAGenerationChain，它给出一个文档

提供问题答案对，这些问题答案对可用于日后评估问题答案任务。

有关如何使用此链的示例，请参见`此笔记本电脑 <./evaluation/qa_generation.html>`_。



**＃2：缺乏指标**



我们对指标的缺乏有两个解决方案。



第一个解决方案是不使用指标，而是仅依靠肉眼观察结果，以了解链/代理的性能如何。

为了帮助这一点，我们开发了（并将继续开发）`tracing <../additional_resources/tracing.html>`_，这是一个基于UI的链和代理运行的可视化工具。



我们建议的第二种解决方案是使用语言模型本身来评估输出。

为此，我们有几个不同的链和提示，旨在解决这个问题。



例子

------------



我们创建了许多组合上述两个解决方案的示例，以展示我们在开发时如何评估链和代理。

除了我们策划的示例外，我们也非常欢迎贡献。

为了促进这一点，我们提供了一个`模板笔记本 <./evaluation/benchmarking_template.html>`_，供社区成员用来构建自己的示例。



我们目前拥有的示例包括：



`问答（国情咨文）<./evaluation/qa_benchmarking_sota.html>`_：一个演示如何在国情咨文上进行问题回答的笔记本。



`问答（保罗·格雷厄姆短文）<./evaluation/qa_benchmarking_pg.html>`_：一个演示如何对保罗·格雷厄姆（Paul Graham）短文进行问题回答的笔记本。



`SQL问答（Chinook）<./evaluation/sql_qa_benchmarking_chinook.html>`_：演示在SQL数据库（Chinook数据库）上进行问题回答的笔记本。



`代理向量存储<./evaluation/agent_vectordb_sota_pg.html>`_：演示代理如何在两个不同的向量数据库之间进行路由并进行问题回答的笔记本。



`代理搜索+计算器<./evaluation/agent_benchmarking.html>`_：演示代理如何使用搜索引擎和计算器作为工具进行问题回答的笔记本电脑。



`评估OpenAPI Chain<./evaluation/openapi_eval.html>`_：演示评估OpenAPI链的方法，包括如何生成测试数据（如果您没有数据）。





其他示例

--------------



此外，我们还有一些更通用的评估资源。



`问答<./evaluation/question_answering.html>`_：旨在评估一般问答系统的LLM概述。



`数据增强问答<./evaluation/data_augmented_question_answering.html>`_：一个端到端的示例，用于评估针对特定文档的问答系统（准确地说，是RetrievalQAChain）。此示例突出了如何使用LLM生成用于评估的问题/回答示例，然后突出了如何使用LLM评估生成的示例的性能。



`抱紧面数据集<./evaluation/huggingface_datasets.html>`_：涵盖了从Hugging Face加载和使用数据集进行评估的示例。





.. toctree::

   :maxdepth：1

   :glob：

   :hidden：



   evaluation / * 

