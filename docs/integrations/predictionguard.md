预测守卫 predictionguard


>[预测守卫](https://docs.predictionguard.com/)提供了一种快速简便的方法，可以访问最先进的开放和封闭访问LLM，而无需花费几天甚至几周来弄清所有实现细节、管理一堆不同的API规范以及设置模型部署的基础设施。





## 安装和设置

- 安装Python SDK：

```bash

pip install predictionguard

```



- 获取预测守卫访问令牌（如[此处](https://docs.predictionguard.com/)所述），并将其设置为环境变量（`PREDICTIONGUARD_TOKEN`）



## LLM 



```python

从langchain.llms导入PredictionGuard

```



### 示例

在初始化LLM时，您可以提供预测守卫模型的名称作为参数：

```python

pgllm = PredictionGuard(model="MPT-7B-Instruct")

```



您还可以直接提供访问令牌作为参数：

```python

pgllm = PredictionGuard(model="MPT-7B-Instruct", token="<your access token>")

```



此外，您可以提供一个"output"参数来结构化/控制LLM的输出：

```python

pgllm = PredictionGuard(model="MPT-7B-Instruct", output={"type": "boolean"})

```



#### 控制或保护LLM的基本使用：

```python

导入os



导入predictionguard as pg

从langchain.llms导入PredictionGuard

从langchain导入PromptTemplate, LLMChain



# 您的预测守卫API密钥。在predictionguard.com上获取一个

os.environ["PREDICTIONGUARD_TOKEN"] = "<your Prediction Guard access token>"



# 定义一个提示模板

template = """基于上下文回答以下查询。



上下文：每个评论、私信+电子邮件建议都引导我们作出令人兴奋的宣布！ 🎉 我们正式添加了两个新的蜡烛订阅盒选项！ 📦

独家蜡烛盒 - $80 

月度蜡烛盒 - $45（新！）

本月之香盒 - $28（新！）

点击故事以了解有关每个盒子的所有详情！ 👆 奖励：使用50OFF代码节省首个盒子的50%! 🎉



查询：{query}



结果："""

prompt = PromptTemplate(template=template, input_variables=["query"])



# 使用"guarding"或控制LLM的输出。请参阅

# 预测守卫文档（https://docs.predictionguard.com）以了解如何

# 使用整数、浮点数、布尔类型、JSON和其他类型和结构来控制输出。

# structures.

pgllm = PredictionGuard(model="MPT-7B-Instruct", 

                        output={

                                "type": "categorical",

                                "categories": [

                                    "产品公告", 

                                    "道歉", 

                                    "关系"

                                    ]

                                })

pgllm(prompt.format(query="这是什么类型的帖子？"))

```



#### 使用预测守卫进行基本的LLM链式操作：

```python

导入os



从langchain导入PromptTemplate, LLMChain

从langchain.llms导入PredictionGuard



# 可选项，添加您的OpenAI API密钥。这是可选的，因为预测守卫允许

# 您访问所有最新的开放访问模型（请参见https://docs.predictionguard.com）

os.environ["OPENAI_API_KEY"] = "<your OpenAI api key>"



# 您的预测守卫API密钥。在predictionguard.com上获取一个

os.environ["PREDICTIONGUARD_TOKEN"] = "<your Prediction Guard access token>"



pgllm = PredictionGuard(model="OpenAI-text-davinci-003")



template = """问题：{question}



回答：让我们逐步思考。"""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=pgllm, verbose=True)



question = "贾斯汀·比伯出生的那一年，哪个NFL球队赢得了超级碗？"



llm_chain.predict(question=question)

```
