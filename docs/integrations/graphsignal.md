# Graphsignal图信号

This page covers how to use [Graphsignal](https://app.graphsignal.com) to trace and monitor LangChain. Graphsignal enables full visibility into your application. It provides latency breakdowns by chains and tools, exceptions with full context, data monitoring, compute/GPU utilization, OpenAI cost analytics, and more.本页面介绍如何使用 [图信号](https://app.graphsignal.com) 来跟踪和监视 LangChain。图信号可以全面了解您的应用程序。它提供了链式延迟中断和工具带有完整上下文的异常数据监视, 计算/GPU 利用率, OpenAI 成本分析等功能。

## Installation and Setup安装与设置

- Install the Python library with `pip install graphsignal`使用 `pip install graphsignal` 安装 Python 库
- Create free Graphsignal account [here](https://graphsignal.com)在此处创建免费的图信号帐户 [here](https://graphsignal.com)
- Get an API key and set it as an environment variable (`GRAPHSIGNAL_API_KEY`)获取 API Key 并将其设置为环境变量 （`GRAPHSIGNAL_API_KEY`）

## Tracing and Monitoring跟踪和监视

Graphsignal automatically instruments and starts tracing and monitoring chains. Traces and metrics are then available in your [Graphsignal dashboards](https://app.graphsignal.com).图信号自动对链进行仪器化并开始跟踪和监视。然后可以在您的 [图信号仪表板](https://app.graphsignal.com) 中使用跟踪和度量。

Initialize the tracer by providing a deployment name:通过提供部署名称来初始化跟踪器

```python
import graphsignal



graphsignal.configure(deployment='my-langchain-app-prod')

```


To additionally trace any function or code, you can use a decorator or a context manager:此外，要跟踪任何函数或代码，可以使用装饰器或上下文管理器。

```python
:graphsignal.trace_function

def handle_request():    

    chain.run("some initial text")

```


```python
with graphsignal.start_trace('my-chain'):

    chain.run("some initial text")

```


Optionally, enable profiling to record function-level statistics for each trace.可以选择启用分析以记录每个跟踪的函数级统计信息。

```python
with graphsignal.start_trace(

        'my-chain', options=graphsignal.TraceOptions(enable_profiling=True)):

    chain.run("some initial text")

```


See the [Quick Start](https://graphsignal.com/docs/guides/quick-start/) guide for complete setup instructions.

