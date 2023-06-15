# LangChain装饰器✨


lanchchain装饰器是在LangChain上添加的一层，为编写自定义LangChain提示和链提供了更简洁的语法糖🍭。



有关反馈、问题和贡献，请在这里提出问题：

[ju-bezdek/langchain-decorators](https://github.com/ju-bezdek/langchain-decorators)







主要原则和好处：



- 更符合Python风格的代码编写方式

- 编写多行提示，不会因缩进而破坏代码流程

- 利用IDE内置的**提示**、**类型检查**和**弹出文档**功能，快速查看函数的提示、消耗的参数等信息

- 发挥🦜🔗 LangChain生态系统的全部能力

- 添加对**可选参数**的支持

- 通过将它们绑定到一个类来在提示之间轻松共享参数







下面是一个使用**LangChain装饰器✨**编写的简单示例：



``` python



@llm_prompt

def write_me_short_post(topic:str, platform:str="twitter", audience:str = "developers")->str:

    """

    为{topic}的{platform}平台编写一篇关于{audience}受众的简短标题。

    （最多15个单词）

    """

    return





# 自然运行

write_me_short_post(topic="starwars")

# 或者

write_me_short_post(topic="starwars", platform="redit")

```



# 快速入门

## 安装

```bash

pip install langchain_decorators

```



## 示例



在这里查看示例的好主意：

 - [jupyter notebook](https://github.com/ju-bezdek/langchain-decorators/blob/main/example_notebook.ipynb)

 - [colab笔记本](https://colab.research.google.com/drive/1no-8WfeP6JaLD9yUtkPgym6x0G9ZYZOG#scrollTo=N4cf__D0E2Yk)



# 定义其他参数

我们只是用`llm_prompt`装饰器标记函数为提示，从而有效地将其转换为LLMChain。而不用运行它





标准LLMchain需要比输入变量和提示更多的参数...在装饰器中隐藏了此实现细节。

工作原理如下：



1. 使用**全局设置**：



``` python

# 为所有提示定义全局设置（如果未设置，默认为chatGPT）

from langchain_decorators import GlobalSettings



GlobalSettings.define_settings(

    default_llm=ChatOpenAI(temperature=0.0)，这是默认值...可以在此处全局更改

    default_streaming_llm=ChatOpenAI(temperature=0.0,streaming=True)，这是默认值...可以在此处全局更改为流式传输

)

```



2. 使用预定义的**提示类型**



``` python

# 您可以更改默认的提示类型

from langchain_decorators import PromptTypes, PromptTypeSettings



PromptTypes.AGENT_REASONING.llm = ChatOpenAI()



# 或者只是定义您自己的提示类型：

class MyCustomPromptTypes(PromptTypes):

    GPT4=PromptTypeSettings(llm=ChatOpenAI(model="gpt-4"))



@llm_prompt(prompt_type=MyCustomPromptTypes.GPT4) 

def write_a_complicated_code(app_idea:str)->str:

    ...



```



3. 直接在装饰器中定义设置



``` python

from langchain.llms import OpenAI



@llm_prompt(

    llm=OpenAI(temperature=0.7),

    stop_tokens=["\nObservation"],

    ...

    )

def creative_writer(book_title:str)->str:

    ...

```



## 传递memory和/或回调函数：



要传递任何这些，请在函数中声明它们（或使用kwargs传递任何内容）



```python



@llm_prompt()

async def write_me_short_post(topic:str, platform:str="twitter", memory:SimpleMemory = None):

    """

    {history_key}

    为{topic}的{platform}平台编写一篇关于{audience}受众的简短标题。

    （最多15个单词）

    """

    pass



await write_me_short_post(topic="old movies")

await write_me_short_post(topic="old movies")



```



# 简化流式传输



如果我们想要利用流式传输：

 - 我们需要将提示定义为异步函数

 - 在装饰器中打开流式传输，或我们可以定义带有流式传输的PromptType

 - 使用StreamingContext来捕获流



这样，我们只需标记哪个提示应该进行流式传输，而无需调整我们要使用的LLM，将流式处理程序的创建和分发传递到我们的链的特定部分中...只需在提示/提示类型上开关流式传输开/关即可



只有当我们在流式上下文中调用它时，流式传输才会发生...我们可以在那里定义一个处理流的简单函数



``` python

# 此代码示例完整且可直接运行



from langchain_decorators import StreamingContext, llm_prompt



# 这将标记提示用于流式传输（如果我们只想要应用程序中的某些提示进行流式传输...但不想传递分发的回调处理程序）

# 请注意，只有异步函数可以进行流式传输（如果不是异步函数，将会报错）

@llm_prompt(capture_stream=True) 

async def write_me_short_post(topic:str, platform:str="twitter", audience:str = "developers"):

    """

    为{topic}的{platform}平台编写一篇关于{audience}受众的简短标题。

    （最多15个单词）

    """

    pass







# 只是一个演示流式传输的任意函数...在现实世界中，将是一些websocket代码

tokens=[]

def capture_stream_func(new_token:str):

    tokens.append(new_token)



# 如果我们要捕获流，我们需要将执行包装在StreamingContext中...

# 这将允许我们捕获流，即使提示调用在更高级的方法中隐藏

# 只有标记为capture_stream的提示将在此处捕获

with StreamingContext(stream_to_stdout=True, callback=capture_stream_func):

    result = await run_prompt()

    print("流程结束...我们可以根据颜色区分令牌")

    print("Stream finished ... we can distinguish tokens thanks to alternating colors")





print("\n我们捕获了",len(tokens),"个令牌🎉\n")

print("下面是结果:")

print(result)

```





# 提示声明

默认情况下，提示是整个函数文档，除非标记了提示



## 文档化您的提示



我们可以通过在代码块中使用**<prompt>**语言标签来指定我们的文档中的哪部分是提示定义



``` python

@llm_prompt

def write_me_short_post(topic:str, platform:str="twitter", audience:str = "developers"):

    """

    这是一个很好的方法，可以将提示作为函数文档的一部分来编写，并为开发人员提供其他文档。



    它必须是一个被标记为`<prompt>`语言的代码块

    ```<prompt>

    为{topic}的{platform}平台编写一篇关于{audience}受众的简短标题。

    （最多15个单词）

    (Max 15 words)

    ```



    现在，只有上面的代码块将被用作提示，剩下的文档将被用作开发人员的描述。

    （它还具有一个好处，即IDE（如VS code）将正确显示提示（不尝试解析为markdown，因此无法正确显示换行））

    """

    return 

```



## 聊天消息提示



对于聊天模型来说，将提示定义为一组消息模板非常有用...以下为如何使用它：



``` python

@llm_prompt

def simulate_conversation(human_input:str, agent_role:str="a pirate"):

    """

    ## 系统消息

     - 注意在<prompt:_role_>标记内部的`:system`后缀

     



    ```<prompt:system>

    你是一个{agent_role}的黑客。你必须像一个黑客一样行动。

    你总是使用Python或JavaScript代码块进行回复...

    例如：

    

    ... 不要回复其他任何内容...只需使用代码进行回复 - 尊重您的角色。

    ```



    # 人类消息

    （我们正在使用LLM强制执行的真实角色，GPT支持system、assistant、user）

    ``` <prompt:user>

    你好，你是谁

    ```

    一条回复：

    



    ``` <prompt:assistant>

    \``` python <<- escaping inner code block with \ that should be part of the prompt

    def hello():

        print("Argh...你好，可恶的海盗")

    \```

    ```

    

    我们还可以使用占位符添加一些历史记录

    ```<prompt:placeholder>

    {history}

    ```

    ```<prompt:user>

    {human_input}

    ```



    现在，只有上面的代码块将被用作提示，剩下的文档将被用作开发人员的描述。

    （它还具有一个好处，即IDE（如VS code）将正确显示提示（不尝试解析为markdown，因此无法正确显示换行））

    """

    pass



```



这里的角色是模型原生角色（assistant、user、system用于chatGPT）







# 可选部分

- 您可以定义整个提示的可选部分

- 如果该部分中的任何输入都丢失，则整个部分将不会被呈现



语法如下：



``` python

@llm_prompt

def prompt_with_optional_partials():

    """

    始终呈现此文本，但



    {? 如果所有{value}参数都不为空（None | ""），则仅渲染该代码块 ?}



    也可以将其放在单词之间

    this too will be rendered{? ，但

        仅当{this_value}和{this_value}

        不为空时才渲染？} !

    """

```





# 输出解析器



- llm_prompt装饰器会尝试根据输出类型自动检测最佳输出解析器（如果未设置，则返回原始字符串）

- 列表、字典和pydantic输出也提供了原生支持（自动处理）



``` python

# 此代码示例完整且可直接运行



from langchain_decorators import llm_prompt



@llm_prompt

def write_name_suggestions(company_business:str, count:int)->list:

    """ 为{company_business}的公司提供{count}个优秀的名称建议

    """

    pass



write_name_suggestions(company_business="sells cookies", count=5)

```



## 更复杂的结构



对于dict / pydantic，您需要指定格式化指令...可以让输出解析器根据模型（pydantic）生成指令，这样就不用一个一个手动添加了





``` python

from langchain_decorators import llm_prompt

from pydantic import BaseModel, Field





class TheOutputStructureWeExpect(BaseModel):

    name:str = Field (description="公司名称")

    headline:str = Field( description="公司描述（用于着陆页）")

    employees:list[str] = Field(description="5-8个假员工姓名及其职位")



@llm_prompt()

def fake_company_generator(company_business:str)->TheOutputStructureWeExpect:

    """ 生成一个{company_business}的虚拟公司

    {FORMAT_INSTRUCTIONS}

    """

    return



company = fake_company_generator(company_business="sells cookies")



# 以漂亮的格式打印结果

print("公司名称：",company.name)

print("公司说明：",company.headline)

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

        我们可以在提示中引用任何{field}或{a_property}，并与{function_kwarg}组合在方法中

        """



    

    @llm_prompt

    def introduce_your_self(self)->str:

        """

        ``` <prompt:system>

        您是名为{assistant_name}的助手。 

        您的角色是充当{assistant_role}

        ```

        ```<prompt:user>

        自我介绍（不超过20个单词）

        ```

        """



    



personality = AssistantPersonality(assistant_name="John", assistant_role="a pirate")



print(personality.introduce_your_self(personality))

```





# 更多示例：



- 这些以及其他几个示例也可以在[colab笔记本中](https://colab.research.google.com/drive/1no-8WfeP6JaLD9yUtkPgym6x0G9ZYZOG#scrollTo=N4cf__D0E2Yk)找到

- 包括纯粹使用LangChain装饰器实现的[ReAct Agent重新实现](https://colab.research.google.com/drive/1no-8WfeP6JaLD9yUtkPgym6x0G9ZYZOG#scrollTo=3bID5fryE2Yp)

