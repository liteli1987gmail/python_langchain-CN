# 查询表格数据



> [概念指南](https://docs.langchain.com/docs/use-cases/qa-tabular)





大量的数据和信息存储在表格数据中，无论是csv文件、Excel表格还是SQL表。

该页面涵盖了LangChain中用于处理这种格式数据的所有资源。



## 文档加载

如果您以表格格式存储文本数据，您可能希望将数据加载到文档中，然后像处理其他文本/非结构化数据一样对其进行索引。

为此，您应该使用类似于[CSVLoader](../modules/indexes/document_loaders/examples/csv.ipynb)的文档加载器，然后您应该使用[创建索引](../modules/indexes.rst)和[查询](../modules/chains/index_examples/vector_db_qa.ipynb)的方式来进行数据操作。





## 查询

如果您拥有更多的数值型表格数据，或者拥有大量数据但不想对其进行索引，您应该查看我们为处理这些数据所提供的各种链和代理。



### 链



如果您刚开始并且拥有相对较小/简单的表格数据，您应该从链开始入手。

链是一系列预定步骤，因此它们适合初学者，因为它们给予您更多控制权并让您更好地了解正在发生的情况。



- [SQL数据库链](../modules/chains/examples/sqlite.ipynb)



- [SQL Database Chain](../modules/chains/examples/sqlite.ipynb)



### 代理



代理更加复杂，需要多个查询到LLM以了解应该执行的操作。

代理的缺点是您拥有的控制权较少。优点是它们更强大，允许您在更大的数据库和更复杂的模式上使用它们。





- [SQL代理](../modules/agents/toolkits/examples/sql_database.ipynb)

- [Pandas代理](../modules/agents/toolkits/examples/pandas.ipynb)

- [CSV代理](../modules/agents/toolkits/examples/csv.ipynb)

