# Graphsignal



本页面介绍如何使用[Graphsignal](https://app.graphsignal.com)来追踪和监控LangChain。Graphsignal可以全面了解您的应用程序。它提供了按链和工具的延迟分解、带有完整上下文的异常、数据监控、计算/GPU利用率、OpenAI成本分析等功能。



## 安装和设置



- 使用`pip install graphsignal`安装Python库

- 在[此处](https://graphsignal.com)创建免费的Graphsignal账户

- 获取一个API密钥，并将其设置为环境变量（`GRAPHSIGNAL_API_KEY`）



## 追踪和监控



Graphsignal会自动进行仪器化，并开始追踪和监控链。然后，跟踪和指标可在您的[Graphsignal仪表板](https://app.graphsignal.com)中使用。



通过提供部署名称来初始化跟踪器：



```python

import graphsignal



graphsignal.configure(deployment='my-langchain-app-prod')

```



如果需要追踪任何函数或代码，可以使用装饰器或上下文管理器：



```python

@graphsignal.trace_function

def handle_request():    

    chain.run("some initial text")

```



```python

with graphsignal.start_trace('my-chain'):

    chain.run("some initial text")

```



可选择启用性能分析，以记录每个跟踪的函数级统计信息。



```python

with graphsignal.start_trace(

        'my-chain', options=graphsignal.TraceOptions(enable_profiling=True)):

    chain.run("some initial text")

```



有关完整设置说明，请参阅[快速入门](https://graphsignal.com/docs/guides/quick-start/)指南。

