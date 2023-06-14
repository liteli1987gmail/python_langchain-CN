# 云托管设置



我们在 langchainplus.vercel.app](https://langchainplus.vercel.app/) 上提供了一个托管版本的跟踪。您可以使用它来查看运行的跟踪，而无需在本地运行服务器。



注意：目前我们只向有限数量的用户提供此服务。托管平台正在积极开发中，数据可能会随时丢失。请不要依赖系统中长期持久化的数据，也不要记录可能包含敏感信息的跟踪。如果您有兴趣使用托管平台，请填写此处](https://forms.gle/tRCEMSeopZf6TE3b6)的表单。



## 安装



1. 登录系统，点击右上角的"API密钥"。生成一个新的密钥并妥善保管。您将需要它来进行系统身份验证。



## 环境设置



安装后，您需要设置环境以使用跟踪功能。



您可以通过在终端中运行 `export LANGCHAIN_HANDLER=langchain` 命令来设置环境变量。



您还可以在每个脚本的顶部添加以下代码片段来完成设置。**重要注意事项：**该代码必须放置在脚本的最顶部，在导入任何 `langchain` 模块之前。



```python

import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"

```



您还需要设置一个环境变量来指定端点和您的API密钥。可以通过以下环境变量来完成设置：



1. `LANGCHAIN_ENDPOINT` = "https://langchain-api-gateway-57eoxz8z.uc.gateway.dev"

2. `LANGCHAIN_API_KEY` - 将其设置为您在安装过程中生成的API密钥。



添加所有相关环境变量的示例如下：



```python

import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"

os.environ["LANGCHAIN_ENDPOINT"] = "https://langchain-api-gateway-57eoxz8z.uc.gateway.dev"

os.environ["LANGCHAIN_API_KEY"] = "my_api_key"  # Don't commit this to your repo! Better to set it in your terminal.

```

