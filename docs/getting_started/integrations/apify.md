Apify是一个云平台，用于网页抓取和数据提取。


本页介绍了在LangChain中如何使用Apify。


概述


Apify是一个提供超过一千个准备好的应用程序（称为*Actors*）的生态系统，用于各种网页抓取、爬取和数据提取用例。
which provides an [ecosystem](https://apify.com/store) of more than a thousand

ready-made apps called *Actors* for various scraping, crawling, and extraction use cases.



!Apify Actors](../_static/ApifyActors.png)](https://apify.com/store)


此集成使您能够在Apify平台上运行Actors，并将它们的结果加载到LangChain中，以从网页中提取文档和数据，例如从带有文档的网站生成答案、博客或知识库。
indexes with documents and data from the web, e.g. to generate answers from websites with documentation,

blogs, or knowledge bases.





安装和设置


- 使用`pip install apify-client`安装Python的Apify API客户端
- 获取您的Apify API令牌](https://console.apify.com/account/integrations)，然后将其设置为环境变量(`APIFY_API_TOKEN`)或在构造函数中将其传递给`ApifyWrapper`作为`apify_api_token`。
  an environment variable (`APIFY_API_TOKEN`) or pass it to the `ApifyWrapper` as `apify_api_token` in the constructor.





包装器


工具


您可以使用`ApifyWrapper`在Apify平台上运行Actors。


```python

from langchain.utilities import ApifyWrapper

```



要详细了解此包装器，请参阅此笔记本](../modules/agents/tools/examples/apify.ipynb)。




加载器


您也可以使用我们的`ApifyDatasetLoader`从Apify数据集中获取数据。


```python

from langchain.document_loaders import ApifyDatasetLoader

```



要详细了解此加载器，请参阅此笔记本](../modules/indexes/document_loaders/examples/apify_dataset.ipynb)。
