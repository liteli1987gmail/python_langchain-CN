SearxNG搜索API


本页面介绍如何在LangChain中使用SearxNG搜索API。
它分为两部分：安装和设置，以及对特定SearxNG API包装器的引用。


安装和设置


虽然可以将包装器与公共searx实例](https://searx.space/)结合使用，但这些实例经常不允许API访问（有关输出格式的注意事项请参见下面的注释），并且对请求的频率有限制。建议选择自托管实例。
instances](https://searx.space/) these instances frequently do not permit API

access (see note on output format below) and have limitations on the frequency

of requests. It is recommended to opt for a self-hosted instance instead.



自托管实例：


请参阅此页面](https://searxng.github.io/searxng/admin/installation.html)了解安装说明。


安装SearxNG时，默认情况下仅激活HTML格式的输出格式。需要激活`json`格式以使用API。您可以通过将以下行添加到`settings.yml`文件中来完成此操作：
You need to activate the `json` format to use the API. This can be done by adding the following line to the `settings.yml` file:

```yaml

search:

    formats:

        - html

        - json

```

您可以通过向API端点发出curl请求来确保API正在工作：


`curl -kLX GET --data-urlencode q='langchain' -d format=json http://localhost:8888`


这应该返回一个带有结果的JSON对象。




包装器


实用工具


要使用包装器，我们需要使用以下方式将SearxNG实例的主机传递给包装器：
    1. 创建实例时，使用命名参数`searx_host`。

    2. 导出环境变量`SEARXNG_HOST`。



您可以使用包装器从SearxNG实例获得结果。


```python

from langchain.utilities import SearxSearchWrapper

s = SearxSearchWrapper(searx_host="http://localhost:8888")

s.run("what is a large language model?")

```



工具


您还可以将此包装器作为工具加载（与代理一起使用）。


您可以通过以下方式实现：


```python

from langchain.agents import load_tools

tools = load_tools(["searx-search"],

                    searx_host="http://localhost:8888",

                    engines=["github"])

```



请注意，我们可以选择性地传递自定义引擎以使用。


如果您想要获得带有*json*元数据的结果，可以使用：
```python

tools = load_tools(["searx-search-results-json"],

                    searx_host="http://localhost:8888",

                    num_results=5)

```



有关工具的更多信息，请参见此页面](../modules/agents/tools/getting_started.md)
