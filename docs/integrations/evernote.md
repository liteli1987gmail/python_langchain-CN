# EverNote 印象笔记


>[EverNote](https://evernote.com/) 旨在用于存档和创建笔记，其中可以嵌入照片、音频和保存的网络内容。笔记存储在虚拟的"笔记本"中，可以进行标记、注释、编辑、搜索和导出。


## 安装和设置


首先，您需要安装 `lxml` 和 `html2text` Python 包。


```bash

pip install lxml
pip install html2text
```



## 文档加载器


参见[使用示例](../modules/indexes/document_loaders/examples/evernote.ipynb)。


```python

from langchain.document_loaders import EverNoteLoader
```

