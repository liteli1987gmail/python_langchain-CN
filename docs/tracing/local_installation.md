# 本地主机设置



此页面包含安装和设置本地托管版本的跟踪所需的说明。



## 安装



1. 确保您已安装Docker（参见[Get Docker](https://docs.docker.com/get-docker/)）并且正在运行。

2. 安装最新版本的`langchain`：`pip install langchain` 或 `pip install langchain -U` 来升级您的

   现有版本。

3. 运行 `langchain-server`。在运行上述命令（`pip install langchain`）时，该命令将自动安装。

    1. 这将在终端上启动服务器，默认情况下托管在端口 `4137`。

    2. 一旦您在终端上看到

       输出 `langchain-langchain-frontend-1 | ➜ Local: [http://localhost:4173/](http://localhost:4173/)`, 请导航到

       [http://localhost:4173/](http://localhost:4173/)



4. 您应该看到一个包含您的跟踪会话的页面。有关用户界面的操作步骤，请参阅概述页面。



5. 目前，跟踪数据不能保证在每次运行`langchain-server`后持久存在。如果您希望

       保持数据，请将卷挂载到Docker容器。有关更多信息，请参阅[Docker文档](https://docs.docker.com/storage/volumes/)。

6. 要停止服务器，请在运行`langchain-server`的终端中按下 `Ctrl+C`。





## 环境设置



安装完成后，您现在必须设置您的环境以使用跟踪。



这可以通过在终端中设置一个环境变量来完成，运行 `export LANGCHAIN_HANDLER=langchain`。



您还可以通过将以下代码段添加到每个脚本的顶部来完成此操作。**重要：**此代码必须位于脚本的最顶部，即在从`langchain`导入任何内容之前。



```python

import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"

```



