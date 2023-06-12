# 十进制

学习如何在Baseten上使用部署的模型与LangChain一起使用。 

## 安装和设置

 - 创建[Baseten]（https : //baseten.co）帐户和[API密钥]（https : //docs.baseten. co / settings / api-keys）。 
 - 使用`pip install baseten`安装Baseten Python客户端
 - 使用您的API密钥进行身份验证`baseten login`

## 调用模型

Baseten通过LLM模块与LangChain集成，该模块为在Baseten工作空间上部署的模型提供了标准化和互操作的接口。 

您可以使用[Baseten模型库](https : //app.baseten.co/explore/)一键部署基础模型，如WizardLM和Alpaca，或者如果您拥有自己的模型，请使用此“[部署教程]”（https : //docs.baseten.co/deploying-models/deploy）进行部署。 

在此示例中，我们将使用WizardLM。[在此处部署WizardLM](https : //app.baseten.co/explore/wizardlm)，并关注已部署模型的[版本ID]（https : //docs.baseten.co/managing-models/manage）。 

```python

from langchain.llms import Baseten



wizardlm = Baseten(model="MODEL_VERSION_ID", verbose=True)



wizardlm("What is the difference between a Wizard and a Sorcerer?")

```

