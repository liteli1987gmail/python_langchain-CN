# RWKV-4



本页面介绍如何在LangChain中使用`RWKV-4`包装器。

分为两个部分：安装和设置，以及使用示例。



## 安装和设置

- 使用`pip install rwkv`命令安装Python包

- 使用`pip install tokenizer`命令安装tokenizer Python包

- 下载RWKV模型](https://huggingface.co/BlinkDL/rwkv-4-raven/tree/main)并将其放置在所需目录中

- 下载tokens文件](https://raw.githubusercontent.com/BlinkDL/ChatRWKV/main/20B_tokenizer.json)



## 使用方法



### RWKV



要使用RWKV包装器，您需要提供预训练模型文件的路径和tokenizer的配置。

```python

from langchain.llms import RWKV



# Test the model



```python



def generate_prompt(instruction, input=None):

    if input:

        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.



# Instruction:

{instruction}



# Input:

{input}



# Response:

"""

    else:

        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.



# Instruction:

{instruction}



# Response:

"""





model = RWKV(model="./models/RWKV-4-Raven-3B-v7-Eng-20230404-ctx4096.pth", strategy="cpu fp32", tokens_path="./rwkv/20B_tokenizer.json")

response = model(generate_prompt("Once upon a time, "))

```

## 模型文件



您可以在RWKV-4-Raven](https://huggingface.co/BlinkDL/rwkv-4-raven/tree/main)存储库中找到模型文件下载链接。



### Rwkv-4 models -> 推荐使用的VRAM





```

RWKV VRAM

模型 | 8位 | bf16/fp16 | fp32

14B   | 16GB | 28GB      | >50GB

7B    | 8GB  | 14GB      | 28GB

3B    | 2.8GB| 6GB       | 12GB

1b5   | 1.3GB| 3GB       | 6GB

```



有关策略（包括流式传输和cuda支持）的更多信息，请参阅rwkv pip](https://pypi.org/project/rwkv/)页面。

