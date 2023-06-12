# 心灵感应

>[Psychic](https://www.psychic.dev/)是一个平台，可以通过OAuth与`Notion`、`Zendesk`、`Confluence`和`Google Drive`等SaaS工具进行集成，将这些应用程序中的文档同步到您的SQL或向量数据库中。您可以将其视为面向非结构化数据的Plaid。

## 安装和设置

```bash
Psychic很容易设置 - 您导入`react`库，并使用您获取的`Sidekick API`密钥对其进行配置，您可以从面板中查看这些连接并使用服务器端库检索数据。
1. 在[面板](https://dashboard.psychic.dev/)中创建帐户。
2. 使用[react库](https://docs.psychic.dev/sidekick-link)将Psychic链接模态框添加到您的前端React应用程序中。您将使用此选项连接SaaS应用程序。
3. 创建连接后，您可以依照[示例笔记本](../modules/indexes/document_loaders/examples/psychic.ipynb)使用`PsychicLoader`

## 其他文档加载器的优势

1.\t**通用API:**：与为每个SaaS应用程序构建OAuth流程和学习API不同，您只需集成一次Psychic，即可利用我们的通用API检索数据。
2.\t**数据同步:**：您客户的SaaS应用程序中的数据可能很快就会变得过时。使用Psychic，您可以配置Webhooks以使您的文档每天或实时更新。
1. Create an account in the [dashboard](https://dashboard.psychic.dev/).

2. Use the [react library](https://docs.psychic.dev/sidekick-link) to add the Psychic link modal to your frontend react app. You will use this to connect the SaaS apps.

3. Once you have created a connection, you can use the `PsychicLoader` by following the [example notebook](../modules/indexes/document_loaders/examples/psychic.ipynb)





## Advantages vs Other Document Loaders



1.	**Universal API:** Instead of building OAuth flows and learning the APIs for every SaaS app, you integrate Psychic once and leverage our universal API to retrieve data.

2.	**Data Syncs:** Data in your customers' SaaS apps can get stale fast. With Psychic you can configure webhooks to keep your documents up to date on a daily or realtime basis.

3.	**Simplified OAuth:** Psychic handles OAuth end-to-end so that you don't have to spend time creating OAuth clients for each integration, keeping access tokens fresh, and handling OAuth redirect logic.
