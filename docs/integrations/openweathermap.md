＃OpenWeatherMap（OpenWeatherMap）提供了特定位置的所有基本气象数据

> -当前天气> -1小时的分钟预报> -48小时的小时预报> -8天的每日天气预报> -国家气象警报> -40多年的历史气象数据
> -当前天气
> -1小时的分钟预报
> -48小时的小时预报
> -8天的每日天气预报
> -国家气象警报
> -40多年的历史气象数据

本页面介绍了如何在LangChain中使用OpenWeatherMap API。

##安装和设置

-使用以下方法安装要求
```bash
pip install pyowm

```

-转到OpenWeatherMap并注册帐户以获取您的API密钥[此处]（https://openweathermap.org/api/）
-将API密钥设置为“OPENWEATHERMAP_API_KEY”环境变量

##包装器

###实用工具

存在一个OpenWeatherMapAPIWrapper实用程序，用于包装此API。 要导入此实用程序: 

```python
from langchain.utilities.openweathermap import OpenWeatherMapAPIWrapper

```


有关此包装器的更详细说明，请参见[此笔记本](../modules/agents/tools/examples/openweathermap.ipynb)。

###工具

您还可以将此包装器轻松加载为工具（与代理一起使用）。 \ n您可以使用以下方法执行此操作: 

```python
```python

from langchain.agents import load_tools

tools = load_tools(["openweathermap-api"])

```


For more information on this, see [this page](../modules/agents/tools/getting_started.md)

