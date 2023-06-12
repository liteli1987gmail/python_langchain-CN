# Notion DB（Notion 数据库）

>[Notion](https://www.notion.so/) 是一个协作平台，支持修改过的 Markdown，并集成看板
> 板、任务、维基和数据库。它是一个集万事皆备的工作空间，可用于记笔记、知识和数据管理，以及项目和任务管理。
>

## 安装和设置

所有的说明都在下面的示例中。

## 文档加载器

我们有两个不同的加载器，`NotionDirectoryLoader` 和 `NotionDBLoader`。

请查看 [NotionDirectoryLoader 的使用示例](../modules/indexes/document_loaders/examples/notion.ipynb)。


```python
from langchain.document_loaders import NotionDirectoryLoader

```


请查看 [NotionDBLoader 的使用示例](../modules/indexes/document_loaders/examples/notiondb.ipynb)。


```python

from langchain.document_loaders import NotionDBLoader

```

