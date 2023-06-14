概述



> 概念指南](https://docs.langchain.com/docs/use-cases/summarization)





Summarization涉及创建多个较长文档的较小摘要。

这对于提取长文档的核心信息非常有用。



使用summarization链的推荐方法是：



```python

from langchain.chains.summarize import load_summarize_chain

chain = load_summarize_chain(llm, chain_type="map_reduce")

chain.run(docs)

```



存在以下资源：

- Summarization Notebook](../modules/chains/index_examples/summarize.ipynb)：通过此笔记本可以了解如何完成此任务。



其他相关资源包括：

- 用于处理文档的实用工具](../reference/utils.rst)：介绍如何使用几个实用工具，对于此任务非常有帮助，包括文本分割器（用于拆分长文档）。

