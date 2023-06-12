# Beam{梁}


> [Beam{梁}](https://docs.beam.cloud/introduction) 使在GPU上运行代码，部署可扩展WEB API和计划cron jobs，执行大规模并行工作负载-无需管理任何基础设施。
> schedule cron jobs, and run massively parallel workloads — without managing any infrastructure.

 



## 安装和设置


- [创建一个账户](https://www.beam.cloud/)
- 使用`curl https://raw.githubusercontent.com/slai-labs/get-beam/main/get-beam.sh -sSfL | sh`安装Beam CLI
- 注册API密钥，使用`beam configure`
- 设置环境变量(`BEAM_CLIENT_ID`)和(`BEAM_CLIENT_SECRET`)
- 安装Beam SDK{软件开发工具包}:
```bash

pip install beam-sdk

```



## LLM{兰姆语言模型}




```python

from langchain.llms.beam import Beam

```



### Beam app{应用程序}的示例


这是你一旦开始应用程序开发时将使用的环境。它还用于定义从模型中返回的最大响应长度。
It's also used to define the maximum response length from the model.

```python

llm = Beam(model_name="gpt2",

           name="langchain-gpt2-test",

           cpu=8,

           memory="32Gi",

           gpu="A10G",

           python_version="python3.8",

           python_packages=[

               "diffusers[torch]>=0.10",

               "transformers",

               "torch",

               "pillow",

               "accelerate",

               "safetensors",

               "xformers",],

           max_length="50",

           verbose=False)

```



### Deploy the Beam app

### 部署Beam app
一旦定义，你可以通过调用模型的`_deploy()`方法来部署Beam应用程序。


```python

llm._deploy()

```



### 调用Beam app


一旦部署了Beam模型，,它可以通过调用模型的`_call()`方法来调用。这将返回GPT2文本响应到您的提示符。
This returns the GPT2 text response to your prompt.



```python

response = llm._call("Running machine learning on a remote GPU")

```



An example script which deploys the model and calls it would be:



```python

from langchain.llms.beam import Beam

import time



llm = Beam(model_name="gpt2",

           name="langchain-gpt2-test",

           cpu=8,

           memory="32Gi",

           gpu="A10G",

           python_version="python3.8",

           python_packages=[

               "diffusers[torch]>=0.10",

               "transformers",

               "torch",

               "pillow",

               "accelerate",

               "safetensors",

               "xformers",],

           max_length="50",

           verbose=False)



llm._deploy()



response = llm._call("Running machine learning on a remote GPU")



print(response)

```
