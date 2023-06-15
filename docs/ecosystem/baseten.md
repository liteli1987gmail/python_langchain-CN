# Baseten



了解如何在 Baseten 上使用已部署的模型进行 LangChain。



## 安装和设置



- 创建一个 [Baseten](https://baseten.co) 账号并获取 [API 密钥](https://docs.baseten.co/settings/api-keys)。

- 使用 `pip install baseten` 命令安装 Baseten Python 客户端

- 使用 API 密钥进行身份验证 `baseten login`



## 调用模型



Baseten 通过 LLM 模块与 LangChain 集成，该模块为已部署在 Baseten 工作区上的模型提供了标准化和可互操作的接口。



您可以通过一键直接从 [Baseten 模型库](https://app.baseten.co/explore/) 部署基础模型，例如 WizardLM 和 Alpaca，或者如果您有自己的模型，可以参考 [该教程](https://docs.baseten.co/deploying-models/deploy) 进行部署。



在这个例子中，我们将使用 WizardLM。请点击 [此处部署 WizardLM](https://app.baseten.co/explore/wizardlm) 并按照部署的 [模型版本 ID](https://docs.baseten.co/managing-models/manage) 进行操作。



```python

from langchain.llms import Baseten



wizardlm = Baseten(model="MODEL_VERSION_ID", verbose=True)



wizardlm("巫师和术士有什么区别？")

```

