OpenWeatherMap



OpenWeatherMap提供特定位置的所有基本天气数据：

- 当前天气

- 1小时的分钟预报

- 48小时的每小时预报

- 8天的每日预报

- 国家天气警报

- 40多年历史天气数据



本页介绍如何在LangChain中使用OpenWeatherMap API



安装和设置



- 使用以下命令安装所需模块：

```bash

pip install pyowm

```

- 前往OpenWeatherMap注册账户并获取API密钥点击这里](https://openweathermap.org/api/)

- 将API密钥设置为`OPENWEATHERMAP_API_KEY`环境变量



封装器



实用工具



存在一个OpenWeatherMapAPIWrapper实用工具, 用于封装该API。导入此工具的方法如下:



```python

from langchain.utilities.openweathermap import OpenWeatherMapAPIWrapper

```



有关此封装器的更详细步骤，请参见此笔记本](../modules/agents/tools/examples/openweathermap.ipynb)。



工具



您也可以将此封装器轻松加载为工具（与代理一起使用）。

可以通过以下方法实现：



```python

from langchain.agents import load_tools

tools = load_tools(["openweathermap-api"])

```



有关更多信息，请参见此页面](../modules/agents/tools/getting_started.md)

