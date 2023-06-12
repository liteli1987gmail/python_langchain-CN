# Confluence（协同编辑）

>[Confluence](https://www.atlassian.com/software/confluence)是一款维护并组织项目相关材料的协同编辑平台。`Confluence`主要用于内容管理。


## 安装和设置

```bash
pip install atlassian-python-api

```


我们需要设置 `用户名/API密钥` 或 `Oauth2 登录` 。备注: We need to set up `username/api_key` or `Oauth2 login`. 
请参阅[说明](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)。备注: See [instructions](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).


## 文档加载器

请参阅[使用示例](../modules/indexes/document_loaders/examples/confluence.ipynb)。备注: See a [usage example](../modules/indexes/document_loaders/examples/confluence.ipynb).

```python

from langchain.document_loaders import ConfluenceLoader

```

