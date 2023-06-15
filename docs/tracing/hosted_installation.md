# 云托管设置



我们在 [langchain-plus.vercel.app](https://langchainplus.vercel.app/) 提供了一个托管版本的追踪服务。您可以使用它来查看运行的追踪，而无需在本地运行服务器。



注意：我们目前只针对有限的用户提供此服务。托管平台在积极开发中且处于非常早期的阶段，数据可能会随时丢失。请不要依赖长期持久化在系统中的数据，并且不要记录可能包含敏感信息的追踪。如果您有兴趣使用托管平台，请填写此[表格](https://forms.gle/tRCEMSeopZf6TE3b6)。



## 安装



1. 登录系统并点击右上角的"API Key"。生成一个新的密钥并妥善保管。您将需要它来进行系统身份验证。



## 环境设置



安装完成后，您现在需要配置您的环境以使用追踪功能。



您可以在终端中运行`export LANGCHAIN_HANDLER=langchain`命令来设置环境变量。



您也可以通过将以下代码段添加到每个脚本的顶部来实现。**重要提示：**这必须放在脚本的非常顶部，先于任何从`langchain`导入的内容。



```python

import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"

```



您还需要设置一个环境变量来指定端点和您的 API 密钥。可以通过以下环境变量来完成设置：



1. `LANGCHAIN_ENDPOINT` = "https://langchain-api-gateway-57eoxz8z.uc.gateway.dev"

2. `LANGCHAIN_API_KEY` - 将其设置为安装期间生成的 API 密钥。



以下是添加所有相关环境变量的示例：



```python

import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"

os.environ["LANGCHAIN_ENDPOINT"] = "https://langchain-api-gateway-57eoxz8z.uc.gateway.dev"

os.environ["LANGCHAIN_API_KEY"] = "my_api_key"  # 不要将这个提交到您的存储库中！最好在终端中设置它。

```

