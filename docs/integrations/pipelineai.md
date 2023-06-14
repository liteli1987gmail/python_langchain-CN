PipelineAI

该页面介绍如何在LangChain中使用PipelineAI生态系统。
分为两部分：安装和设置，然后引用特定的PipelineAI包装器。

安装和设置

- 使用`pip install pipeline-ai`进行安装
- 获取Pipeline Cloud api密钥并将其设置为环境变量（`PIPELINE_API_KEY`）

包装器

LLM包装器

存在一个PipelineAI LLM包装器，您可以通过以下方式访问

```python

from langchain.llms import PipelineAI

```

