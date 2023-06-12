# 本地托管设置


本页面包含安装和设置环境以使用本地托管版本的跟踪的说明。


## 安装


1. 确保您已安装 Docker（请参阅 [获取 Docker](https://docs.docker.com/get-docker/)），并且正在运行。
2. 安装最新版本的 `langchain` : `pip install langchain` 或 `pip install langchain -U` 以升级您的。
   existing version.

3. 运行`langchain-server`。当您运行上述命令（`pip install langchain`）时，此命令会自动安装。
    1. This will spin up the server in the terminal, hosted on port `4137` by default.

    2. Once you see the terminal

       output `langchain-langchain-frontend-1 | ➜ Local: [http://localhost:4173/](http://localhost:4173/)`, navigate

       to [http://localhost:4173/](http://localhost:4173/)



4. 您应该会看到一个带有跟踪会话的页面。有关 UI 的演练，请参阅概述页面。


5. 目前 `trace` 数据不能保证在运行 `langchain-server` 的多次运行之间持续存在。如果您想要
       persist your data, you can mount a volume to the Docker container. See the [Docker docs](https://docs.docker.com/storage/volumes/) for more info.

6. 要停止服务器，请在运行 `langchain-server` 的终端中按`Ctrl + C`。




## 环境设置


安装后，您现在必须设置环境以使用跟踪。


可以通过在终端中运行 `export LANGCHAIN_HANDLER = langchain` 来设置环境变量来完成此操作。


您还可以通过将以下代码片段添加到每个脚本的顶部来完成此操作。 **重要:** 这必须放在您从 `langchain` 导入任何内容之前的脚本顶部。


```python

import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"

```



