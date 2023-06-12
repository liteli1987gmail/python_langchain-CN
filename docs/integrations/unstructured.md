## 无结构化

> `unstructured`包来自[Unstructured.IO](https://www.unstructured.io/)，可以从原始源文件(如PDF和Word文档)中提取干净的文本。
本页面介绍如何在LangChain内使用`unstructured`生态系统。

## 安装和设置

如果您使用的是本地运行的加载程序，请使用以下步骤来在本地运行`unstructured`及其相关依赖项。

- 使用`pip install \"unstructured[local-inference]\"`安装Python SDK
- 如果系统上尚未安装以下系统依赖项，请先安装以下系统依赖项。

如果您想要更少的设置就能运行，请直接执行`pip install unstructured`，并使用`UnstructuredAPIFileLoader`或`UnstructuredAPIFileIOLoader`。这将使用托管的Unstructured API处理您的文档。
请注意，目前(截至2023年5月1日)，Unstructured API是开放的，但很快就会需要API。[Unstructured文档页面](https://unstructured-io.github.io/)将提供有关如何生成API密钥的说明一旦它们可用。如果您想要自托管Unstructured API或在本地运行，请参阅[此处](https://github.com/Unstructured-IO/unstructured-api#dizzy-instructions-for-using-the-docker-image)的说明。

  Depending on what document types you're parsing, you may not need all of these.

    - `libmagic-dev` (filetype detection)

    - `poppler-utils` (images and PDFs)

    - `tesseract-ocr`(images and PDFs)

    - `libreoffice` (MS Office docs)

    - `pandoc` (EPUBs)

## 包装器

### 数据加载器

`langchain`中主要的`unstructured`包装器是数据加载器。以下是如何使用最基本的unstructured数据加载器的示例。`langchain.document_loaders`模块中还有其他特定文件的数据加载器可用。

```python
[here](https://github.com/Unstructured-IO/unstructured-api#dizzy-instructions-for-using-the-docker-image)

if you'd like to self-host the Unstructured API or run it locally.



## Wrappers



### Data Loaders



The primary `unstructured` wrappers within `langchain` are data loaders. The following

shows how to use the most basic unstructured data loader. There are other file-specific

data loaders available in the `langchain.document_loaders` module.



```python

from langchain.document_loaders import UnstructuredFileLoader



loader = UnstructuredFileLoader("state_of_the_union.txt")

loader.load()

```



如果您使用\"UnstructuredFileLoader(mode=\"elements\")\"实例化装载程序，,装载程序将跟踪额外的元数据，如页码和文本类型（即标题,叙述文本） 当此信息可用时。
当此信息可用时，将跟踪附加的元数据，如页码和文本类型（即标题,叙述文本），如果您使用`UnstructuredFileLoader(mode=\"elements\")`实例化装载程序。
when that information is available.

