# 概述



> [概念指引](https://docs.langchain.com/docs/use-cases/summarization)





Summarization涉及创建多个较长文档的较小摘要。

这对于提取长文档的核心信息非常有用。



使用摘要链的推荐方法如下：



```python

from langchain.chains.summarize import load_summarize_chain

chain = load_summarize_chain(llm, chain_type="map_reduce")

chain.run(docs)

```



以下资源可用：

- [摘要 Notebok](../modules/chains/index_examples/summarize.ipynb): 通过演示如何完成此任务的笔记本。



附加的相关资源包括：

- [文档工具](../reference/utils.rst)：有关如何使用几个对此任务非常有帮助的实用程序的指南，包括文本拆分器（用于拆分长文档）。

