非结构化


## 安装和设置
[Unstructured.IO](https://www.unstructured.io/) extracts clean text from raw source documents like

PDFs and Word documents.

This page covers how to use the [`unstructured`](https://github.com/Unstructured-IO/unstructured)

ecosystem within LangChain.



## Installation and Setup



如果您使用的是本地运行的加载器，请按照以下步骤获取unstructured及其依赖项的本地运行方式。
安装带有`pip install "unstructuredlocal-inference]"`的Python SDK


安装以下系统依赖项（如果系统上没有的话）。根据您解析的文档类型，您可能不需要所有这些依赖项。
- Install the following system dependencies if they are not already available on your system.

  Depending on what document types you're parsing, you may not need all of these.

`libmagic-dev` （文件类型检测）
`poppler-utils` （图像和PDF文档）
`tesseract-ocr`（图像和PDF文档）
`libreoffice` （MS Office文档）
`pandoc` （EPUB文档）


如果您想要更少的设置即可开始运行，请简单地运行`pip install unstructured`并使用 `UnstructuredAPIFileLoader` 或 `UnstructuredAPIFileIOLoader`。这将使用托管的Unstructured API处理您的文档。
simply run `pip install unstructured` and use `UnstructuredAPIFileLoader` or

`UnstructuredAPIFileIOLoader`. That will process your document using the hosted Unstructured API.

请注意，截至2023年5月1日，Unstructured API是公开的，但很快将需要一个API密钥。一旦API密钥可用，Unstructured文档页面](https://unstructured-io.github.io/)将提供生成API密钥的说明。如果您希望自托管Unstructured API或在本地运行它，请查看此处](https://github.com/Unstructured-IO/unstructured-api#dizzy-instructions-for-using-the-docker-image)的说明。
an API. The [Unstructured documentation page](https://unstructured-io.github.io/) will have

instructions on how to generate an API key once they're available. Check out the instructions

[here](https://github.com/Unstructured-IO/unstructured-api#dizzy-instructions-for-using-the-docker-image)

if you'd like to self-host the Unstructured API or run it locally.



## 包装器


### 数据加载器


langchain中的主要unstructured包装器是数据加载器。以下是如何使用最基本的unstructured数据加载器的示例。`langchain.document_loaders` 模块中还提供了其他特定文件的数据加载器。
shows how to use the most basic unstructured data loader. There are other file-specific

data loaders available in the `langchain.document_loaders` module.



```python

from langchain.document_loaders import UnstructuredFileLoader



loader = UnstructuredFileLoader("state_of_the_union.txt")

loader.load()

```



如果使用`UnstructuredFileLoader(mode="elements")`实例化加载器，加载器会在可用时跟踪附加的元数据，如页码和文本类型（例如标题、叙述文本）。
will track additional metadata like the page number and text type (i.e. title, narrative text)

when that information is available.

