#  AwaDB# AwaDB（人工智能原生数据库）


>[AwaDB](https://github.com/awa-ai/awadb)是用于LLM应用程序中使用的嵌入向量的搜索和存储的数据库。# LLM（Language Model for Learning）应用程序


安装和设置## 安装和设置


```bash
pip install awadb

```




嵌入向量仓库## 嵌入向量仓库


AwaDB向量数据库存在一个包装器，允许您将其用作向量仓库# 向量仓库
无论是用于语义搜索还是示例选择。


```python
from langchain.vectorstores import AwaDB

```


For a more detailed walkthrough of the AwaDB wrapper, see [this notebook](../modules/indexes/vectorstores/examples/awadb.ipynb)

