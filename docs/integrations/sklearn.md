# scikit-learn

本页介绍如何在LangChain中使用scikit-learn包。
它分为两个部分:安装和设置，然后是对特定scikit-learn包装器的引用。

## 安装和设置

- 使用`pip install scikit-learn`安装Python包

## 包装器

### 向量存储

`SKLearnVectorStore`是最近邻实现的简单包装器
scikit-learn包，允许您将其用作向量存储。

要导入此向量存储，

```python
from langchain.vectorstores import SKLearnVectorStore

```


For a more detailed walkthrough of the SKLearnVectorStore wrapper, see [this notebook](../modules/indexes/vectorstores/examples/sklearn.ipynb).

