# 起步


工具是代理可以用来与世界交互的函数。
这些工具可以是通用工具（例如搜索）,其他链,甚至其他代理。


目前，可以使用以下代码片段加载工具:


```python

from langchain.agents import load_tools

tool_names = [...]

tools = load_tools(tool_names)

```



一些工具（例如链,代理）可能需要基本LLM才能使用以初始化它们。
在这种情况下，您也可以传递LLM:


```python

from langchain.agents import load_tools

tool_names = [...]

llm = ...

tools = load_tools(tool_names, llm=llm)

```



下面是所有支持的工具及相关信息的列表:


- 工具名称: LLM引用工具的名称。
- 工具描述: 传递给LLM的工具描述。
- 注释: 有关工具的注释，不会传递给LLM。
- 需要LLM: 此工具是否需要初始化LLM。
- （可选）额外参数: 初始化此工具所需的其他参数。


## 工具列表


**python_repl**


- 工具名称: Python REPL
- 工具描述: 一个Python shell。使用它来执行Python命令。输入应该是一个有效的Python命令。如果您期望输出，应该打印出来。
- 注释: 保持状态。
- 需要LLM: 否


**serpapi**


- 工具名称: 搜索
- 工具描述: 一个搜索引擎。当您需要回答关于当前事件的问题时有用。输入应该是一个搜索查询。
- 注释: 调用Serp API，然后解析结果。
- 需要LLM: 否


**wolfram-alpha**


- Tool Name: Wolfram Alpha

- 工具描述: 一个 Wolfram Alpha 搜索引擎。当你需要回答关于数学,科学,技术,文化,社会和日常生活的问题时非常有用。输入应该是一个搜索查询。
- 注解: 调用 Wolfram Alpha API 然后解析结果。
- 需要 LLM: 否
- 额外参数: `wolfram_alpha_appid`: Wolfram Alpha 应用 ID。

**requests**

- 工具名称: 请求
- 工具描述: 一个访问互联网的门户网站。当你需要从一个站点获取特定内容时使用。输入应该是一个特定的 url，输出将是该页面上的所有文本。
- 注解: 使用 Python requests 模块。
- 需要 LLM: 否

**terminal**

- 工具名称: 终端
- 工具描述: 在终端中执行命令。输入应该是有效的命令，而输出将是运行该命令所产生的所有输出。
- 注解: 使用 subprocess 执行命令。
- 需要 LLM: 否

**pal-math**

- 工具名称: PAL-MATH
- 工具描述: 一个优秀的语言模型，可以解决复杂的单词数学问题。输入应该是一个完全字词化的艰难数学问题。
- 注解: 基于 [这篇论文](https://arxiv.org/pdf/2211.10435.pdf)。
- 需要 LLM: 是

**pal-colored-objects**

- 工具名称: PAL-COLOR-OBJ
- 工具描述: 一个优秀的语言模型，可以处理关于物体位置和颜色属性的推理问题。输入应该是一个完全字词化的艰难推理问题。确保包括有关物体和最终要回答的问题的所有信息。
- 注解: 基于 [这篇论文](https://arxiv.org/pdf/2211.10435.pdf)。
- 需要 LLM: 是

**llm-math**


- 工具名称: 计算器
- 工具说明: 在需要回答与数学有关的问题时非常有用。
- 备注: 属于 `LLMMath` 链的一个实例。
- 需要 LLM: 是

**open-meteo-api**

- 工具名称: Open Meteo API
- 工具说明: 当你需要从 OpenMeteo API 获取天气信息时非常有用。输入应为该 API 可以回答的自然语言问题。
- 备注: 是一个自然语言连接到 Open Meteo API (`https://api.open-meteo.com/`) ,具体是 `/v1/forecast` 端点。
- 需要 LLM: 是

**news-api**

- 工具名称: 新闻 API
- 工具说明: 当你想要获取有关当前新闻故事的头条新闻的信息时，请使用此工具。输入应为该 API 可以回答的自然语言问题。
- 备注: 是一个自然语言连接到新闻 API (`https://newsapi.org`) ,具体是 `/v2/top-headlines` 端点。
- 需要 LLM: 是
- 额外参数: `news_api_key`（访问此端点的 API 密钥）

**tmdb-api**

- 工具名称: TMDB API
- 工具说明: 当你需要从电影数据库中获取信息时非常有用。输入应为该 API 可以回答的自然语言问题。
- 备注: 是一个自然语言连接到 TMDB API (`https://api.themoviedb.org/3`) ,具体是 `/search/movie` 端点。
- 需要 LLM: 是
- 额外参数: `tmdb_bearer_token`（访问此端点的 Bearer Token - 请注意，这与 API 密钥不同）

**google-search**

- Tool Name: Search

- 工具描述: Google搜索的封装。需要回答有关当前事件的问题时非常有用。输入应该是一个搜索查询。
- 注意事项: 使用Google自定义搜索API
- 需要LLM: 不需要
- 额外参数: `google_api_key`, `google_cse_id`
- 欲了解更多信息，请参见[此页面](../../../integrations/google_search.md)


**searx-search**


- 工具名称: 搜索
- 工具描述: 一个SearxNG元搜索引擎的封装。输入应该是一个搜索查询。
- 注意事项: SearxNG易于部署自托管。它是一个良好的隐私友好型替代品，用于Google搜索。使用SearxNG API。
- 需要LLM: 不需要
- 额外参数: `searx_host`


**google-serper**


- 工具名称: 搜索
- 工具描述: 低成本的Google搜索API。需要回答有关当前事件的问题时非常有用。输入应该是一个搜索查询。
- 注意事项: 调用[serper.dev](https://serper.dev)的Google搜索API，然后解析结果。
- 需要LLM: 不需要
- 额外参数: `serper_api_key`
- 欲了解更多信息，请参见[此页面](../../../integrations/google_serper.md)


**wikipedia**


- 工具名称: 维基百科
- 工具描述: 维基百科的一个封装。需要回答有关人物、地点、公司、历史事件或其他主题的一般问题时非常有用。输入应该是一个搜索查询。
- 注意事项: 使用[wikipedia](https://pypi.org/project/wikipedia/) Python包调用MediaWiki API，然后解析结果。
- 需要LLM: 不需要
- 额外参数: `top_k_results`


**podcast-api**



- 工具名称: Podcast API
- 工具描述: 使用 Listen Notes Podcast API 搜索所有播客或剧集。输入应该是此 API 可以回答的自然语言问题。
- 备注: 是一个与 Listen Notes Podcast API（`https://www.PodcastAPI.com`）特定的 `/search/` 端点相连的自然语言连接。
- 需要 LLM: 是
- 额外参数: `listen_api_key`（访问此端点的 API 密钥）

**openweathermap-api**

- 工具名称: OpenWeatherMap
- 工具描述: 包装了 OpenWeatherMap API。有助于获取指定位置的当前天气信息。输入应该是位置字符串（例如伦敦,GB）。
- 备注: 与 OpenWeatherMap API（https://api.openweathermap.org）特定的 `/data/2.5/weather` 端点相连。
- 需要 LLM: 否
- 额外参数: `openweathermap_api_key`（访问此端点的 API 密钥）

**sleep**

- 工具名称: Sleep
- 工具描述: 让代理程序休眠一段时间。
- Requires LLM: No

