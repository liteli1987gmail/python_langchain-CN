# MediaWikiDump（媒体维基转储）


>[MediaWiki XML Dumps](https://www.mediawiki.org/wiki/Manual:Importing_XML_dumps) contain the content of a wiki （[MediaWiki XML转储](https://www.mediawiki.org/wiki/Manual:Importing_XML_dumps)包含维基的内容）
> (wiki pages with all their revisions), without the site-related data. A XML dump does not create a full backup （其中包含所有修订的维基页面）,不包含与站点相关的数据。XML转储不创建完整的备份。）
> of the wiki database, the dump does not contain user accounts, images, edit logs, etc.（维基数据库的内容）,不包含用户帐户、图像、编辑日志等。）




## Installation and Setup（安装和设置）


We need to install several python packages.（我们需要安装几个Python包。）


The `mediawiki-utilities` supports XML schema 0.11 in unmerged branches.（`mediawiki-utilities`支持未合并分支的XML模式0.11。）
```bash

pip install -qU git+https://github.com/mediawiki-utilities/python-mwtypes:updates_schema_0.11

```



The `mediawiki-utilities mwxml` has a bug, fix PR pending.（`mediawiki-utilities mwxml`存在一个错误,修复PR待定。）


```bash

pip install -qU git+https://github.com/gdedrouas/python-mwxml:xml_format_0.11

pip install -qU mwparserfromhell

```



## Document Loader（文档加载器）


See a [usage example](../modules/indexes/document_loaders/examples/mediawikidump.ipynb).





```python

from langchain.document_loaders import MWDumpLoader

```

