入门指南



工具是代理可以用来与世界互动的功能。

这些工具可以是通用实用程序（例如搜索），其他链条，甚至其他代理。



目前，可以使用以下代码片段加载工具：



```python

from langchain.agents import load_tools

tool_names = [...]

tools = load_tools(tool_names)

```



一些工具（例如链条，代理）可能需要基本的LLM来使用以初始化它们。

在这种情况下，您也可以传递LLM：



```python

from langchain.agents import load_tools

tool_names = [...]

llm = ...

tools = load_tools(tool_names, llm=llm)

```



以下是所有支持的工具及相关信息的列表：



- 工具名称：LLM通过此名称引用工具。

- 工具描述：传递给LLM的工具描述。

- 备注：不会传递给LLM的工具备注。

- 需要LLM：此工具是否需要初始化LLM。

- （可选）额外参数：初始化此工具需要哪些额外参数。



## 工具列表



**python_repl**



- 工具名称：Python REPL

- 工具描述：Python shell。使用它执行Python命令。输入应该是有效的Python命令。如果期望输出，则应打印出来。

- 备注：保持状态。

- 需要LLM：否



**serpapi**



- 工具名称：搜索

- 工具描述：搜索引擎。在需要回答有关当前事件的问题时很有用。输入应该是搜索查询。

- 备注：调用Serp API，然后解析结果。

- 需要LLM：否



**wolfram-alpha**



- 工具名称：Wolfram Alpha

- 工具描述：Wolfram Alpha搜索引擎。在需要回答关于数学、科学、技术、文化、社会和日常生活的问题时很有用。输入应该是搜索查询。

- 备注：调用Wolfram Alpha API，然后解析结果。

- 需要LLM：否

- 额外参数：`wolfram_alpha_appid`：Wolfram Alpha应用程序ID。



**requests**



- 工具名称：Requests

- 工具描述：访问互联网的门户。当需要从网站获取特定内容时使用。输入应该是一个特定的URL，输出将是该页面上的所有文本。

- 备注：使用Python的requests模块。

- 需要LLM：否



**terminal**



- 工具名称：终端

- 工具描述：在终端中执行命令。输入应该是有效的命令，输出将是运行该命令的任何输出。

- 备注：使用subprocess执行命令。

- 需要LLM：否



**pal-math**



- 工具名称：PAL-MATH

- 工具描述：一个在解决复杂词汇数学问题方面表现出色的语言模型。输入应该是一个完全具有挑战性的词汇数学问题。

- 备注：基于这篇论文](https://arxiv.org/pdf/2211.10435.pdf)。

- 需要LLM：是



**pal-colored-objects**



- 工具名称：PAL-COLOR-OBJ

- 工具描述：一个出色地推理物体位置和颜色属性的语言模型。输入应该是一个完全描述场景和所需回答的最终问题的复杂推理问题。

- 备注：基于这篇论文](https://arxiv.org/pdf/2211.10435.pdf)。

- 需要LLM：是



**llm-math**



- 工具名称：计算器

- 工具描述：用于回答数学问题。

- 备注：LLMMath链条的一种实例。

- 需要LLM：是



**open-meteo-api**



- 工具名称：Open Meteo API

- 工具描述：从OpenMeteo API获取天气信息时很有用。输入应该是这个API可以回答的自然语言问题。

- 备注：与Open Meteo API (`https://api.open-meteo.com/`) 的自然语言连接，具体是 `/v1/forecast` 端点。

- 需要LLM：是



**news-api**



- 工具名称：News API

- 工具描述：当您想要获取有关当前新闻头条的信息时，请使用它。输入应该是这个API可以回答的自然语言问题。

- 备注：与News API (`https://newsapi.org`) 的自然语言连接，具体是 `/v2/top-headlines`  端点。

- 需要LLM：是

- 额外参数：`news_api_key`（用于访问此端点的API密钥）



**tmdb-api**



- 工具名称：TMDB API

- 工具描述：当您想要从The Movie Database获取信息时请使用它。输入应该是这个API可以回答的自然语言问题。

- 备注：与TMDB API (`https://api.themoviedb.org/3`) 的自然语言连接，具体是 `/search/movie` 端点。

- 需要LLM：是

- 额外参数：`tmdb_bearer_token`（用于访问此端点的Bearer令牌 - 请注意，这与API密钥不同）



**google-search**



- 工具名称：搜索

- 工具描述：Google搜索的封装。当您需要回答有关当前事件的问题时很有用。输入应该是搜索查询。

- 备注：使用Google Custom Search API

- 需要LLM：否

- 额外参数：`google_api_key`，`google_cse_id`

- 有关此信息，请参阅此页面](../../../integrations/google_search.md)



**searx-search**



- 工具名称：搜索

- 工具描述：SearxNG元搜索引擎的封装。输入应该是搜索查询。

- 备注：SearxNG易于部署的自托管解决方案。是Google搜索的良好隐私友好替代品。使用SearxNG API。

- 需要LLM：否

- 额外参数：`searx_host`



**google-serper**



- 工具名称：搜索

- 工具描述：一种低成本的Google搜索API。当您需要回答有关当前事件的问题时很有用。输入应该是搜索查询。

- 备注：调用serper.dev](https://serper.dev)的Google搜索API，然后解析结果。

- 需要LLM：否

- 额外参数：`serper_api_key`

- 有关此信息，请参阅此页面](../../../integrations/google_serper.md)



**wikipedia**



- 工具名称：Wikipedia

- 工具描述：维基百科的封装。回答关于人物、地点、公司、历史事件或其他主题的一般问题时很有用。输入应该是搜索查询。

- 备注：使用wikipedia](https://pypi.org/project/wikipedia/) Python软件包调用MediaWiki API，然后解析结果。

- 需要LLM：否

- 额外参数：`top_k_results`



**podcast-api**



- 工具名称：Podcast API

- 工具描述：使用Listen Notes Podcast API搜索所有播客或剧集。输入应该是这个API可以回答的自然语言问题。

- 备注：与Listen Notes Podcast API (`https://www.PodcastAPI.com`) 的自然语言连接，具体是 `/search/` 端点。

- 需要LLM：是

- 额外参数：`listen_api_key`（访问此端点的API密钥）



**openweathermap-api**



- 工具名称：OpenWeatherMap

- 工具描述：OpenWeatherMap API的封装。用于获取指定位置的当前天气信息。输入应该是位置字符串（例如London,GB）。

- 备注：与OpenWeatherMap API (https://api.openweathermap.org) 的连接，具体是 `/data/2.5/weather` 端点。

- 需要LLM：否

- 额外参数：`openweathermap_api_key`（访问此端点的API密钥）



**sleep**



- 工具名称：Sleep

- 工具描述：使代理休眠一段时间。

- 需要LLM：否

