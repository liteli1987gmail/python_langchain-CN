# RWKV-4

本页包含如何在LangChain中使用`RWKV-4`包装器的说明。
它分为两部分:安装和设置以及使用示例。

## 安装和设置
- 使用`pip install rwkv`安装Python包
- 使用`pip install tokenizer`安装分词器Python包
- 下载[RWKV模型](https://huggingface.co/BlinkDL/rwkv-4-raven/tree/main)并将其放置在您想要的目录中
- 下载[tokens文件](https://raw.githubusercontent.com/BlinkDL/ChatRWKV/main/20B_tokenizer.json)

## 使用方法

### RWKV

要使用RWKV包装器，您需要提供预训练模型文件的路径和分词器的配置。
```python
from langchain.llms import RWKV



# Test the model



```python


def generate_prompt(instruction, input=None):
    if input:

        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.


# 指令:
{指令}

# 输入:
{输入}

# 响应:
\"\"\"
    else:

        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.


# 指令:
{指令}

# 响应:
\"\"\"


model = RWKV(model=\"./models/RWKV-4-Raven-3B-v7-Eng-20230404-ctx4096.pth\", strategy=\"cpu fp32\", tokens_path=\"./rwkv/20B_tokenizer.json\")
response = model(generate_prompt(\"从前有个人, \"))
```
## Model File



You can find links to model file downloads at the [RWKV-4-Raven](https://huggingface.co/BlinkDL/rwkv-4-raven/tree/main) repository.



### Rwkv-4 models -> recommended VRAM





```

RWKV VRAM
模型 | 8位 | bf16/fp16 | fp32
14B  | 16GB | 28GB      | >50GB
7B   | 8GB  | 14GB      | 28GB
3B   | 2.8GB| 6GB       | 12GB
1b5  | 1.3GB| 3GB       | 6GB
```



See the [rwkv pip](https://pypi.org/project/rwkv/) page for more information about strategies, including streaming and cuda support.

