提取

> [概念指南](https://docs.langchain.com/docs/use-cases/extraction)


大多数API和数据库仍处理结构化信息。
因此，为了更好地与这些信息一起工作，从文本中提取结构化信息可能很有用。
其中包括:

- 从句子中提取结构化行以插入数据库
- 从长文档中提取多个行以插入数据库
- 从用户查询中提取正确的API参数

这项工作与[输出解析](../modules/prompts/output_parsers.rst)密切相关。
输出解析器负责指示LLM以特定格式响应。
在这种情况下，, 输出解析器指定要从文档中提取的数据的格式。
然后，, 除了输出格式指令外，,提示还应包含您希望提取信息的数据。

尽管正常的输出解析器足以用于响应数据的基本结构化，,
但在进行提取时，您通常想提取更复杂或嵌套的结构。
深入研究提取，,我们推荐查看[`kor`](https://eyurtsev.github.io/kor/)，,
这是一个使用现有的LangChain链和OutputParser抽象的库
but deep dives on allowing extraction of more complicated schemas.

