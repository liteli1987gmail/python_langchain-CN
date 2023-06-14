Arxiv(天狗)



>arXiv(天狗)](https://arxiv.org/)是一个开放获取的存档库，收录了200万篇涵盖物理学、

>数学、计算机科学、数量生物学、数量金融、统计学、电气工程、

>系统科学和经济学等领域的学术文章。





## 安装和设置



首先，您需要安装`arxiv` Python包。



```bash

pip install arxiv

```



其次，您需要安装`PyMuPDF` Python包，可将从`arxiv.org`站点下载的PDF文件转换为文本格式。



```bash

pip install pymupdf

```



## 文档加载器



请参阅使用示例](../modules/indexes/document_loaders/examples/arxiv.ipynb)。



```python

from langchain.document_loaders import ArxivLoader

```



## 检索器



请参阅使用示例](../modules/indexes/retrievers/examples/arxiv.ipynb)。



```python

from langchain.retrievers import ArxivRetriever

```

