媒体维基百科转储


【MediaWiki XML转储】(https://www.mediawiki.org/wiki/Manual:Importing_XML_dumps)包含了维基百科的内容
（包括所有修订版本的维基页面），但不包含与网站相关的数据。XML转储不会创建完整的备份
维基数据库的完整备份不会包含用户帐户、图像、编辑日志等。




安装和设置


我们需要安装几个Python包。


`mediawiki-utilities`在未合并的分支中支持XML模式0.11。
```bash

pip install -qU git+https://github.com/mediawiki-utilities/python-mwtypes@updates_schema_0.11
```



`mediawiki-utilities mwxml`存在一个错误，修复正在等待中。


```bash

pip install -qU git+https://github.com/gdedrouas/python-mwxml@xml_format_0.11
pip install -qU mwparserfromhell
```



文档加载器


查看用法示例](../modules/indexes/document_loaders/examples/mediawikidump.ipynb)




```python

from langchain.document_loaders import MWDumpLoader

```

