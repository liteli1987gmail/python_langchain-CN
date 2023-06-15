# 香蕉



本页面介绍如何在LangChain内使用香蕉生态系统。

它分为两部分：安装和设置，以及特定香蕉包装器的参考。



## 安装和设置



- 使用 `pip install banana-dev` 进行安装

- 获取一个香蕉 API 密钥，并将其设置为环境变量 (`BANANA_API_KEY`)



## 定义你的香蕉模板



如果您想使用现有的语言模型模板，您可以在[这里](https://app.banana.dev/templates/conceptofmind/serverless-template-palmyra-base)找到一个。

此模板使用 [Writer](https://writer.com/product/api/) 的 Palmyra-Base 模型。

您可以在[这里](https://github.com/conceptofmind/serverless-template-palmyra-base)查看一个示例香蕉代码仓库。



## 构建香蕉应用



香蕉应用程序必须在返回的 JSON 中包含 "output" 键。

有一个固定的响应结构。



```python

# 将结果作为字典返回

result = {'output': result}

```



推理函数的示例可以是：



```python

def 推理(model_inputs:dict) -> dict:

    global model

    global tokenizer



    # 解析参数

    prompt = model_inputs.get('prompt', None)

    if prompt == None:

        return {'message': "未提供提示"}



    # 运行模型

    input_ids = tokenizer.encode(prompt, return_tensors='pt').cuda()

    output = model.generate(

        input_ids,

        max_length=100,

        do_sample=True,

        top_k=50,

        top_p=0.95,

        num_return_sequences=1,

        temperature=0.9,

        early_stopping=True,

        no_repeat_ngram_size=3,

        num_beams=5,

        length_penalty=1.5,

        repetition_penalty=1.5,

        bad_words_ids=[[tokenizer.encode(' ', add_prefix_space=True)[0]]]

        )



    result = tokenizer.decode(output[0], skip_special_tokens=True)

    # 将结果作为字典返回

    result = {'output': result}

    return result

```



您可以在[这里](https://github.com/conceptofmind/serverless-template-palmyra-base/blob/main/app.py)找到一个完整的香蕉应用示例。



## 包装器



### LLM



存在一个香蕉 LLM 包装器，您可以使用以下方式访问



```python

from langchain.llms import Banana

```



您需要提供位于仪表板中的模型密钥：



```python

llm = Banana(model_key="YOUR_MODEL_KEY")

```

