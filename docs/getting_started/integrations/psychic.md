心灵感应


Psychic是与Notion、Zendesk、Confluence和Google Drive等SaaS工具集成的平台，通过OAuth将这些应用程序中的文档同步到您的SQL或矢量数据库中。您可以将其看作是用于非结构化数据的Plaid。
> `Confluence`, and `Google Drive` via OAuth and syncing documents from these applications to your SQL or vector

> database. You can think of it like Plaid for unstructured data. 



安装和设置


```bash

pip install psychicapi
```



Psychic的设置很简单-您导入react库并使用您从Psychic仪表板获取的Sidekick API密钥进行配置。连接应用程序时，您可以从仪表板查看这些连接，并使用服务器端库检索数据。
from the [Psychic dashboard](https://dashboard.psychic.dev/). When you connect the applications, you  

view these connections from the dashboard and retrieve data using the server-side libraries.

 

1. 在仪表板](https://dashboard.psychic.dev/)上创建帐户。
2. 使用react库](https://docs.psychic.dev/sidekick-link)将Psychic链接模态框添加到您的前端React应用程序中。您将使用它来连接SaaS应用程序。
3. 创建连接后，您可以按照示例笔记本](../modules/indexes/document_loaders/examples/psychic.ipynb)中的步骤使用PsychicLoader。




与其他文档加载器相比的优点


1. 通用API: 您只需集成Psychic一次并利用我们的通用API检索数据，而无需构建OAuth流程和学习每个SaaS应用的API。
2. 数据同步: 您客户的SaaS应用中的数据可能会很快过时。使用Psychic，您可以配置Webhooks以使您的文档每天或实时保持最新状态。
3. 简化的OAuth: Psychic自动处理OAuth的全部流程，因此您无需花时间为每个集成创建OAuth客户端、保持访问令牌的新鲜和处理OAuth重定向逻辑。
