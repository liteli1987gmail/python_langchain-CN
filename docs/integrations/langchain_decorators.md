# LangChain装饰器 ✨（LangChain Decorators ✨）

lanchchain装饰器是在LangChain之上提供的一层，为编写自定义的langchain提示和链式交互提供了语法糖🍭。

如有任何反馈、问题或贡献，请在这里提出：
ju-bezdek/langchain-decorators](https://github.com/ju-bezdek/langchain-decorators)



主要原则和优势：

- 更酷的编程方式
- 编写多行提示而无需打破代码流程和缩进
- 利用IDE内置的支持进行**提示**、**类型检查**和**弹出文档**，以快速查看函数的提示、参数等
- 充分利用🦜🔗 LangChain 生态系统的所有功能
- 支持**可选参数**
- 通过将参数绑定到一个类来轻松共享提示之间的参数



下面是使用**LangChain装饰器 ✨**编写的一个简单示例代码

``` python


@llm_prompt（提供装饰器llm_prompt）
def write_me_short_post（topic：str，platform：str = "twitter"，audience：str = "developers"）-> str：
    """
    为我在{platform}平台上关于{topic}的帖子写一个简短的标题。
    它应该是针对{audience}受众的。
    （最多15个字）
    """
    返回

# 自然运行
write_me_short_post（topic="starwars"）
# 或
write_me_short_post（topic="starwars"，platform="redit"）
```


# 快速开始
## 安装
```bash

pip install langchain_decorators
```


## 示例

从这里查看示例的好方法：
 - jupyter notebook](https://github.com/ju-bezdek/langchain-decorators/blob/main/example_notebook.ipynb)
 - colab notebook](https://colab.research.google.com/drive/1no-8WfeP6JaLD9yUtkPgym6x0G9ZYZOG#scrollTo=N4cf__D0E2Yk)

# 定义其他参数
在此处，我们只是使用`llm_prompt`装饰器将函数标记为提示符，将其有效地转换为LLMChain。而不是运行它


标准LLMchain的初始化参数比仅仅输入变量和提示符要多得多...这个实现细节在装饰器中隐藏起来。
以下是它的工作原理：

1. 使用**全局设置**：

``` python

# 为所有提示符定义全局设置（如果未设置，则chatGPT是当前默认设置）
from langchain_decorators import GlobalSettings

GlobalSettings.define_settings(
    default_llm=ChatOpenAI(temperature=0.0)，这是默认设置...可以在这里全局更改
    default_streaming_llm=ChatOpenAI(temperature=0.0,streaming=True)，这是默认设置...可以在这里全局更改，将使用于流处理
)
```


2. 使用预定义的**提示符类型**

``` python

# 您可以更改默认提示符类型
from langchain_decorators import PromptTypes, PromptTypeSettings

PromptTypes.AGENT_REASONING.llm = ChatOpenAI()

# 或者您可以定义自己的提示符类型：
class MyCustomPromptTypes(PromptTypes):
    GPT4=PromptTypeSettings(llm=ChatOpenAI(model="gpt-4"))

@llm_prompt(prompt_type=MyCustomPromptTypes.GPT4)
def write_a_complicated_code(app_idea:str)->str:
    ...

```


3. 直接在装饰器中**定义设置**

``` python

from langchain.llms import OpenAI

@llm_prompt(
    llm=OpenAI(temperature=0.7),
    stop_tokens="\nObservation"],
    ...
    )
def creative_writer(book_title:str)->str:
    ...
```


## 传递内存和/或回调

要传递任何这些内容，只需在函数中声明它们（或使用kwargs传递任何内容）

```python



@llm_prompt()

async def write_me_short_post(topic:str, platform:str="twitter", memory:SimpleMemory = None):

    """

    {history_key}

    Write me a short header for my post about {topic} for {platform} platform. 

    It should be for {audience} audience.

    (Max 15 words)

    """

    pass



await write_me_short_post(topic="old movies")



```


# 简化流式

如果我们想利用流式处理：
 - 我们需要将提示标记为异步函数
 - 在装饰器上打开流式处理，或我们可以定义启用流式处理的PromptType
 - 使用StreamingContext捕获流式处理

这样我们只需标记哪个提示应该进行流式处理，而不需要修改使用的LLM，将流式处理创建和分发处理程序传递给我们的链的特定部分...只需在提示/提示类型上打开/关闭流式处理...

只有在流式上下文中调用时，流式处理才会发生...在此处我们可以定义一个简单的函数来处理流式处理

``` python

# 此代码示例是完整的，并可以直接运行

from langchain_decorators import StreamingContext, llm_prompt

# 这将标记该提示用于流式处理（如果我们想仅在应用程序中的某些提示上进行流式处理...但不希望分发回调处理程序）
# 注意，只有异步函数可以进行流式处理（如果不是，则会出现错误）
@llm_prompt(capture_stream=True)
async def write_me_short_post(topic:str, platform:str="twitter", audience:str = "developers"):
    """
    为我在{platform}平台上关于{topic}的帖子写一个简短的标题。
    它应该是针对{audience}受众的。
    （最多15个字）
    """
    pass



# 仅是一个用来演示流式处理的任意函数...实际情况下将是一些Websockets代码
tokens=]
def capture_stream_func(new_token:str):
    tokens.append(new_token)

# 如果我们想捕获流式处理，我们需要将执行包装在StreamingContext中...
# 这将允许我们在高级方法中捕获流式处理，即使提示调用在其中隐藏
# 只有标记为capture_stream的提示才会在此处捕获
with StreamingContext(stream_to_stdout=True, callback=capture_stream_func):
    result = await run_prompt()
    print("流式处理完成...我们可以通过交替的颜色区分令牌")


print("\n我们捕获了",len(tokens),"个令牌🎉\n")
print("这是结果：")
print(result)
```



# 提示声明
默认情况下，提示是整个函数文档，除非标记了提示

## 记录提示

我们可以通过使用带有**<prompt>**语言标记的代码块来指定我们文档的哪个部分是提示定义

``` python

@llm_prompt
def write_me_short_post(topic:str, platform:str="twitter", audience:str = "developers"):
    """
    这是作为函数文档字符串一部分编写提示的好方法，其中还包括开发人员的其他文档。

    它需要作为`<prompt>`语言的代码块标记
    ```<prompt>
    为我在{platform}平台上关于{topic}的帖子写一个简短的标题。
    它应该是针对{audience}受众的。
    （最多15个字）
    ```

    现在只有上面的代码块将被用作提示，其余的字符串将被用作开发者的描述。
    （它还有一个好处是，IDE（例如VS Code）会正确显示提示（不会尝试解析为Markdown，因此不会正确显示换行符））
    """
    return
```


## 聊天消息提示

对于聊天模型，将提示定义为一组消息模板非常有用...我们来看看如何操作：

``` python

@llm_prompt
def simulate_conversation(human_input:str, agent_role:str="a pirate"):
    """
    ## System message（系统消息）
     - 注意`<prompt:_role_>`标记内部的`:system`后缀
     


    ```<prompt:system>
    你是一个{agent_role}黑客。你必须表现得像一个黑客。
    你只回复代码，在 python 或 javascript 代码块中...
    例如：
    

    ... 不要回复任何其他内容... 使用代码回复 - 尊重您的角色。
    ```

    # human message（人类消息）
    （我们使用由LLM强制执行的真实角色）
    ```<prompt:user>
    你好，你是谁？
    ```
    一个回复：
    


    ```<prompt:assistant>
    \``` python <<- 用 \ 转义内部代码块，该代码块应该是提示的一部分
    def hello():
        print("啊... 你好，该死的海盗！")
    \```

    ```
    

    我们还可以使用占位符来添加一些历史记录
    ```<prompt:placeholder>
    {history}
    ```
    ```<prompt:user>
    {human_input}
    ```

    现在只有上面的代码块将被用作提示，其余的字符串将被用作开发者的描述。
    （它还有一个好处是，IDE（例如VS Code）会正确显示提示（不会尝试解析为Markdown，因此不会正确显示换行符））
    """
    pass

```


这里的角色是模型本地的角色（assistant、user、system用于chatGPT）



# 可选部分
- 您可以定义您的提示的整个部分都是可选的
- 如果部分的任何输入缺失，则将不渲染整个部分

语法如下：

``` python

@llm_prompt
def prompt_with_optional_partials():
    """
    这段文字将一直被渲染，但

    {? 任何在此块中的内容将仅在全部{value}参数都不为空（None |“”）时渲染？}

    您也可以将其放在单词之间
    这也将被渲染{? ，但
             只有当{this_value}和{this_value}不为空时此块才会被渲染？}！
    """

```



# 输出解析器

- llm_prompt装饰器会尝试根据输出类型自动检测最佳的输出解析器（如果未设置，它将返回原始字符串）
- 原生支持列表、字典和pydantic输出（自动生成）

``` python

# 此代码示例是完整的，并可以直接运行

from langchain_decorators import llm_prompt

@llm_prompt
def write_name_suggestions(company_business:str, count:int)->list:
    """ 为那些{company_business}的公司提供{count}个好的名称建议 '"""
    pass

write_name_suggestions(company_business="sells cookies", count=5)
write_name_suggestions(company_business="sells cookies", count=5)

```


## 更复杂的结构

对于字典/Pydantic，您需要指定格式化说明...但是这可能很麻烦，所以您可以让输出解析器基于模型（pydantic）生成说明



``` python

from langchain_decorators import llm_prompt
from pydantic import BaseModel, Field


class TheOutputStructureWeExpect(BaseModel):
    name:str = Field (description="公司的名称")
    headline:str = Field( description="公司的描述（用于首页）")
    employees:liststr] = Field(description="5-8个带有职位的虚假员工姓名")

@llm_prompt()
def fake_company_generator(company_business:str)->TheOutputStructureWeExpect:
    """ 生成一个关于{company_business}的虚假公司

    {FORMAT_INSTRUCTIONS}

    """
    return

company = fake_company_generator(company_business="sells cookies")

# 将结果漂亮地格式化并打印出来
print("公司名称：",company.name)
print("公司标题：",company.headline)
print("公司员工：",company.employees)

```



# 将提示绑定到对象

``` python

from pydantic import BaseModel
from langchain_decorators import llm_prompt

class AssistantPersonality(BaseModel):
    assistant_name:str
    assistant_role:str
    field:str

    @property
    def a_property(self):
        return "whatever"

    def hello_world(self, function_kwarg:str=None):
        """
        我们可以在我们的提示中引用任何{field}或{a_property}，并与方法中的{function_kwarg}组合
        """

    
    @llm_prompt
    def introduce_your_self(self)->str:
        """
        ``` <prompt:system>
        您是一个名为{assistant_name}的助手。
        您的角色是扮演{assistant_role}
        ```
        ```<prompt:user>
        自我介绍（不超过20个字）
        ```
        """



personality = AssistantPersonality(assistant_name="John", assistant_role="a pirate")

print(personality.introduce_your_self(personality))
```



# 更多示例

- 这些示例和更多示例也可在此处的colab notebook](https://colab.research.google.com/drive/1no-8WfeP6JaLD9yUtkPgym6x0G9ZYZOG#scrollTo=N4cf__D0E2Yk)中找到
- 还包括使用纯langchain装饰器重新实现的ReAct Agent](https://colab.research.google.com/drive/1no-8WfeP6JaLD9yUtkPgym6x0G9ZYZOG#scrollTo=3bID5fryE2Yp)
