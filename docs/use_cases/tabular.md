# 查询表格数据


> [概念指南](https://docs.langchain.com/docs/use-cases/qa-tabular)




许多数据和信息存储在表格数据中，无论是csv、Excel表格还是SQL表格。
本页介绍了LangChain中用于处理这种格式数据的所有资源。


## 文档加载
如果您将文本数据存储在表格格式中，则可能需要将数据加载到文档中，然后像处理其他文本/非结构化数据一样对其进行索引。为此，您应该使用像[CSVLoader](../modules/indexes/document_loaders/examples/csv.ipynb)这样的文档加载器，然后应该[创建索引](../modules/indexes.rst)在那些数据上，以[这种方式进行查询](../modules/chains/index_examples/vector_db_qa.ipynb)。
other text/unstructured data. For this, you should use a document loader like the [CSVLoader](../modules/indexes/document_loaders/examples/csv.ipynb)

and then you should [create an index](../modules/indexes.rst) over that data, and [query it that way](../modules/chains/index_examples/vector_db_qa.ipynb).



## 查询
如果您有更多的数值表格数据，或者有大量数据且不想对其进行索引，则应开始查看我们用于处理此数据的各种链和代理。
by looking at various chains and agents we have for dealing with this data.



### 链


如果您刚开始，并且有相对较小/简单的表格数据，则应该开始使用链。链是一系列预定步骤，因此它们很适合入门，因为它们可以让您更有控制力，让您更好地理解正在发生的事情。
Chains are a sequence of predetermined steps, so they are good to get started with as they give you more control and let you 

understand what is happening better.



- [SQL数据库链](../modules/chains/examples/sqlite.ipynb)


### 代理


Agents are more complex, and involve multiple queries to the LLM to understand what to do.

The downside of agents are that you have less control. The upside is that they are more powerful,

which allows you to use them on larger databases and more complex schemas. 



- [SQL代理](../modules/agents/toolkits/examples/sql_database.ipynb)
- [Pandas代理](../modules/agents/toolkits/examples/pandas.ipynb)
- [CSV Agent](../modules/agents/toolkits/examples/csv.ipynb)

