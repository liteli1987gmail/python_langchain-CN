基数



学习如何在Baseten上使用已部署模型的LangChain。



安装和设置



- 创建一个Baseten](https://baseten.co)账户，并获取API密钥](https://docs.baseten.co/settings/api-keys)。

- 使用`pip install baseten`命令安装Baseten Python客户端

- 使用您的API密钥进行身份验证，使用`baseten login`命令



调用模型



Baseten通过LLM模块与LangChain集成，该模块为部署在您的Baseten工作空间上的模型提供了标准化和可互操作的接口。



您可以通过Baseten模型库](https://app.baseten.co/explore/)一键部署基础模型，如WizardLM和Alpaca，或者如果您有自己的模型，可以按照本教程部署模型](https://docs.baseten.co/deploying-models/deploy)。



在本示例中，我们将使用WizardLM。在这里部署WizardLM](https://app.baseten.co/explore/wizardlm)，然后按照已部署模型的版本ID](https://docs.baseten.co/managing-models/manage)进行操作。



```python

from langchain.llms import Baseten



wizardlm = Baseten(model="MODEL_VERSION_ID", verbose=True)



wizardlm("What is the difference between a Wizard and a Sorcerer?")

```

