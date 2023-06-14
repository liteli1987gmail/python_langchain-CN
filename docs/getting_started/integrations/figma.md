Figma


Figma是一个用于界面设计的协作网页应用。


安装和设置


Figma API需要访问令牌（access token），节点 ID（node_ids）和文件键（file key）


文件键（file key）可以从URL中获取。https://www.figma.com/file/{filekey}/sampleFilename


节点ID（Node IDs）也可以在URL中找到。点击任何元素，寻找 '?node-id={node_id}' 参数


访问令牌（Access token）说明](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens)


文档加载器


查看使用示例](../modules/indexes/document_loaders/examples/figma.ipynb)


```python

from langchain.document_loaders import FigmaFileLoader

```

