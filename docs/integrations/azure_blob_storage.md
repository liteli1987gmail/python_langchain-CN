# Azure Blob Storage



Azure Blob Storage是Microsoft在云中的对象存储解决方案。Blob Storage被优化用于存储大量的非结构化数据。非结构化数据是指不符合特定数据模型或定义的数据，例如文本或二进制数据。



Azure Files在云中提供完全托管的文件共享，可以通过行业标准的Server Message Block（SMB）协议、Network File System（NFS）协议和Azure Files REST API进行访问。Azure Files基于Azure Blob Storage。

> file shares in the cloud that are accessible via the industry standard Server Message Block (`SMB`) protocol, 

> Network File System (`NFS`) protocol, and `Azure Files REST API`. `Azure Files` are based on the `Azure Blob Storage`.



Azure Blob Storage的设计目标包括：
- 直接向浏览器提供图像或文档。
- 存储用于分布式访问的文件。
- 流式传输视频和音频。
- 写入日志文件。
- 存储备份和恢复、灾难恢复和归档的数据。
- 存储供本地部署或Azure托管服务分析的数据。


## 安装和设置



```bash

pip install azure-storage-blob

```





## 文档加载器



查看Azure Blob Storage的使用示例[../modules/indexes/document_loaders/examples/azure_blob_storage_container.ipynb]。



```python

from langchain.document_loaders import AzureBlobStorageContainerLoader

```



查看Azure Files的使用示例[../modules/indexes/document_loaders/examples/azure_blob_storage_file.ipynb]。



```python

from langchain.document_loaders import AzureBlobStorageFileLoader

```

