Databricks
==========

Databricks（https://www.databricks.com/） Lakehouse平台将数据、分析和人工智能统一到一个平台上。

Databricks以多种方式拥抱LangChain生态系统:

1. Databricks连接器用于SQLDatabase Chain: SQLDatabase.from_databricks()提供了一种在LangChain上查询Databricks数据的简单方法
2. Databricks管理的MLflow与LangChain集成:跟踪和服务LangChain应用程序的步骤更少
3. Databricks作为LLM提供商:通过服务端点或集群驱动程序代理应用程序在Databricks上部署您的精调LLMs，并将其查询为langchain.llms.Databricks
4. Databricks Dolly: Databricks开源的Dolly允许商业使用 :并可以通过Hugging Face Hub访问

Databricks连接器用于SQLDatabase Chain
------------------------------------------------
您可以使用LangChain的SQLDatabase包装器连接[Databricks runtimes](https://docs.databricks.com/runtime/index.html)和[Databricks SQL](https://www.databricks.com/product/databricks-sql)。有关详细信息，请参见笔记本[连接到Databricks](./databricks/databricks.html)。

Databricks管理的MLflow与LangChain集成
-----------------------------------------------------

MLflow是一个开源平台，用于管理ML生命周期，包括实验、可重复性、部署和中央模型注册表。有关MLflow与LangChain集成的详细信息，请参见笔记本[MLflow Callback Handler](./mlflow_tracking.ipynb)。


Databricks提供了一个完全托管和托管版本的MLflow，集成了企业安全功能,高可用性,和其他Databricks工作区功能，如实验和运行管理以及笔记本修订捕获。MLflow on Databricks为跟踪和保护机器学习模型训练运行和运行机器学习项目提供了一个集成的体验。有关更多详细信息，请参阅[MLflow指南]（https : //docs.databricks.com/mlflow/index.html）。

Databricks托管的MLflow使在Databricks上开发LangChain应用程序更加便捷。对于MLflow跟踪，您不需要设置跟踪uri。对于MLflow模型服务，,您可以将LangChain Chains保存在MLflow langchain风味中，然后使用几个单击在Databricks上注册和服务Chain，凭据由MLflow Model Serving安全管理。

Databricks作为LLM提供者
-----------------------------

笔记本电脑[Wrap Databricks endpoints as LLMs]（../modules/models/llms/integrations/databricks.html）说明了将Databricks端点包装为LangChain中的LLMs的方法。它支持两种类型的端点:服务端点，,推荐用于生产和开发，,和集群驱动程序代理应用程序，,推荐用于交互式开发。

Databricks端点支持Dolly，,但也非常适合托管Hugging Face生态系统中的模型，如MPT-7B或任何其他模型。Databricks端点也可以与专有模型（如OpenAI）一起使用，为企业提供治理层。

Databricks Dolly
----------------


Databricks’ Dolly is an instruction-following large language model trained on the Databricks machine learning platform that is licensed for commercial use. The model is available on Hugging Face Hub as databricks/dolly-v2-12b. See the notebook [Hugging Face Hub](../modules/models/llms/integrations/huggingface_hub.html) for instructions to access it through the Hugging Face Hub integration with LangChain. 

