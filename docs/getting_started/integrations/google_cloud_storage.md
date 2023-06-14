Google Cloud Storage（谷歌云存储）#


Google Cloud Storage（谷歌云存储）是用于存储非结构化数据的托管服务。#


安装和设置#


首先，您需要安装 `google-cloud-bigquery` Python 包。#


```bash

pip install google-cloud-storage#
```



文档加载器#


谷歌云存储有两种加载器：`目录` 和 `文件` 加载器。#


请参见 使用示例](../modules/indexes/document_loaders/examples/google_cloud_storage_directory.ipynb)。#


```python

from langchain.document_loaders import GCSDirectoryLoader

```

请参见 使用示例](../modules/indexes/document_loaders/examples/google_cloud_storage_file.ipynb)。#


```python

from langchain.document_loaders import GCSFileLoader

```

