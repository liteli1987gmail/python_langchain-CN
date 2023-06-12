# Arxiv


>[arXiv](https://arxiv.org/)是一个开放获取的档案，收录了在物理、数学、计算机科学、数量生物学、数量金融、统计学、电气工程和系统科学以及经济学领域中的两百万篇学术文章。,
> 数学, 计算机科学, 数量生物学, 数量金融, 统计学, 电气工程和
> 系统科学,和经济学。




## 安装和设置


首先，您需要安装“arxiv”Python包。


```bash

pip install arxiv

```



其次，您需要安装`PyMuPDF` python包，以将从`arxiv.org`网站下载的PDF文件转换为文本格式。


```bash

pip install pymupdf

```



## 文档加载器


请参阅[使用示例](../modules/indexes/document_loaders/examples/arxiv.ipynb)。


```python

from langchain.document_loaders import ArxivLoader

```



## 检索器


See a [usage example](../modules/indexes/retrievers/examples/arxiv.ipynb).



```python

from langchain.retrievers import ArxivRetriever

```

