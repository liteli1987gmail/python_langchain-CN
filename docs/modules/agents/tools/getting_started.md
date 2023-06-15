# 开始使用



工具是代理人与世界交互的函数。

这些工具可以是通用工具（例如搜索），其他链，甚至其他代理人。



目前，可以使用以下代码段加载工具：



```python

from langchain.agents import load_tools

tool_names = [...]

tools = load_tools(tool_names)

```



某些工具（例如链，代理人）可能需要基本的LLM才能使用初始化。

在这种情况下，您还可以传入LLM：



```python

from langchain.agents import load_tools

tool_names = [...]

llm = ...

tools = load_tools(tool_names, llm=llm)

```



下面是支持的全部工具及相关信息的列表：



- 工具名称：LLM引用该工具的名称。

- 工具描述：传递给LLM的工具描述。

- 注释：有关工具的注释不会传递给LLM。

- 需要LLM：此工具是否需要LLM进行初始化。

- （可选）额外参数：初始化此工具所需的额外参数。



## 工具列表



**python_repl**



- 工具名称：Python REPL

- 工具描述：Python shell。可以使用它来执行Python命令。输入应为有效的Python命令。如果您期望有输出，则应打印出来。

- 注释：保持状态。

- 需要LLM：否



**serpapi**



- 工具名称：搜索

- 工具描述：搜索引擎。当您需要回答关于当前事件的问题时有用。输入应为搜索查询。

- 注释：调用Serp API，然后解析结果。

- 需要LLM：否



**wolfram-alpha**



- 工具名称：Wolfram Alpha

- 工具描述：Wolfram Alpha搜索引擎。当您需要回答关于数学、科学、技术、文化、社会和日常生活的问题时有用。输入应为搜索查询。

- 注释：调用Wolfram Alpha API然后解析结果。

- 需要LLM：否

- 额外参数：`wolfram_alpha_appid`：Wolfram Alpha应用ID。



**requests**



- 工具名称：请求

- 工具描述：访问互联网的门户。当您需要从网站获取特定内容时使用。输入应为特定的URL，输出将是该页面上的所有文本。

- 注释：使用Python requests模块。

- 需要LLM：否



**terminal**



- 工具名称：终端

- 工具描述：在终端中执行命令。输入应为有效命令，输出将是运行该命令时的任何输出。

- 注释：使用subprocess执行命令。

- 需要LLM：否



**pal-math**



- 工具名称：PAL-MATH

- 工具描述：用于解决复杂的字词数学问题的语言模型。输入应为完整的字词难度数学问题。

- 注释：基于此论文（https://arxiv.org/pdf/2211.10435.pdf）。

- 需要LLM：是



**pal-colored-objects**



- 工具名称：PAL-COLOR-OBJ

- 工具描述：出色地推理对象的位置和颜色属性的语言模型。输入应为完整的推理问题的字词难度。确保包括关于对象和您想要回答的最终问题的所有信息。

- 注释：基于此论文（https://arxiv.org/pdf/2211.10435.pdf）。

- 需要LLM：是



**llm-math**



- 工具名称：计算器

- 工具描述：用于回答数学问题的有用工具。

- 注释：`LLMMath`链的实例。

- 需要LLM：是



**open-meteo-api**



- 工具名称：Open Meteo API

- 工具描述：从OpenMeteo API获取天气信息时使用。输入应为此API可以回答的自然语言问题。

- 注释：与Open Meteo API（https://api.open-meteo.com/）的自然语言连接，特别是`/v1/forecast`终点。

- 需要LLM：是



**news-api**



- 工具名称：新闻API

- 工具描述：当您想要获取有关当前新闻故事的头条新闻信息时使用。输入应为此API可以回答的自然语言问题。

- 注释：与新闻API（https://newsapi.org）的自然语言连接，特别是`/v2/top-headlines`终点。

- 需要LLM：是

- 额外参数：`news_api_key`（访问此终点的API密钥）



**tmdb-api**



- 工具名称：TMDB API

- 工具描述：从The Movie Database获取信息时使用。输入应为此API可以回答的自然语言问题。

- 注释：与TMDB API（https://api.themoviedb.org/3）的自然语言连接，特别是`/search/movie`终点。

- 需要LLM：是

- 额外参数：`tmdb_bearer_token`（访问此终点的Bearer令牌 - 注意，这与API密钥不同）



**google-search**



- 工具名称：搜索

- 工具描述：Google搜索的包装器。当您需要回答关于当前事件的问题时有用。输入应为搜索查询。

- 注释：使用Google Custom Search API

- 需要LLM：否

- 额外参数：`google_api_key`，`google_cse_id`

- 有关此信息，请参阅[此页面](../../../integrations/google_search.md)



**searx-search**



- 工具名称：搜索

- 工具描述：SearxNG元搜索引擎的包装器。输入应为搜索查询。

- 注释：SearxNG易于部署的自托管工具。这是一个对Google Search友好的隐私友好的替代品。使用SearxNG API。

- 需要LLM：否

- 额外参数：`searx_host`



**google-serper**



- 工具名称：搜索

- 工具描述：成本较低的Google搜索API。当您需要回答关于当前事件的问题时有用。输入应为搜索查询。

- 注释：调用[serper.dev](https://serper.dev)的Google搜索API，然后解析结果。

- 需要LLM：否

- 额外参数：`serper_api_key`

- 有关此信息，请参阅[此页面](../../../integrations/google_serper.md)



**wikipedia**



- 工具名称：维基百科

- 工具描述：维基百科的包装器。用于回答关于人物、地点、公司、历史事件或其他主题的一般问题。输入应为搜索查询。

- 注释：使用[wikipedia](https://pypi.org/project/wikipedia/) Python包调用MediaWiki API，然后解析结果。

- 需要LLM：否

- 额外参数：`top_k_results`



**podcast-api**



- 工具名称：Podcast API

- 工具描述：使用Listen Notes Podcast API搜索所有播客或剧集。输入应为此API可以回答的自然语言问题。

- 注释：与Listen Notes Podcast API（https://www.PodcastAPI.com）的自然语言连接，特别是`/search/`终点。

- 需要LLM：是

- 额外参数：`listen_api_key`（访问此终点的API密钥）



**openweathermap-api**



- 工具名称：OpenWeatherMap

- 工具描述：OpenWeatherMap API的包装器。用于获取指定位置的当前天气信息。输入应为位置字符串（例如London,GB）。

- 注释：与OpenWeatherMap API（https://api.openweathermap.org）的连接，特别是`/data/2.5/weather`终点。

- 需要LLM：否

- 额外参数：`openweathermap_api_key`（访问此终点的API密钥）



**sleep**



- 工具名称：睡眠

- 工具描述：使代理人休眠一段时间。

- 需要LLM：否

