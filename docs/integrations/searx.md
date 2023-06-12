# SearxNG 搜索API


本页面介绍如何在LangChain中使用SearxNG搜索API。
它分为两个部分，安装和设置，然后引用特定的SearxNG API包装器。


## 安装和设置


虽然可以与[公共searx实例](https://searx.space/)一起使用包装器，但这些实例通常不允许API访问（请参阅下面有关输出格式的注释），并且在请求频率上有限制。建议选择自托管实例。
instances](https://searx.space/) these instances frequently do not permit API

access (see note on output format below) and have limitations on the frequency

建议选择自托管实例。


### 自托管实例


请参阅[此页面](https://searxng.github.io/searxng/admin/installation.html)获取安装说明。


安装SearxNG后，默认情况下仅有HTML格式是活动的输出格式。您需要激活'json'格式以使用API。这可以通过将以下行添加到“settings.yml”文件中来完成。
You need to activate the `json` format to use the API. This can be done by adding the following line to the `settings.yml` file:

```yaml
search:

    formats:

        - html

        - json

```

您可以通过向API端点发出curl请求来确保API正常工作。 


`curl -kLX GET --data-urlencode q = 'langchain' -d format = json http：// localhost : 8888`


这应该返回一个带有结果的JSON对象。




## 包装器


### 实用程序


要使用包装器，我们需要将SearxNG实例的主机传递给包装器。
    1. the named parameter `searx_host` when creating the instance.

    2. exporting the environment variable `SEARXNG_HOST`.



您可以使用包装器从SearxNG实例中获取结果。


```python
from langchain.utilities import SearxSearchWrapper

s = SearxSearchWrapper(searx_host="http://localhost:8888")

s.run("what is a large language model?")

```



### 工具


您还可以将此包装器加载为工具（与代理一起使用）。


可以通过以下方式完成：


```python
from langchain.agents import load_tools

tools = load_tools(["searx-search"],

                    searx_host="http://localhost:8888",

                    engines=["github"])

```



Note that we could _optionally_ pass custom engines to use.



如果您想获得具有元数据的结果，可以使用 *json* 格式，可以使用:
```python
tools = load_tools(["searx-search-results-json"],

                    searx_host="http://localhost:8888",

                    num_results=5)

```


For more information on tools, see [this page](../modules/agents/tools/getting_started.md)

