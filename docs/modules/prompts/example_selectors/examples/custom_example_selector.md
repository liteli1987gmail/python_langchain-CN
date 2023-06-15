# 如何创建自定义示例选择器



在本教程中，我们将创建一个自定义示例选择器，从给定的示例列表中选择每个交替示例。



一个 `ExampleSelector` 必须实现两个方法：



1. 一个 `add_example` 方法，它接收一个示例并将其添加到 ExampleSelector 中

2. 一个 `select_examples` 方法，它接收输入变量（用户输入）并返回用于 few shot 提示中的示例列表。



让我们实现一个自定义的 `ExampleSelector`，它只是随机选择两个示例。



:::{note}

在 LangChain 中支持的当前示例选择器实现请参阅[这里](../../prompt_templates/getting_started.md)。

:::



<!-- TODO(shreya): 添加正确的链接。 -->



## 实现自定义示例选择器



```python

from langchain.prompts.example_selector.base import BaseExampleSelector

from typing import Dict, List

import numpy as np





class CustomExampleSelector(BaseExampleSelector):

    

    def __init__(self, examples: List[Dict[str, str]]):

        self.examples = examples

    

    def add_example(self, example: Dict[str, str]) -> None:

        """为一个键添加新示例."""

        self.examples.append(example)



    def select_examples(self, input_variables: Dict[str, str]) -> List[dict]:

        """根据输入选择要使用的示例."""

        return np.random.choice(self.examples, size=2, replace=False)



```





## 使用自定义示例选择器



```python



examples = [

    {"foo": "1"},

    {"foo": "2"},

    {"foo": "3"}

]



# 初始化示例选择器。

example_selector = CustomExampleSelector(examples)





# 选择示例

example_selector.select_examples({"foo": "foo"})

# -> array([{'foo': '2'}, {'foo': '3'}], dtype=object)



# 将新示例添加到示例集中

example_selector.add_example({"foo": "4"})

example_selector.examples

# -> [{'foo': '1'}, {'foo': '2'}, {'foo': '3'}, {'foo': '4'}]



# 选择示例

example_selector.select_examples({"foo": "foo"})

# -> array([{'foo': '1'}, {'foo': '4'}], dtype=object)

```

