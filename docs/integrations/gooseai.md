GooseAI

本页面介绍了如何在LangChain中使用GooseAI生态系统。
它分为两部分：安装和设置，然后引用特定的GooseAI包装器。

安装和设置
- 使用`pip install openai`安装Python SDK
- 从这里](https://goose.ai/)获取你的GooseAI API密钥。
- 设置环境变量(`GOOSEAI_API_KEY`)。

```python

import os

os.environ["GOOSEAI_API_KEY"] = "YOUR_API_KEY"

```


包装器

LLM

存在一个GooseAI LLM包装器，您可以使用以下方式进行访问：
```python

from langchain.llms import GooseAI

```
