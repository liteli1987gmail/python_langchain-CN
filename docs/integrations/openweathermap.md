# OpenWeatherMap



>[OpenWeatherMap](https://openweathermap.org/api/)为特定位置提供所有基本的天气数据:

>- 当前天气

>- 1小时内的分钟级预报

>- 48小时内的每小时预报

>- 8天内的每日预报

>- 全国天气警报

>- 40年以上的历史天气数据



本页面介绍如何在LangChain中使用`OpenWeatherMap API`。



## 安装和设置



- 使用以下命令安装所需的软件包

```bash

pip install pyowm

```

- 前往OpenWeatherMap注册账户并获取API密钥[在这里](https://openweathermap.org/api/)

- 将API密钥设置为`OPENWEATHERMAP_API_KEY`环境变量



## 包装器



### 实用工具



存在一个OpenWeatherMapAPIWrapper实用工具来封装该API。导入此工具的方式如下:



```python

from langchain.utilities.openweathermap import OpenWeatherMapAPIWrapper

```



有关此包装器的详细介绍，请参阅[此笔记本](../modules/agents/tools/examples/openweathermap.ipynb)。



### 工具



您还可以将此包装器轻松加载为工具（与Agent一起使用）。

您可以使用以下代码实现:



```python

from langchain.agents import load_tools

tools = load_tools(["openweathermap-api"])

```



有关更多信息，请参阅[此页面](../modules/agents/tools/getting_started.md)

