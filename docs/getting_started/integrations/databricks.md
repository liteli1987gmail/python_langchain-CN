Databricks平台

==========



[Databricks](https://www.databricks.com/) Lakehouse Platform将数据、分析和人工智能统一到一个平台上。



Databricks以多种方式支持LangChain生态系统：



1. SQLDatabase Chain的Databricks连接器：SQLDatabase.from_databricks()通过LangChain提供了一种方便的方式，在LangChain上查询您在Databricks上的数据

2. Databricks托管的MLflow与LangChain集成：使用较少的步骤跟踪和提供LangChain应用程序

3. Databricks作为LLM提供者：通过Serving端点或集群驱动程序代理应用程序在Databricks上部署精调的LLM，并将其查询为langchain.llms.Databricks

4. Databricks Dolly：Databricks开源的Dolly可进行商业使用，可以通过Hugging Face Hub访问



SQLDatabase Chain的Databricks连接器

----------------------------------------------

您可以使用LangChain的SQLDatabase包装器连接到[Databricks运行时](https://docs.databricks.com/runtime/index.html)和[Databricks SQL](https://www.databricks.com/product/databricks-sql)。有关详细信息，请参阅[连接到Databricks](./databricks/databricks.html)的笔记本



Databricks托管的MLflow与LangChain集成

---------------------------------------------------



MLflow是一个开源平台，用于管理机器学习生命周期，包括实验、可重现性、部署和中央模型注册表。有关MLflow与LangChain集成的详细信息，请参阅[MLflow回调处理程序](./mlflow_tracking.ipynb)的笔记本



Databricks提供了一个完全托管和托管的MLflow版本，集成了企业安全功能、高可用性和其他Databricks工作区功能，如实验和运行管理以及笔记本修订捕获。Databricks上的MLflow为跟踪和保护机器学习模型训练运行以及运行机器学习项目提供了集成体验。有关更多详细信息，请参阅[MLflow指南](https://docs.databricks.com/mlflow/index.html)



Databricks托管的MLflow使在Databricks上开发LangChain应用程序更加便捷。对于MLflow的跟踪，您不需要设置跟踪uri。对于MLflow模型服务，您可以将LangChain Chain保存在MLflow langchain flavor中，然后使用Databricks上几个点击注册和服务Chain，并由MLflow模型服务安全管理凭据



Databricks作为LLM提供者

-----------------------------



笔记本[将Databricks端点封装为LLM](../modules/models/llms/integrations/databricks.html)演示了如何在LangChain中将Databricks端点封装为LLM的方法。它支持两种类型的端点：建议在生产和开发中都使用的Serving端点和建议在交互式开发中使用的集群驱动程序代理应用程序



Databricks端点支持Dolly，但也非常适合托管来自Hugging Face生态系统的模型，如MPT-7B或任何其他模型。Databricks端点还可与OpenAI等专有模型一起使用，为企业提供治理层



Databricks Dolly

----------------



Databricks的Dolly是在Databricks机器学习平台上训练的一种指令遵循型大语言模型，可商业使用。该模型在Hugging Face Hub上作为databricks/dolly-v2-12b提供。请参阅[Hugging Face Hub](../modules/models/llms/integrations/huggingface_hub.html)的笔记本以了解通过LangChain与Hugging Face Hub集成访问它的说明

