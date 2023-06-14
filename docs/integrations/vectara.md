Vectara




Vectara是什么？


Vectara概述：
- Vectara是一款针对开发者的API平台，用于构建GenAI应用程序
- 要使用Vectara - 首先注册](https://console.vectara.com/signup)并创建一个账户。然后创建语料库和用于索引和搜索的API密钥。
- 您可以使用Vectara的索引API](https://docs.vectara.com/docs/indexing-apis/indexing)将文档添加到Vectara的索引中
- 您可以使用Vectara的搜索API](https://docs.vectara.com/docs/search-apis/search)查询Vectara的索引（还隐式支持混合搜索）
- 您可以使用LangChain与Vectara集成作为向量存储或使用Retriever抽象


安装和设置
使用Vectara与LangChain不需要特殊的安装步骤。您只需要提供在Vectara控制台中创建的customer_id，corpus ID和API密钥，以启用索引和搜索。


或者您可以提供这些作为环境变量
- export `VECTARA_CUSTOMER_ID`="your_customer_id"
- export `VECTARA_CORPUS_ID`="your_corpus_id"
- export `VECTARA_API_KEY`="your-vectara-api-key"


使用


VectorStore


存在一个围绕Vectara平台的包装，允许您将其用作向量存储，无论是用于语义搜索还是示例选择


要导入此向量存储
```python

from langchain.vectorstores import Vectara

```



要创建Vectara向量存储的实例
```python

vectara = Vectara(

    vectara_customer_id=customer_id, 

    vectara_corpus_id=corpus_id, 

    vectara_api_key=api_key

)

```

customer_id，corpus_id和api_key是可选的，如果未提供它们，将从环境变量`VECTARA_CUSTOMER_ID`，`VECTARA_CORPUS_ID`和`VECTARA_API_KEY`中读取


要查询向量存储，可以使用`similarity_search`方法（或`similarity_search_with_score`），它接受一个查询字符串并返回结果列表
```python

results = vectara.similarity_score("what is LangChain?")

```



`similarity_search_with_score`还支持以下附加参数
- `k`：要返回的结果数（默认为5）
- `lambda_val`：混合搜索的词汇匹配](https://docs.vectara.com/docs/api-reference/search-apis/lexical-matching)因子（默认为0.025）
- `filter`：要应用于结果的过滤器](https://docs.vectara.com/docs/common-use-cases/filtering-by-metadata/filter-overview)（默认为None）
- `n_sentence_context`：在返回结果时包括实际匹配片段之前/之后的句子数。默认为0，以返回精确匹配的文本片段，但可以与其他值（例如2或3）一起使用，以返回相邻的文本片段


结果以相关文档的列表和每个文档的相关分数返回


若要了解更详细的使用Vectara包装器的示例，请参阅以下两个示例笔记本之一：
For a more detailed examples of using the Vectara wrapper, see one of these two sample notebooks:

* Chat Over Documents with Vectara](./vectara/vectara_chat.html)
* Vectara Text Generation](./vectara/vectara_text_generation.html)




