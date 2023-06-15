# Psychic 心灵



>[Psychic](https://www.psychic.dev/) 是一个与 `Notion`, `Zendesk`, `Confluence` 和 `Google Drive` 等 SaaS 工具进行集成的平台，

>使用 OAuth 将这些应用程序的文档同步到您的 SQL 或向量数据库中。您可以将其视为非结构化数据的 Plaid.





## 安装和设置



```bash

pip install psychicapi

```



Psychic 很容易设置 - 您导入 `react` 库并使用您从 [Psychic 仪表板](https://dashboard.psychic.dev/) 获取的 `Sidekick API` 密钥进行配置。连接应用程序后，

您可以从仪表板中查看这些连接，并使用服务器端库检索数据。



 

1. 在 [仪表板](https://dashboard.psychic.dev/) 中创建一个帐户。

2. 使用 [react 库](https://docs.psychic.dev/sidekick-link) 向您的前端 React 应用程序添加 Psychic 链接模态框。您将使用此模态框连接 SaaS 应用程序。

3. 创建连接后，您可以使用 `PsychicLoader`，请参考 [示例笔记本](../modules/indexes/document_loaders/examples/psychic.ipynb)





## 与其他文档加载器相比的优势



1.	**通用 API：** 不需要构建每个 SaaS 应用的 OAuth 流程或了解其 API，只需集成 Psychic 并利用我们的通用 API 即可检索数据。

2.	**数据同步：** 客户的 SaaS 应用中的数据可能很快过期。使用 Psychic，您可以配置 Webhook 以按日或实时方式使文档保持最新。

3.	**简化的 OAuth：** Psychic 端到端处理 OAuth，因此您无需花时间为每个集成创建 OAuth 客户端，保持访问令牌的有效性以及处理 OAuth 重定向逻辑。
