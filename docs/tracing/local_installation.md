本地托管设置


本页面包含了安装并设置使用本地托管版本的追踪的说明


安装


1. 确保已安装Docker（参见获取Docker](https://docs.docker.com/get-docker/)）并且已启动
2. 安装最新版本的`langchain`：`pip install langchain` 或 `pip install langchain -U` 升级已有版本
   的
3. 运行`langchain-server`。该命令在运行上述命令(`pip install langchain`)时自动安装
    1. 默认情况下，服务器将在终端上的端口`4137`上运行
    2. 一旦在终端看到
       输出 `langchain-langchain-frontend-1 | ➜ 本地：http://localhost:4173/](http://localhost:4173/)`, 导航至
       http://localhost:4173/](http://localhost:4173/)


4. 您将看到包含有追踪会话的页面。有关用户界面的详细信息，请参阅概览页面


5. 目前，追踪数据不能保证在`langchain-server`重新运行时持久存在。如果要持久保存您的数据，可以将卷挂载到Docker容器中。有关更多信息，请参阅Docker文档](https://docs.docker.com/storage/volumes/)
       persist your data, you can mount a volume to the Docker container. See the [Docker docs](https://docs.docker.com/storage/volumes/) for more info.

6. 要停止服务器，请在运行`langchain-server`的终端中按下`Ctrl+C`




环境设置


安装完成后，现在必须设置您的环境以使用追踪


可以通过在终端中运行`export LANGCHAIN_HANDLER=langchain`来设置环境变量


您也可以通过将下面的代码段添加到每个脚本的顶部来实现。 **重要：** 必须将此放在脚本的最顶部，在从`langchain`导入任何内容之前

```python

import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"

```


