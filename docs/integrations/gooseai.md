# GooseAI（注：GooseAI为一个公司的名字）


本页介绍如何在LangChain中使用GooseAI生态系统。
它分为两个部分：安装和设置,然后引用特定的GooseAI封装器。


## 安装和设置
- 通过`pip install openai`安装Python SDK。
- 从此链接[here](https://goose.ai/)获取您的GooseAI API密钥。
- 设置环境变量（`GOOSEAI_API_KEY`）。


```python

import os

os.environ["GOOSEAI_API_KEY"] = "YOUR_API_KEY"

```



## 封装器


### LLM


There exists an GooseAI LLM wrapper, which you can access with: 

```python

from langchain.llms import GooseAI

```
