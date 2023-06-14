Airbyte（数据一体化）


Airbyte是一个用于从API、数据库和文件到数据仓库和数据湖的ELT管道的数据一体化平台。具有最大的ELT连接器目录，可连接到数据仓库和数据库。
> databases & files to warehouses & lakes. It has the largest catalog of ELT connectors to data warehouses and databases.



安装和设置


此说明书介绍了如何将任何源从Airbyte加载到本地JSON文件中，并将其作为文档读入。


先决条件：
已安装Docker Desktop。


步骤：
1. 从GitHub克隆Airbyte - `git clone https://github.com/airbytehq/airbyte.git`。
2. 切换到Airbyte目录 - `cd airbyte`。
3. 启动Airbyte - `docker compose up`。
4. 在浏览器中访问 http://localhost:8000。您将被要求输入用户名和密码。默认情况下，用户名为`airbyte`，密码为`password`。
5. 设置任何您想要的源。
6. 将目的地设置为本地JSON，并指定目标路径 - 假设为`/json_data`。设置手动同步。
7. 运行连接。
8. 要查看生成的文件，请导航至：`file:///tmp/airbyte_local/`。


文档装载器


查看使用示例](../modules/indexes/document_loaders/examples/airbyte_json.ipynb)。


```python

from langchain.document_loaders import AirbyteJSONLoader

```

