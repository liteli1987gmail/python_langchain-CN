# Google Cloud Storage谷歌云存储


>[Google Cloud Storage](https://en.wikipedia.org/wiki/Google_Cloud_Storage) is a managed service for storing unstructured data.



## Installation and Setup安装和设置


First, you need to install `google-cloud-bigquery` python package.您需要首先安装 `google-cloud-bigquery` python包。


```bash

pip install google-cloud-storage

```



## Document Loader文档加载器


There are two loaders for the `Google Cloud Storage`: the `Directory` and the `File` loaders. `Google Cloud Storage` 有两种加载器，分别是 `Directory` 和 `File` 加载器。


See a [usage example](../modules/indexes/document_loaders/examples/google_cloud_storage_directory.ipynb). 参见 [用法示例](../modules/indexes/document_loaders/examples/google_cloud_storage_directory.ipynb)。


```python

from langchain.document_loaders import GCSDirectoryLoader

```

See a [usage example](../modules/indexes/document_loaders/examples/google_cloud_storage_file.ipynb).



```python

from langchain.document_loaders import GCSFileLoader

```

