# Figma画板



> [Figma](https://www.figma.com/) 是一个用于界面设计的协作性网络应用。



## 安装和设置



Figma API需要一个`访问令牌`，`节点ID`和一个`文件键`。



`文件键`可以从URL中获取。https://www.figma.com/file/{文件键}/示例文件名



`节点ID`也可以在URL中找到。点击任何内容并寻找'?node-id={节点ID}'参数。



`访问令牌`的使用说明请参阅[此处](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens)。



## 文档加载器



查看[使用示例](../modules/indexes/document_loaders/examples/figma.ipynb)。



```python

from langchain.document_loaders import FigmaFileLoader

```

