页隄稑板斐示协议



Shale Protocol](https://shaleprotocol.com) 提供了面向开放LLMs的生产就绪推理API。由于其托管在高度可扩展的GPU云基础架构上，它是一个即插即用的API。



我们的免费版本支持每个密钥每天多达1K个请求，因为我们希望消除任何人开始构建带有LLMs的genAI应用的障碍。



在Shale Protocol的帮助下，开发人员/研究人员可以免费创建应用程序并探索开放LLMs的功能。



本页面介绍了如何将Shale-Serve API与LangChain结合使用。



截至2023年6月，该API默认支持Vicuna-13B。我们计划在未来的版本中支持更多的LLMs，如Falcon-40B。





## 如何



### 1. 在 https://shaleprotocol.com 上查找我们的Discord链接。通过我们的Discord上的"Shale Bot"生成API密钥。不需要信用卡，也没有免费试用。每个API密钥每天有1K的永久免费配额。



### 2. 使用 https://shale.live/v1 作为OpenAI API的替代。



例如

```python

from langchain.llms import OpenAI

from langchain import PromptTemplate, LLMChain



import os

os.environ['OPENAI_API_BASE'] = "https://shale.live/v1"

os.environ['OPENAI_API_KEY'] = "ENTER YOUR API KEY"



llm = OpenAI()



template = """Question: {question}



# Answer: Let's think step by step."""



prompt = PromptTemplate(template=template, input_variables=["question"])



llm_chain = LLMChain(prompt=prompt, llm=llm)



question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"



llm_chain.run(question)



```

