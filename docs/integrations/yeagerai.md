Yeager.ai



本页面介绍如何使用Yeager.ai](https://yeager.ai)生成LangChain工具和代理。



什么是Yeager.ai?

Yeager.ai是一个旨在简化创建AI代理和工具过程的生态系统。



它具有yAgents，一个无代码LangChain代理构建器，使用户能够轻松构建、测试和部署AI解决方案。利用LangChain框架，yAgents可以无缝集成各种语言模型和资源，适用于开发人员、研究人员和各种应用领域的AI爱好者。



yAgents

低代码生成的代理，旨在帮助您轻松构建、原型化和部署Langchain工具。



如何使用?

```

pip install yeagerai-agent

yeagerai-agent

```

访问 http://127.0.0.1:7860



这将安装必要的依赖项并在您的系统上设置yAgents。第一次运行后，yAgents将创建一个.env文件，您可以在其中输入您的OpenAI API密钥。您还可以直接从Gradio界面的“Settings”选项卡中完成相同操作。



`OPENAI_API_KEY=<your_openai_api_key_here>`



我们建议使用GPT-4，但如果问题被充分分解，该工具也可以与GPT-3一起使用。



使用yAgents创建和执行工具

yAgents简化了创建和执行基于AI的工具。以下是简要概述的过程：

1. 创建一个工具：要创建一个工具，向yAgents提供一个自然语言提示。提示应清楚地描述工具的目的和功能。例如：

`create a tool that returns the n-th prime number`



2. 将工具加载到工具包中：要将工具加载到yAgents中，只需向yAgents提供一个相应的命令即可。例如：

`load the tool that you just created it into your toolkit`



3. 执行工具：要运行一个工具或代理，只需向yAgents提供一个包含工具名称和任何必需参数的命令即可。例如：

`generate the 50th prime number`



您可以在此处](https://www.youtube.com/watch?v=KA5hCM3RaWE)查看它的工作视频。



随着对yAgents的熟悉程度越来越高，您可以创建更高级的工具和代理来自动化您的工作并提高您的生产力。



更多信息，请参阅yAgents的Github](https://github.com/yeagerai/yeagerai-agent)或我们的文档](https://yeagerai.gitbook.io/docs/general/welcome-to-yeager.ai)





