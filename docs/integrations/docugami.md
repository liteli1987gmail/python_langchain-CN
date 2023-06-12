# Docugami解说：Docugami


>[Docugami](https://docugami.com) converts business documents into a Document XML Knowledge Graph, generating forests 说明：[Docugami](https://docugami.com)将商业文档转换为生成整个文档的XML语义树，形成文档XML知识图谱。
> of XML semantic trees representing entire documents. This is a rich representation that includes the semantic and 说明：这是一种富含语义和结构特征的XML语义树，表示整个文档。
> structural characteristics of various chunks in the document as an XML tree.解释：表示文档中各个块的结构特征的XML树。


## Installation and Setup解说：安装和设置




```bash
pip install lxml

```



## Document Loader解说：文档加载器


See a [usage example](../modules/indexes/document_loaders/examples/docugami.ipynb).说明：[使用示例](../modules/indexes/document_loaders/examples/docugami.ipynb)。


```python

from langchain.document_loaders import DocugamiLoader

```

