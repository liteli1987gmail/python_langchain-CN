# Google Cloud Storage 谷歌云存储


>[Google Cloud Storage](https://en.wikipedia.org/wiki/Google_Cloud_Storage) 是用于存储非结构化数据的托管服务。



## 安装和设置



首先，您需要安装 `google-cloud-bigquery` Python 包。



```bash

pip install google-cloud-storage

```



## 文档加载器



有两种 `Google Cloud Storage` 的加载器：`Directory` 和 `File` 加载器。



查看一个[使用示例](../modules/indexes/document_loaders/examples/google_cloud_storage_directory.ipynb)。



```python

from langchain.document_loaders import GCSDirectoryLoader

```

查看一个[使用示例](../modules/indexes/document_loaders/examples/google_cloud_storage_file.ipynb)。



```python

from langchain.document_loaders import GCSFileLoader

```

