# 开始使用

在本教程中，我们将学习以下内容：
- 什么是提示模板以及为什么需要它
- 如何创建提示模板
- 如何向提示模板传递少数示例
- 如何选择提示模板的示例

## 什么是提示模板？

提示模板是指一种可复制的生成提示的方式。它包含一个文本字符串（"模板"），可以从最终用户那里接收一组参数并生成提示。

提示模板可以包含以下内容：
- 给语言模型的指示
- 一组少数示例，以帮助语言模型生成更好的回答
- 给语言模型的问题

下面的代码示例包含一个提示模板的示例：

```python

# 导入LangChain的PromptTemplate模块


template = """

我希望你能充当新公司的命名顾问。

一个制造{product}的公司的好名字是什么？

"""


prompt = PromptTemplate(

    input_variables=["product"],

    template=template,

)

prompt.format(product="五颜六色的袜子")

# -> 我希望你能充当新公司的命名顾问。

# -> 一个制造五颜六色的袜子的公司的好名字是什么？

```



## 创建一个提示模板

您可以使用`PromptTemplate`类创建简单的硬编码提示。提示模板可以接受任意数量的输入变量，并且可以进行格式化以生成提示。


```python

# 导入LangChain的PromptTemplate模块

# 没有输入变量的示例提示
no_input_prompt = PromptTemplate(input_variables=[], template="告诉我一个笑话。")

no_input_prompt.format()

# -> "告诉我一个笑话。"


# 一个输入变量的示例提示
one_input_prompt = PromptTemplate(input_variables=["形容词"], template="告诉我一个{形容词}笑话。")

one_input_prompt.format(形容词="有趣的")

# -> "告诉我一个有趣的笑话。"


# 多个输入变量的示例提示
multiple_input_prompt = PromptTemplate(

    input_variables=["形容词", "内容"], 

    template="告诉我一个{形容词}关于{内容}的笑话。"

)

multiple_input_prompt.format(形容词="有趣的", 内容="鸡")

# -> "告诉我一个有趣的关于鸡的笑话。"

```


如果您不想手动指定`input_variables`，您还可以使用`from_template`类方法创建`PromptTemplate`。`LangChain`将根据传递的`template`自动推断`input_variables`。

```python

template = "告诉我一个{形容词}关于{内容}的笑话。"


prompt_template = PromptTemplate.from_template(template)

prompt_template.input_variables

# -> ['形容词', '内容']

prompt_template.format(形容词="有趣的", 内容="鸡")

# -> 告诉我一个有趣的关于鸡的笑话。

```


您可以创建自定义提示模板来以任何您想要的方式格式化提示。有关更多信息，请参阅[自定义提示模板](examples/custom_prompt_template.ipynb)。


<!-- TODO (shreya)：在这里添加Jinja的链接。 -->

## 模板格式

默认情况下，`PromptTemplate`会将提供的模板视为Python f-string。您可以通过`template_format`参数指定其他模板格式：

```python

# 在运行此代码之前，请确保已安装jinja2

jinja2_template = "告诉我一个{{形容词}}关于{{内容}}的笑话"

prompt_template = PromptTemplate.from_template(template=jinja2_template, template_format="jinja2")


prompt_template.format(形容词="有趣的", 内容="鸡")

# -> 告诉我一个有趣的关于鸡的笑话。

```


目前，`PromptTemplate`只支持`jinja2`和`f-string`模板格式。如果您想使用其他模板格式，请随时在[Github](https://github.com/hwchase17/langchain/issues)页面上提出问题。

## 验证模板

默认情况下，`PromptTemplate`会通过检查`template`中的变量是否与`input_variables`中定义的变量匹配来验证`template`字符串。您可以通过将`validate_template`设置为`False`来禁用此行为。

```python

template = "我正在学习LangChain，因为{原因}。"


prompt_template = PromptTemplate(template=template, 

                                 input_variables=["原因", "foo"]) # 由于有额外的变量而引发ValueError

prompt_template = PromptTemplate(template=template, 

                                 input_variables=["原因", "foo"], 

                                 validate_template=False) # 无错误

```



## 序列化提示模板

您可以将`PromptTemplate`保存到本地文件系统中的文件中。`LangChain`将通过文件扩展名自动推断文件格式。目前，`LangChain`支持将模板保存为YAML和JSON文件。

```python

prompt_template.save("awesome_prompt.json") # 保存为JSON文件

```


```python

from langchain.prompts import load_prompt

loaded_prompt = load_prompt("awesome_prompt.json")


assert prompt_template == loaded_prompt

```


`LangChain`还支持从LangChainHub加载提示模板，其中包含一系列有用的提示，可供您在项目中使用。您可以在[这里](https://github.com/hwchase17/langchain-hub)了解有关LangChainHub和可用的提示的更多信息。

```python


from langchain.prompts import load_prompt


prompt = load_prompt("lc://prompts/conversation/prompt.json")

prompt.format(history="", input="1 + 1等于多少？")

```


您可以在[如何序列化提示](examples/prompt_serialization.ipynb)中了解更多关于序列化提示模板的信息。


## 向提示模板传递少数示例

少数示例是一组可用于帮助语言模型生成更好回答的示例。

要使用少数示例生成提示，您可以使用`FewShotPromptTemplate`。该类接收一个`PromptTemplate`和一个少数示例列表，并使用少数示例格式化提示模板。

在此示例中，我们将创建一个生成单词反义词的提示。

```python

from langchain import PromptTemplate, FewShotPromptTemplate


# 首先，创建少数示例列表。

examples = [

    {"word": "happy", "antonym": "sad"},

    {"word": "tall", "antonym": "short"},

]


# 接下来，我们指定用于格式化提供的示例的模板。

# 我们使用`PromptTemplate`类来完成此操作。

example_formatter_template = """Word: {word}

Antonym: {antonym}

"""


example_prompt = PromptTemplate(

    input_variables=["word", "antonym"],

    template=example_formatter_template,

)


# 最后，我们创建`FewShotPromptTemplate`对象。

few_shot_prompt = FewShotPromptTemplate(

    # 这是我们要插入到提示中的示例。

    examples=examples,

    # 这是插入到提示中的示例的格式。

    example_prompt=example_prompt,

    # 前缀是一些在示例之前的文本，通常包含说明。

    prefix="给出每个输入的反义词\n",

    # 后缀是一些在示例之后的文本，通常这是用户输入的位置。

    suffix="Word: {input}\nAntonym: ",

    # 输入变量是整个提示期望的变量。

    input_variables=["input"],

    # 示例分隔符是用来连接前缀、示例和后缀的字符串。

    example_separator="\n",

)


# 现在我们可以使用`format`方法生成一个提示。

print(few_shot_prompt.format(input="big"))

# -> 给出每个输入的反义词

# -> 

# -> Word: happy

# -> Antonym: sad

# ->

# -> Word: tall

# -> Antonym: short

# ->

# -> Word: big

# -> Antonym: 

# -> Word: big


```



## 选择提示模板的示例

如果您有大量的示例，您可以使用`ExampleSelector`选择一部分最有信息量的示例，这有助于您生成更有可能得到良好回应的提示。

在下面的示例中，我们将使用`LengthBasedExampleSelector`，它根据输入的长度选择示例。当您担心构建的提示超过上下文窗口的长度时，这非常有用。对于较长的输入，它会选择要包含的示例较少，而对于较短的输入，它会选择较多的示例。

我们将继续使用上一节的示例，但这次我们将使用`LengthBasedExampleSelector`来选择示例。

```python

from langchain.prompts.example_selector import LengthBasedExampleSelector



# 这里有很多一个虚构的任务的示例，我们要创建反义词。

examples = [

    {"word": "happy", "antonym": "sad"},

    {"word": "tall", "antonym": "short"},

    {"word": "energetic", "antonym": "lethargic"},

    {"word": "sunny", "antonym": "gloomy"},

    {"word": "windy", "antonym": "calm"},

]


# 我们将使用`LengthBasedExampleSelector`来选择示例。

example_selector = LengthBasedExampleSelector(

    # 这是它可选择的示例。

    examples=examples, 

    # 这是用于格式化示例的PromptTemplate。

    example_prompt=example_prompt, 

    # 这是应该格式化示例的最大长度。

    # 长度是由下面的get_text_length函数测量的。

    max_length=25

    # 这是用于获取字符串长度的函数，它用于确定要包含的示例。如果未指定，它将作为默认值提供。

    # get_text_length: Callable[[str], int] = lambda x: len(re.split("\n| ", x))

)


)



# 现在我们可以使用`example_selector`创建`FewShotPromptTemplate`。

dynamic_prompt = FewShotPromptTemplate(

    # 我们提供了ExampleSelector而不是examples。

    example_selector=example_selector,

    example_prompt=example_prompt,

    prefix="给出每个输入的反义词",

    suffix="Word: {input}\nAntonym:",

    input_variables=["input"],

    example_separator="\n\n",

)


# 现在我们可以使用`format`方法生成一个提示。

print(dynamic_prompt.format(input="big"))

# -> 给出每个输入的反义词

# ->

# -> Word: happy

# -> Antonym: sad

# ->

# -> Word: tall

# -> Antonym: short

# ->

# -> Word: energetic

# -> Antonym: lethargic

# ->

# -> Word: sunny

# -> Antonym: gloomy

# ->

# -> Word: windy

# -> Antonym: calm

# ->

# -> Word: big

# -> Antonym:

```


与此相反，如果我们输入一个很长的输入，`LengthBasedExampleSelector`会选择较少的示例包含在提示中。


```python

long_string = "big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else"

print(dynamic_prompt.format(input=long_string))

# -> 给出每个输入的反义词


# -> Word: happy

# -> Antonym: sad

# ->

# -> Word: big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else

# -> Antonym:

```


<!-- TODO (shreya): 添加正确的链接。 -->
LangChain带有几个示例选择器，您可以使用它们。有关如何使用它们的详细信息，请参阅[示例选择器](../example_selectors.rst)。

您可以创建自定义示例选择器，根据您想要的任何条件选择示例。有关如何执行此操作的详细信息，请参阅[创建自定义示例选择器](../example_selectors/examples/custom_example_selector.md)。
