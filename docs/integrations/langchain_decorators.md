# LangChain Decorators ✨LangChain装饰器✨


lanchchain decorators is a layer on the top of LangChain that provides syntactic sugar 🍭 for writing custom langchain prompts and chainsLangChain装饰器是LangChain的一层，为编写自定义LangChain提示和链提供语法糖🍭


For Feedback, Issues, Contributions - please raise an issue here: 有反馈,问题,贡献-请在此提出问题:
[ju-bezdek/langchain-decorators](https://github.com/ju-bezdek/langchain-decorators)






Main principles and benefits:



- more `pythonic` way of writing code更符合Python风格的代码编写方式
- write multiline prompts that wont break your code flow with indentation编写多行提示，不会因缩进而中断代码流
- making use of IDE in-built support for **hinting**, **type checking** and **popup with docs** to quickly peek in the function to see the prompt, parameters it consumes etc.利用IDE内置的支持实现**提示**, **类型检查**和**弹出文档**，以快速查看函数中的提示,参数等
- leverage all the power of 🦜🔗 LangChain ecosystem利用🦜🔗 LangChain生态系统的所有功能
- adding support for **optional parameters**添加对**可选参数**的支持
- easily share parameters between the prompts by binding them to one class通过将参数绑定到一个类实现在提示之间轻松共享参数






Here is a simple example of a code written with **LangChain Decorators ✨**这是使用**LangChain装饰器✨**编写的简单代码示例


``` python


:llm_prompt

def write_me_short_post(topic:str, platform:str="twitter", audience:str = "developers")->str:

    """

    Write me a short header for my post about {topic} for {platform} platform. 

    It should be for {audience} audience.

    (Max 15 words)

    """

    return



# run it naturaly

write_me_short_post(topic="starwars")

# or

write_me_short_post(topic="starwars", platform="redit")

```



# Quick start快速入门
## Installation安装
```bash
pip install langchain_decorators

```



## Examples示例


Good idea on how to start is to review the examples here:开始的好方法是查看这里的示例:
 - [jupyter notebook](https://github.com/ju-bezdek/langchain-decorators/blob/main/example_notebook.ipynb)

 - [colab notebook](https://colab.research.google.com/drive/1no-8WfeP6JaLD9yUtkPgym6x0G9ZYZOG#scrollTo=N4cf__D0E2Yk)



# Defining other parameters定义其他参数
Here we are just marking a function as a prompt with `llm_prompt` decorator, turning it effectively into a LLMChain. Instead of running it 在这里，我们只是用`llm_prompt`装饰器将函数标记为提示，实际上将其转换为LLMChain。而不是运行它




Standard LLMchain takes much more init parameter than just inputs_variables and prompt... here is this implementation detail hidden in the decorator.标准LLMchain所需的初始化参数远远不止inputs_variables和prompt…这个实现细节隐藏在装饰器中。
Here is how it works:它是如何工作的


1. Using **Global settings**:1. 使用**全局设置**


``` python
# define global settings for all prompty (if not set - chatGPT is the current default)

from langchain_decorators import GlobalSettings



GlobalSettings.define_settings(

    default_llm=ChatOpenAI(temperature=0.0), this is default... can change it here globally

    default_streaming_llm=ChatOpenAI(temperature=0.0,streaming=True), this is default... can change it here for all ... will be used for streaming

)

```



2. Using predefined **prompt types**



``` python
#You can change the default prompt types

from langchain_decorators import PromptTypes, PromptTypeSettings



PromptTypes.AGENT_REASONING.llm = ChatOpenAI()



# Or you can just define your own ones:

class MyCustomPromptTypes(PromptTypes):

    GPT4=PromptTypeSettings(llm=ChatOpenAI(model="gpt-4"))



:llm_prompt(prompt_type=MyCustomPromptTypes.GPT4) 

def write_a_complicated_code(app_idea:str)->str:

    ...



```


3. 直接在装饰器中定义设置 **

``` python
from langchain.llms import OpenAI



:llm_prompt(

    llm=OpenAI(temperature=0.7),

    stop_tokens=["Observation"],

    ...

    )

def creative_writer(book_title:str)->str:

    ...

```


## 传递内存和/或回调函数:

要传递这些东西，只需在函数中声明它们（或使用kwargs传递任何内容）

``` python


:llm_prompt()

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


# 简化流式传输

如果我们想利用流式传输 :
 - we need to define prompt as async function 

 - turn on the streaming on the decorator, or we can define PromptType with streaming on

 - capture the stream using StreamingContext


这样，我们只需标记哪个提示应该被流，而不需要调整使用哪个LLM，在我们的链的特定部分传递并分发流式处理程序...

只有在流上下文中调用时，流式传输才会发生...在那里我们可以定义一个简单的函数来处理流

``` python
# this code example is complete and should run as it is



from langchain_decorators import StreamingContext, llm_prompt



# this will mark the prompt for streaming (useful if we want stream just some prompts in our app... but don't want to pass distribute the callback handlers)

# note that only async functions can be streamed (will get an error if it's not)

:llm_prompt(capture_stream=True) 

async def write_me_short_post(topic:str, platform:str="twitter", audience:str = "developers"):

    """

    Write me a short header for my post about {topic} for {platform} platform. 

    It should be for {audience} audience.

    (Max 15 words)

    """

    pass







# just an arbitrary  function to demonstrate the streaming... wil be some websockets code in the real world

tokens=[]

def capture_stream_func(new_token:str):

    tokens.append(new_token)



# if we want to capture the stream, we need to wrap the execution into StreamingContext... 

# this will allow us to capture the stream even if the prompt call is hidden inside higher level method

# only the prompts marked with capture_stream will be captured here

with StreamingContext(stream_to_stdout=True, callback=capture_stream_func):

    result = await run_prompt()

    print("Stream finished ... we can distinguish tokens thanks to alternating colors")





print("We've captured",len(tokens),"tokens🎉")

print("Here is the result:")

print(result)

```



# 提示声明
默认情况下，提示是整个函数文档，除非您标记了提示

## 记录您的提示

我们可以通过指定带有 **<prompt>** 语言标记的代码块来指定我们的文档的哪一部分是提示定义

``` python
:llm_prompt

def write_me_short_post(topic:str, platform:str="twitter", audience:str = "developers"):

    """

    Here is a good way to write a prompt as part of a function docstring, with additional documentation for devs.



    It needs to be a code block, marked as a `<prompt>` language

    ```<prompt>

    Write me a short header for my post about {topic} for {platform} platform. 

    It should be for {audience} audience.

    (Max 15 words)

    ```



    Now only to code block above will be used as a prompt, and the rest of the docstring will be used as a description for developers.

    (It has also a nice benefit that IDE (like VS code) will display the prompt properly (not trying to parse it as markdown, and thus not showing new lines properly))

    """

    return 

```


## 聊天消息提示

对于聊天模型而言，将提示定义为一组消息模板非常有用...以下是如何执行的 :

``` python
:llm_prompt

def simulate_conversation(human_input:str, agent_role:str="a pirate"):

    """

    ## System message

     - note the `:system` sufix inside the <prompt:_role_> tag

     



    ```<prompt:system>

    You are a {agent_role} hacker. You mus act like one.

    You reply always in code, using python or javascript code block...

    for example:

    

    ... do not reply with anything else.. just with code - respecting your role.

    ```



    # human message 

    (we are using the real role that are enforced by the LLM - GPT supports system, assistant, user)

    ``` <prompt:user>

    Helo, who are you

    ```

    a reply:

    



    ``` <prompt:assistant>

    \``` python <<- escaping inner code block with \ that should be part of the prompt

    def hello():

        print("Argh... hello you pesky pirate")

    \```

    ```

    

    we can also add some history using placeholder

    ```<prompt:placeholder>

    {history}

    ```

    ```<prompt:user>

    {human_input}

    ```



    Now only to code block above will be used as a prompt, and the rest of the docstring will be used as a description for developers.

    (It has also a nice benefit that IDE (like VS code) will display the prompt properly (not trying to parse it as markdown, and thus not showing new lines properly))

    """

    pass



```


这里的角色是模型的本机角色（聊天GPT的助手,用户,系统）



# 可选部分
- 您可以定义整个提示的可选部分
- 如果部分中的任何输入都丢失，则整个部分将不会呈现

这个语法的写法如下:


``` python
:llm_prompt

def prompt_with_optional_partials():

    """

    this text will be rendered always, but



    {? anything inside this block will be rendered only if all the {value}s parameters are not empty (None | "")   ?}



    you can also place it in between the words

    this too will be rendered{? , but

        this  block will be rendered only if {this_value} and {this_value}

        is not empty?} !

    """

```



# 输出解析器

- llm_prompt修饰器会自动检测最佳的输出解析器（如果没有设置则返回原始字符串）
- list/dict和pydantic类型的输出也会被自动支持

``` python
# this code example is complete and should run as it is



from langchain_decorators import llm_prompt



:llm_prompt

def write_name_suggestions(company_business:str, count:int)->list:

    """ Write me {count} good name suggestions for company that {company_business}

    """

    pass



write_name_suggestions(company_business="sells cookies", count=5)

```


## 更复杂的结构

对于dict/pydantic类型，您需要指定格式化指令…
这可能很乏味，这就是为什么您可以让输出解析器基于模型（pydantic）为您生成指令

``` python
from langchain_decorators import llm_prompt

from pydantic import BaseModel, Field





class TheOutputStructureWeExpect(BaseModel):

    name:str = Field (description="The name of the company")

    headline:str = Field( description="The description of the company (for landing page)")

    employees:list[str] = Field(description="5-8 fake employee names with their positions")



:llm_prompt()

def fake_company_generator(company_business:str)->TheOutputStructureWeExpect:

    """ Generate a fake company that {company_business}

    {FORMAT_INSTRUCTIONS}

    """

    return



company = fake_company_generator(company_business="sells cookies")



# print the result nicely formatted

print("Company name: ",company.name)

print("company headline: ",company.headline)

print("company employees: ",company.employees)



```



# 将提示绑定到对象

``` python
from pydantic import BaseModel

from langchain_decorators import llm_prompt



class AssistantPersonality(BaseModel):

    assistant_name:str

    assistant_role:str

    field:str



    :property

    def a_property(self):

        return "whatever"



    def hello_world(self, function_kwarg:str=None):

        """

        We can reference any {field} or {a_property} inside our prompt... and combine it with {function_kwarg} in the method

        """



    

    :llm_prompt

    def introduce_your_self(self)->str:

        """

        ``` <prompt:system>

        You are an assistant named {assistant_name}. 

        Your role is to act as {assistant_role}

        ```

        ```<prompt:user>

        Introduce your self (in less than 20 words)

        ```

        """



    



personality = AssistantPersonality(assistant_name="John", assistant_role="a pirate")



print(personality.introduce_your_self(personality))

```



# 更多示例:

- 这些和其他几个示例也可以在[此处的colab笔记本](https://colab.research.google.com/drive/1no-8WfeP6JaLD9yUtkPgym6x0G9ZYZOG#scrollTo=N4cf__D0E2Yk)中找到
- including the [ReAct Agent re-implementation](https://colab.research.google.com/drive/1no-8WfeP6JaLD9yUtkPgym6x0G9ZYZOG#scrollTo=3bID5fryE2Yp) using purely langchain decorators

