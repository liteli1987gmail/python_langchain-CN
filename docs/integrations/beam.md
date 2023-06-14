梁



Beam](https://docs.beam.cloud/introduction)使在GPU上运行代码、部署可扩展的Web API

>计划cron作业，并运行大规模并行工作负载-无需管理任何基础设施。

 



安装和设置



-创建一个帐户](https://www.beam.cloud/)

-使用`curl https://raw.githubusercontent.com/slai-labs/get-beam/main/get-beam.sh -sSfL | sh` 安装Beam CLI

-使用`beam configure`注册API密钥

-设置环境变量(`BEAM_CLIENT_ID`)和(`BEAM_CLIENT_SECRET`)

-安装Beam SDK:

```bash

pip安装Beam SDK

```



LLM





```python

from langchain.llms.beam import Beam

```



Beam应用程序示例



这是您开始应用程序后将要开发的环境。

它还用于定义来自模型的最大响应长度。

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



部署Beam应用程序



一旦定义，您可以通过调用模型的`_deploy()`方法来部署Beam应用程序。



```python

llm._deploy()

```



调用Beam应用程序



一旦Beam模型被部署，可以通过调用模型的`_call()`方法来调用它。

这将返回对您的提示的GPT2文本响应。



```python

response = llm._call("Running machine learning on a remote GPU")

```



部署模型并调用它的示例脚本如下：



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
