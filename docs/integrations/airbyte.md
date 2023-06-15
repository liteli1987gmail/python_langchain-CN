# Airbyte 本说明书的翻译


>[Airbyte](https://github.com/airbytehq/airbyte) 是一个用于从API、数据库和文件到数据仓库和数据湖的ELT管道的数据集成平台。

> 它拥有最大量的ELT连接器目录，可连接到数据仓库和数据库。



## 安装和设置



此指南展示了如何将 `Airbyte` 中的任何来源加载到一个本地的 `JSON` 文件中，以便作为一个文档进行阅读。



**先决条件:**

已安装 `Docker Desktop`。



**步骤:**

1. 从GitHub上克隆Airbyte - `git clone https://github.com/airbytehq/airbyte.git`。

2. 切换到Airbyte目录 - `cd airbyte`。

3. 启动Airbyte - `docker compose up`。

4. 在浏览器中访问 http://localhost:8000。您将被要求输入用户名和密码。默认用户名为 `airbyte`，密码为 `password`。

5. 设置任何您希望的数据来源。

6. 将目标设置为本地JSON，指定目标路径 - 假设为 `/json_data`。设置手动同步。

7. 运行连接。

8. 要查看创建的文件，请导航到：`file:///tmp/airbyte_local/`。



## 文档加载器



查看一个[使用示例](../modules/indexes/document_loaders/examples/airbyte_json.ipynb)。



```python

from langchain.document_loaders import AirbyteJSONLoader

```

