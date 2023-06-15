# MediaWikiDump



>[MediaWiki XML Dumps](https://www.mediawiki.org/wiki/Manual:Importing_XML_dumps) 包含了维基的内容

> （包括所有的修订版本的维基页面），但不包含与网站相关的数据。 XML dump 不会创建完整的备份

> 维基数据库的备份不包含用户账号、图片、编辑日志等信息。





## 安装和设置



我们需要安装几个Python包。



`mediawiki-utilities` 在未合并分支中支持XML schema 0.11

```bash

pip install -qU git+https://github.com/mediawiki-utilities/python-mwtypes@updates_schema_0.11

```



`mediawiki-utilities mwxml` 存在一个bug，修复PR正在等待中。



```bash

pip install -qU git+https://github.com/gdedrouas/python-mwxml@xml_format_0.11

pip install -qU mwparserfromhell

```



## 文档加载器



查看一个[使用示例](../modules/indexes/document_loaders/examples/mediawikidump.ipynb)。





```python

from langchain.document_loaders import MWDumpLoader

```

