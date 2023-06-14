查询表格数据



[概念指南](https://docs.langchain.com/docs/use-cases/qa-tabular)





大量的数据和信息存储在表格数据中，无论是csv、excel表格还是SQL表。

本文涵盖了LangChain中用于处理这种格式数据的所有资源。



## 文档加载

如果您有存储在表格格式中的文本数据，您可能希望将数据加载到文档中，然后按照处理其他文本/非结构化数据的方式进行索引。

为此，您应该使用文档加载器，如[CSVLoader](../modules/indexes/document_loaders/examples/csv.ipynb)

然后您应该[创建一个索引](../modules/indexes.rst)用于该数据，并使用[此方式查询](../modules/chains/index_examples/vector_db_qa.ipynb)。



## 查询

如果您有更多的数值型表格数据，或者有大量数据并且不想对其进行索引，您应该从查看我们用于处理此类数据的各种链和代理开始。



### 链



如果您刚刚入门，并且您有相对较小/简单的表格数据，您应该从链开始。

链是一系列预定的步骤，因此它们适合入门，因为它们给您更多控制权并让您更好地理解正在发生的事情。



- [SQL数据库链](../modules/chains/examples/sqlite.ipynb)



### 代理



代理更复杂，涉及多个查询到LLM以了解要做什么。

代理的缺点是您拥有的控制权较少。好处是它们更强大，

这使您可以在较大的数据库和更复杂的模式上使用它们。



- [SQL代理](../modules/agents/toolkits/examples/sql_database.ipynb)

- [Pandas代理](../modules/agents/toolkits/examples/pandas.ipynb)

- [CSV代理](../modules/agents/toolkits/examples/csv.ipynb)

- [Pandas Agent](../modules/agents/toolkits/examples/pandas.ipynb)

- [CSV Agent](../modules/agents/toolkits/examples/csv.ipynb)

