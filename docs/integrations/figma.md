＃ Figma


> [Figma]（https : //www.figma.com/）是用于界面设计的协作Web应用程序。


## 安装和设置


Figma API需要`access token`,`node_ids`,和`file key`。


可以从URL获取`file key`。 https : //www.figma.com/file/{filekey}/sampleFilename


“节点ID”也可在URL中找到。单击任何内容并查找“？node-id ={node_id}”参数。


`Access token` [说明](https : //help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens)。


## 文档加载器


请参见[使用示例](../modules/indexes/document_loaders/examples/figma.ipynb)。


```python

from langchain.document_loaders import FigmaFileLoader

```

