# Graphsignal图信号



本页面介绍如何使用[Graphsignal](https://app.graphsignal.com)来跟踪和监控LangChain。Graphsignal可以全面查看您的应用程序，提供链路和工具的延迟分解、带有完整上下文的异常、数据监控、计算/ GPU利用率、OpenAI成本分析等。



## 安装和设置



- 使用`pip install graphsignal`命令安装Python库

- 在此处创建免费的Graphsignal账号[此处](https://graphsignal.com)

- 获取一个API密钥并将其设置为环境变量(`GRAPHSIGNAL_API_KEY`)



## 跟踪和监控



Graphsignal会自动插入仪器并开始跟踪和监控链路。然后，跟踪和度量指标将在您的[Graphsignal仪表板](https://app.graphsignal.com)中可用。



通过提供部署名称来初始化跟踪器:



```python

import graphsignal



graphsignal.configure(deployment='my-langchain-app-prod')

```



要额外跟踪任何函数或代码，可以使用装饰器或上下文管理器:



```python

@graphsignal.trace_function

def handle_request():    

    chain.run("一些初始文本")

```



```python

with graphsignal.start_trace('my-chain'):

    chain.run("一些初始文本")

```



可选择启用性能分析，以记录每个跟踪的函数级统计信息。



```python

with graphsignal.start_trace(

        'my-chain', options=graphsignal.TraceOptions(enable_profiling=True)):

    chain.run("一些初始文本")

```



参阅[快速入门](https://graphsignal.com/docs/guides/quick-start/)指南以获取完整的设置说明。

