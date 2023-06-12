# Modal


本页介绍如何在LangChain中使用Modal生态系统。
它被分为两个部分：安装和设置以及参考特定的Modal封装。


## 安装和设置
- 使用`pip install modal-client`进行安装
- 运行`modal token new`


## 定义Modal函数和Webhooks


您必须包含提示。有一个严格的响应结构。


```python

class Item(BaseModel):

    prompt: str



:stub.webhook(method="POST")

def my_webhook(item: Item):

    return {"prompt": my_function.call(item.prompt)}

```



一个使用GPT2的示例:


```python

from pydantic import BaseModel



import modal



stub = modal.Stub("example-get-started")



volume = modal.SharedVolume().persist("gpt2_model_vol")

CACHE_PATH = "/root/model_cache"



:stub.function(

    gpu="any",

    image=modal.Image.debian_slim().pip_install(

        "tokenizers", "transformers", "torch", "accelerate"

    ),

    shared_volumes={CACHE_PATH: volume},

    retries=3,

)

def run_gpt2(text: str):

    from transformers import GPT2Tokenizer, GPT2LMHeadModel

    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    model = GPT2LMHeadModel.from_pretrained('gpt2')

    encoded_input = tokenizer(text, return_tensors='pt').input_ids

    output = model.generate(encoded_input, max_length=50, do_sample=True)

    return tokenizer.decode(output[0], skip_special_tokens=True)



class Item(BaseModel):

    prompt: str



:stub.webhook(method="POST")

def get_text(item: Item):

    return {"prompt": run_gpt2.call(item.prompt)}

```



## 封装


### LLM


There exists an Modal LLM wrapper, which you can access with 

```python

from langchain.llms import Modal

```
