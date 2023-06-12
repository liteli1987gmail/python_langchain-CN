
请在\"docs/integrations/arxiv.md\"参考一个示例。
使用此模板创建\"docs/integrations/\"中的新.md文件。

# 标题_REPLACE_ME

只允许一个标题/H1！

>
 

描述:阅读此描述后，读者应该决定是否足够好以尝试/跟随阅读或
阅读下一个整合文档。
描述应包含一个指向源的链接，以进行跟随阅读。

## 安装和设置

安装和设置:所有必要的附加程序包安装和设置令牌等

```bash
pip install package_name_REPLACE_ME

```


或者这个文本
它没有任何特殊的设置。


下一步H2/##部分，带有整合模块的名称，如\"LLM\"，\"文本嵌入模型\"，等等
请参阅\"index.html\"页面中的\"模块\"。
每个H2部分都应包括一个指向示例和导入整合类的Python代码的链接。
以下是几个示例部分。 删除所有不必要的部分。 添加所有必要的未在此处提供的部分。

## LLM

参见[使用示例](../modules/models/llms/integrations/INCLUDE_REAL_NAME.ipynb)。

```python
from langchain.llms import integration_class_REPLACE_ME

```



## 文本嵌入模型

参见[使用示例](../modules/models/text_embedding/examples/INCLUDE_REAL_NAME.ipynb)

```python
from langchain.embeddings import integration_class_REPLACE_ME

```



## 聊天模型

See a [usage example](../modules/models/chat/integrations/INCLUDE_REAL_NAME.ipynb)


```python
from langchain.chat_models import integration_class_REPLACE_ME

```


## 文档加载器（Document Loader）

参见 [使用示例](../modules/indexes/document_loaders/examples/INCLUDE_REAL_NAME.ipynb)。

```python

from langchain.document_loaders import integration_class_REPLACE_ME

```

