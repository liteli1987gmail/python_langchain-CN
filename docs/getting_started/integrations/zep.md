# Zep


>Zep](https://docs.getzep.com/) - 一个用于LLM应用的长期存储。


>`Zep`存储、总结、嵌入、索引和丰富了对话AI聊天历史，并通过简单、低延迟的API公开。

>- 长期存储持久性，可以访问历史消息，而不受总结策略的限制。

>- 基于可配置的消息窗口自动总结存储的消息。一系列摘要被存储，为将来的总结策略提供了灵活性。

>- 对记忆进行向量搜索，消息在创建时自动嵌入。

>- 对记忆和摘要进行自动令牌计数，允许更精细的控制提示组装。

>- 提供Python和JavaScript SDK。



`Zep` 项目](https://github.com/getzep/zep) 


## 安装和设置


```bash

pip install zep_python

```



## 检索器


参见用法示例](../modules/indexes/retrievers/examples/zep_memorystore.ipynb)。


```python

from langchain.retrievers import ZepRetriever

```

