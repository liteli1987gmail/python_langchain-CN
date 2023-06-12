## 摘要（Summarization）


> [概念指南](https://docs.langchain.com/docs/use-cases/summarization)（Conceptual Guide）




摘要是创建多个长文档的较小摘要。
这对于将长文档凝结成信息核心非常有用。


开始使用摘要链的推荐方法是:


```python

from langchain.chains.summarize import load_summarize_chain

chain = load_summarize_chain(llm, chain_type="map_reduce")

chain.run(docs)

```



The following resources exist:

- [摘要笔记本](../modules/chains/index_examples/summarize.ipynb): 一本笔记本教你如何完成这个任务。


其他相关资源包括:
- [Utilities for working with Documents](../reference/utils.rst): Guides on how to use several of the utilities which will prove helpful for this task, including Text Splitters (for splitting up long documents).

