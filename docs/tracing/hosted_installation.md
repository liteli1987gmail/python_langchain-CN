# 云托管设置

我们提供托管版本的跟踪服务，您可以通过 [langchainplus.vercel.app](https://langchainplus.vercel.app/) 访问。使用此服务可查看您的运行记录，无需在本地运行服务器。

注意：目前我们仅向部分用户提供此服务。此托管平台处于非常初期的开发阶段，并且数据随时可能会丢失。请勿将可能包含敏感信息的运行记录长期存储在系统中。如果您有兴趣使用托管平台，请填写 [此处的表格](https://forms.gle/tRCEMSeopZf6TE3b6)。

## 安装

1. 登录系统，点击右上角的\"API Key\"。生成一个新的密钥并妥善保存。您将需要此密钥与系统进行身份验证。

## 环境设置

安装后，您现在必须设置环境来使用跟踪功能。

您可以通过在终端中运行 `export LANGCHAIN_HANDLER=langchain` 命令来设置环境变量。

您也可以通过在每个脚本的顶部添加下面的代码片段来做到这一点。 **重要提示**：此代码片段必须位于脚本的最顶部，即在从 `langchain` 导入任何内容之前。

```python
import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"

```


此外，您还需要设置一个环境变量来指定终端节点和您的 API 密钥。您可以通过以下环境变量来完成此操作:

1. `LANGCHAIN_ENDPOINT` = \"https://langchain-api-gateway-57eoxz8z.uc.gateway.dev\"
2. `LANGCHAIN_API_KEY` - 将其设置为您在安装过程中生成的 API 密钥。

下面是添加所有相关环境变量的示例:

```python

import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"

os.environ["LANGCHAIN_ENDPOINT"] = "https://langchain-api-gateway-57eoxz8z.uc.gateway.dev"

os.environ["LANGCHAIN_API_KEY"] = "my_api_key"  # Don't commit this to your repo! Better to set it in your terminal.

```

