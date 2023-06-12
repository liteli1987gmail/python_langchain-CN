Vectara产品简介




Vectara是什么？


**Vectara概述:**
- Vectara是一个面向开发者的API平台，用于构建GenAI应用程序。
- 要使用Vectara-首先[注册](https://console.vectara.com/signup)并创建一个帐户。然后创建一个语料库和一个用于索引和搜索的API密钥。
- 您可以使用Vectara的索引API将文档添加到Vectara的索引中
- 您可以使用Vectara的搜索API查询Vectara索引(隐式支持混合搜索)。
- 您可以使用Vectara与LangChain的集成作为向量存储器或使用Retriever抽象。


## 安装和设置
要在LangChain中使用Vectara，不需要特殊的安装步骤。您只需提供Vectara控制台中创建的客户ID,语料库ID和API密钥，以启用索引和搜索。


或者，这些可以作为环境变量提供
- export `VECTARA_CUSTOMER_ID`=\"your_customer_id\"
- export `VECTARA_CORPUS_ID`=\"your_corpus_id\"
- export `VECTARA_API_KEY`=\"your-vectara-api-key\"


## 用法


### 向量存储器


存在一个Vectara平台的包装器，使您可以将其用作向量存储器，无论是用于语义搜索还是示例选择。


要导入此向量存储器:
```python
from langchain.vectorstores import Vectara

```

``` 
要创建Vectara向量存储器的实例:
```python
vectara = Vectara(

    vectara_customer_id=customer_id, 

    vectara_corpus_id=corpus_id, 

    vectara_api_key=api_key

)

```

The customer_id, corpus_id and api_key are optional, and if they are not supplied will be read from the environment variables `VECTARA_CUSTOMER_ID`, `VECTARA_CORPUS_ID` and `VECTARA_API_KEY`, respectively.

\u6211\u65e0\u8bed\u8868\u3002
\u4f60\u53ef\u4ee5\u4f7f\u7528`similarity_search`\u65b9\u6cd5\uff08\u6216`similarity_search_with_score`)\u67e5\u8be2\u5411\u91cf\u5b58\u50a8\u4e2d\u7684\u5411\u91cf\uff0c\u4e26\u8fd4\u56de\u4e00\u4e2a\u7ed3\u679c\u5217\u8868:\u3002
```python
results = vectara.similarity_score("what is LangChain?")

```


`similarity_search_with_score`\u8fd8\u652f\u6301\u4ee5\u4e0b\u4e09\u4e2a\u989d\u5916\u7684\u53c2\u6570:
- `k`\u8fd4\u56d5\u7684\u6570\u76ee\u4e2a\u6570\uff08\u9ed8\u8ba4\u4e3a5\uff09
- `lambda_val`\u4e2a[lexical matching](https://docs.vectara.com/docs/api-reference/search-apis/lexical-matching)\u56e0\u5b50\u4e3a\u578b\u5bf9\u4f4d\u7b26\u5408\u4f7f\u7528\uff0c\u9ed8\u8ba4\u4e3a0.025
- `filter`\u8fd4\u56de\u7684\u7ed1\u5b9a\u7ed3\u679c\u7684[filter](https://docs.vectara.com/docs/common-use-cases/filtering-by-metadata/filter-overview)\u4e0d\u5e26\u53c2\u6570\uff08\u9ed8\u8ba4\u4e3aNone\uff09
- `n_sentence_context`\u53cd\u5c04\u8fd4\u56de\u7ed3\u679c\u65f6\uff0c\u4f7f\u7528/\u63a5\u9762\u7684\u53d8\u91cf\u53d6\u5f97\u7edd\u5bf9\u5339\u914d\u6bb5\u524d/\u540e\u7684\u53d8\u91cf\u7684\u6570\u91cf\u3002\u9ed8\u8ba4\u8be5\u503c\u4e3a0\uff0c\u4ee5\u8fd4\u56de\u7b26\u5408\u7684\u4e00\u6bb5\uff0c\u4f46\u53ef\u4ee5\u4f7f\u7528\u5176\u4ed6\u503c\uff0c\u4f8b\u5982\u4ee5\u4e0b\u7684\u6570\u503c2\u62163\u8fd4\u56de\u76f8\u5173\u6587\u672c\u6bb5\u3002

\u7ed3\u679c\u8fd4\u56de\u4e3a\u4e00\u4e2a\u76f8\u5173\u6587\u6863\u7ed9\u51fa\u5173\u952e\u5b57\uff0c\u4ee5\u53ca\u6bcf\u4e2a\u6587\u6863\u7684\u76f8\u5173\u5ea6\u91cf\u3002


\u5176\u4ed6\u4f7f\u7528Vectara\u5305\u88c5\u7b80\u4ecb\uff0c\u53ef\u4ee5\u67e5\u770b\u4e0b\u9762\u4e24\u4e2a\u793a\u4f8bnotebook:
* [Chat Over Documents with Vectara](./vectara/vectara_chat.html)
* [Vectara Text Generation](./vectara/vectara_text_generation.html)



