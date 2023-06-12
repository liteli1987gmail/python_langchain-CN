# 谷歌云盘


>[谷歌云盘](https://zh.wikipedia.org/wiki/谷歌云端硬盘) 是由谷歌开发的文件存储和同步服务。


目前只支持 `谷歌文档`。


## 安装与设置


首先，您需要安装几个Python包。


```bash

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

```



## 文档加载器


See a [usage example and authorizing instructions](../modules/indexes/document_loaders/examples/google_drive.ipynb).





```python

from langchain.document_loaders import GoogleDriveLoader

```

