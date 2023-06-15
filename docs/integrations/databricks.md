# Databerry



> [Databerry](https://databerry.ai) 是一个[开源](https://github.com/gmpetrov/databerry)的文档检索平台，它可以将您的个人数据与大型语言模型连接起来。





## 安装和设置



我们需要注册Databerry账号，创建数据存储，添加一些数据并获取您的数据存储API端点URL。

我们需要[API密钥](https://docs.databerry.ai/api-reference/authentication)。



## 检索器



查看[用法示例](../modules/indexes/retrievers/examples/databerry.ipynb)。



You can connect to [Databricks runtimes](https://docs.databricks.com/runtime/index.html) and [Databricks SQL](https://www.databricks.com/product/databricks-sql) using the SQLDatabase wrapper of LangChain. See the notebook [Connect to Databricks](./databricks/databricks.html) for details.

from langchain.retrievers import DataberryRetriever

Databricks-managed MLflow integrates with LangChain

---------------------------------------------------



MLflow is an open source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry. See the notebook [MLflow Callback Handler](./mlflow_tracking.ipynb) for details about MLflow's integration with LangChain.



Databricks provides a fully managed and hosted version of MLflow integrated with enterprise security features, high availability, and other Databricks workspace features such as experiment and run management and notebook revision capture. MLflow on Databricks offers an integrated experience for tracking and securing machine learning model training runs and running machine learning projects. See [MLflow guide](https://docs.databricks.com/mlflow/index.html) for more details.



Databricks-managed MLflow makes it more convenient to develop LangChain applications on Databricks. For MLflow tracking, you don't need to set the tracking uri. For MLflow Model Serving, you can save LangChain Chains in the MLflow langchain flavor, and then register and serve the Chain with a few clicks on Databricks, with credentials securely managed by MLflow Model Serving.



Databricks as an LLM provider

-----------------------------



The notebook [Wrap Databricks endpoints as LLMs](../modules/models/llms/integrations/databricks.html) illustrates the method to wrap Databricks endpoints as LLMs in LangChain. It supports two types of endpoints: the serving endpoint, which is recommended for both production and development, and the cluster driver proxy app, which is recommended for interactive development. 



Databricks endpoints support Dolly, but are also great for hosting models like MPT-7B or any other models from the Hugging Face ecosystem. Databricks endpoints can also be used with proprietary models like OpenAI to provide a governance layer for enterprises.



Databricks Dolly

----------------



Databricks’ Dolly is an instruction-following large language model trained on the Databricks machine learning platform that is licensed for commercial use. The model is available on Hugging Face Hub as databricks/dolly-v2-12b. See the notebook [Hugging Face Hub](../modules/models/llms/integrations/huggingface_hub.html) for instructions to access it through the Hugging Face Hub integration with LangChain. 

