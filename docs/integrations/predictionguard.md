# 预测保护



>[预测保护](https://docs.predictionguard.com/)提供了一种快速简便的方法，可以使用最先进的开放和封闭访问LLMs，无需花费数天或数周来理解所有实现细节，管理大量不同的API规范，并设置模型部署的基础设施。





## 安装和设置

- 安装Python SDK：

```bash

pip install predictionguard

```



- 获取预测保护的访问令牌（请参见[这里](https://docs.predictionguard.com/)）并将其设置为环境变量（`PREDICTIONGUARD_TOKEN`）



## LLM



```python

from langchain.llms import PredictionGuard

```



### 示例

当初始化LLM时，您可以将Prediction Guard模型的名称作为参数提供：

```python

pgllm = PredictionGuard(model="MPT-7B-Instruct")

```



您还可以直接提供访问令牌作为参数：

```python

pgllm = PredictionGuard(model="MPT-7B-Instruct", token="<your access token>")

```



此外，您可以提供一个“output”参数，用于结构化/控制LLM的输出：

```python

pgllm = PredictionGuard(model="MPT-7B-Instruct", output={"type": "boolean"})

```



#### 控制或受保护的LLM的基本用法：

```python

import os



import predictionguard as pg

from langchain.llms import PredictionGuard

from langchain import PromptTemplate, LLMChain



# Your Prediction Guard API key. Get one at predictionguard.com

os.environ["PREDICTIONGUARD_TOKEN"] = "<your Prediction Guard access token>"



# Define a prompt template

template = """Respond to the following query based on the context.



Context: EVERY comment, DM + email suggestion has led us to this EXCITING announcement! 🎉 We have officially added TWO new candle subscription box options! 📦

Exclusive Candle Box - $80 

Monthly Candle Box - $45 (NEW!)

Scent of The Month Box - $28 (NEW!)

Head to stories to get ALLL the deets on each box! 👆 BONUS: Save 50% on your first box with code 50OFF! 🎉



Query: {query}



Result: """

prompt = PromptTemplate(template=template, input_variables=["query"])



# With "guarding" or controlling the output of the LLM. See the 

# Prediction Guard docs (https://docs.predictionguard.com) to learn how to 

# control the output with integer, float, boolean, JSON, and other types and

# structures.

pgllm = PredictionGuard(model="MPT-7B-Instruct", 

                        output={

                                "type": "categorical",

                                "categories": [

                                    "product announcement", 

                                    "apology", 

                                    "relational"

                                    ]

                                })

pgllm(prompt.format(query="What kind of post is this?"))

```



#### Prediction Guard的基本LLM链接：

```python

import os



from langchain import PromptTemplate, LLMChain

from langchain.llms import PredictionGuard



# Optional, add your OpenAI API Key. This is optional, as Prediction Guard allows

# you to access all the latest open access models (see https://docs.predictionguard.com)

os.environ["OPENAI_API_KEY"] = "<your OpenAI api key>"



# Your Prediction Guard API key. Get one at predictionguard.com

os.environ["PREDICTIONGUARD_TOKEN"] = "<your Prediction Guard access token>"



pgllm = PredictionGuard(model="OpenAI-text-davinci-003")



template = """Question: {question}



Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=pgllm, verbose=True)



question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"



llm_chain.predict(question=question)

```
