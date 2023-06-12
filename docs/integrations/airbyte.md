# Airbyte


>[Airbyte](https://github.com/airbytehq/airbyte) 是一个用于将 API、数据库和文件集成到数据仓库和数据湖中的 ELT 管道的平台。它拥有目前最大的 ORS 连接器目录。
> databases & files to warehouses & lakes. It has the largest catalog of ELT connectors to data warehouses and databases.



## 安装和设置


本指南展示了如何将 `Airbyte` 中的任何源加载到本地 `JSON` 文件中，并将其作为文档读入。


**前提条件:**
已安装 `docker desktop`。


**步骤:**
1. 从 GitHub 上克隆 Airbyte - `git clone https://github.com/airbytehq/airbyte.git`。
2. 进入 Airbyte 目录 - `cd airbyte`。
3. 启动 Airbyte - `docker compose up`。
4. 在浏览器中访问 http://localhost:8000。您将被要求输入用户名和密码。默认情况下，用户名为 `airbyte`，密码为 `password`。
5. 设置您希望的任何源。
6. 将目的地设置为 `JSON`，并指定目标路径 - 假设为 `/json_data`。设置手动同步。
7. 运行连接。
8. 若要查看创建了哪些文件，请导航至 `file:///tmp/airbyte_local/`。


## 文档加载程序


请参见[用法示例](../modules/indexes/document_loaders/example/airbyte_json.ipynb)。


```python

from langchain.document_loaders import AirbyteJSONLoader

```

