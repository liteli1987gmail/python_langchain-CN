# PipelineAI（管道人工智能）

本页介绍如何在LangChain中使用PipelineAI生态系统。
它分为两部分——安装和设置，然后参考特定的PipelineAI包装器。

## 安装和设置

- 使用`pip install pipeline-ai`进行安装
- 获取Pipeline Cloud api密钥并将其设置为环境变量（`PIPELINE_API_KEY`）

## 包装器

### LLM

存在一个PipelineAI LLM包装器，你可以通过以下方式访问

```python

from langchain.llms import PipelineAI

```

