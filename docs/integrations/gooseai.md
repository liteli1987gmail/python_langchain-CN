# GooseAI 凤凰AI



本页面介绍了如何在LangChain中使用凤凰AI生态系统。

它分为两个部分：安装和设置，以及对特定凤凰AI包装器的引用。



## 安装和设置

- 使用 `pip install openai` 安装Python SDK

- 从此链接 [here](https://goose.ai/) 获取您的凤凰AI API密钥.

- 设置环境变量 (`GOOSEAI_API_KEY`).



```python

import os

os.environ["GOOSEAI_API_KEY"] = "YOUR_API_KEY"

```



## 包装器



### LLM



存在一个凤凰AI LLM包装器，您可以使用以下方式访问: 

```python

from langchain.llms import GooseAI

```
