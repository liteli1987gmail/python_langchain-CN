CerebriumAI

本页面介绍如何在LangChain中使用CerebriumAI生态系统。
它分为两个部分：安装和设置，以及对特定CerebriumAI封装的引用。

安装和设置
- 使用`pip install cerebrium`进行安装
- 获取CerebriumAI API密钥并将其设置为环境变量（`CEREBRIUMAI_API_KEY`）

封装器

LLM

存在一个CerebriumAI LLM封装器，您可以使用以下方式访问
```python

from langchain.llms import CerebriumAI

```