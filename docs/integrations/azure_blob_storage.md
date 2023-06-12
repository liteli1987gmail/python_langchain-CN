# Azure Blob Storage（Azure 块 Blob 存储）

>[Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) 是 Microsoft 提供的云端对象存储解决方案。Blob Storage 专为存储大量非结构化数据而优化。非结构化数据是指不符合特定数据模型或定义的数据，例如文本或二进制数据。

>[Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction) 提供完全托管的云端文件共享，可以通过行业标准 Server Message Block (SMB) 协议、Network File System (NFS) 协议和 Azure Files REST API 访问。Azure Files 基于 Azure Blob Storage。

`Azure Blob Storage` 适用于:
- 直接向浏览器提供图像或文档。
- 存储分布式访问的文件。
- 流式传输视频和音频。
- 编写日志文件。
- 存储数据以备份和恢复、灾难恢复、归档等用途。
- 存储数据以供本地或 Azure 托管的服务分析使用。

## 安装和设置

```bash

`Azure Blob Storage` 的使用示例请参见：../modules/indexes/document_loaders/examples/azure_blob_storage_container.ipynb。

```python


## 文档加载器

`Azure Files` 的使用示例请参见：../modules/indexes/document_loaders/examples/azure_blob_storage_file.ipynb。

```python





```python

from langchain.document_loaders import AzureBlobStorageFileLoader

```

