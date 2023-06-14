跟踪


通过在LangChain运行中启用跟踪，您将能够更有效地可视化、逐步进行和调试您的链和代理。


首先，您应该安装跟踪并正确设置您的环境。
您可以使用本地托管版本（使用Docker）或云托管版本（封闭alpha）的任一版本。
如果您有兴趣使用托管平台，请在此处填写表单（https://forms.gle/tRCEMSeopZf6TE3b6）。


-本地托管设置](../tracing/local_installation.md)
-云托管设置](../tracing/hosted_installation.md)


跟踪演练


当您首次访问UI时，您应该看到一个包含跟踪会话的页面。
一个初始的"默认"会话应该已经为您创建。
会话只是一种将跟踪分组在一起的方式。
如果单击会话，它将带您进入一个没有记录的跟踪的页面，上面写着"没有运行"。
您可以使用新的会话表单创建新的会话。


![](../tracing/homepage.png)



如果我们单击"默认"会话，我们会看到开始时没有存储的跟踪。


![](../tracing/default_empty.png)



如果我们现在启用跟踪，运行链和代理，我们将在这里看到数据出现。
为了这样做，我们可以运行此笔记本](../tracing/agent_with_tracing.ipynb)作为示例。
运行后，我们将看到一个初始的跟踪显示出来。


![](../tracing/first_trace.png)



从这里，我们可以通过点击箭头以显示嵌套运行来高层次地探索跟踪。
我们可以不断点击下去，深入探索更深入的情况。


![](../tracing/explore.png)



我们还可以点击顶级运行的"探索"按钮，更深入地钻研。
在这里，我们可以完整地查看输入和输出，以及所有嵌套跟踪。


![](../tracing/explore_trace.png)



我们可以继续深入探索每一个嵌套跟踪的细节。
例如，这是最低级别跟踪，显示了与LLM的确切输入/输出。


![](../tracing/explore_llm.png)



更改会话


1. 要将跟踪记录到除"默认"之外的其他会话，请将`LANGCHAIN_SESSION`环境变量设置为要记录到的会话的名称：


```python

import os

os.environ["LANGCHAIN_TRACING"] = "true"

os.environ["LANGCHAIN_SESSION"] = "my_session" # Make sure this session actually exists. You can create a new session in the UI.

```



2. 要在脚本或笔记本的中途切换会话，请不要设置`LANGCHAIN_SESSION`环境变量。而是使用`langchain.set_tracing_callback_manager(session_name="my_session")`
