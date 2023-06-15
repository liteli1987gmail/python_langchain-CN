# 复制 Replicate模型
本页介绍如何在LangChain中运行Replicate模型。

## 安装和设置
- 创建[Replicate](https://replicate.com)账户。获取API密钥并将其设置为环境变量(`REPLICATE_API_TOKEN`)
- 使用`pip install replicate`安装[Replicate Python客户端](https://github.com/replicate/replicate-python)

## 调用模型

在[Replicate探索页面](https://replicate.com/explore)上找到一个模型，然后按照以下格式粘贴模型名称和版本：`owner-name/model-name:version`

例如，对于这个[dolly模型](https://replicate.com/replicate/dolly-v2-12b)，点击API选项卡。 模型名称/版本将为：`"replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5"`

只有`model`参数是必需的，但也可以使用`input={model_param: value, ...}`的格式传递任何其他模型参数


例如，如果我们运行稳定扩散并希望更改图像尺寸：

```

Replicate(model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", input={'image_dimensions': '512x512'})
```


*请注意，只会返回模型的第一个输出*
从这里，我们可以初始化我们的模型：

```python

llm = Replicate(model="replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5")
```


然后运行它：

```python

prompt = """
回答以下问题：通过逐步推理回答是或否。
狗能开车吗？
"""

llm(prompt)
Can a dog drive a car?

"""

llm(prompt)

```


我们可以使用此语法调用任何Replicate模型（不仅仅是LLMs）。例如，我们可以调用[Stable Diffusion](https://replicate.com/stability-ai/stable-diffusion)：

```python

text2image = Replicate(model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", input={'image_dimensions':'512x512'})

image_output = text2image("A cat riding a motorcycle by Picasso")
```

