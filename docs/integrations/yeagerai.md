# Yeager.ai


本页介绍如何使用 [Yeager.ai](https://yeager.ai) 生成 LangChain 工具和代理。


## 什么是 Yeager.ai？
Yeager.ai 是一个生态系统，旨在简化创建人工智能代理和工具的过程。


它具有 yAgents，一款无代码 LangChain 代理构建器，使用户可以轻松构建、测试和部署人工智能解决方案。利用 LangChain 框架，yAgents 允许与各种语言模型和资源无缝集成，适用于开发人员、研究人员和人工智能爱好者在各种应用程序中的应用。


## yAgents
低代码生成代理，旨在帮助您轻松构建、原型和部署 Langchain 工具。


### 如何使用？
```

pip install yeagerai-agent

yeagerai-agent

```

转到 http://127.0.0.1:7860


这将安装必要的依赖项并在系统上设置 yAgents。第一次运行后，yAgents 将创建一个 .env 文件，在其中您可以输入您的 OpenAI API 密钥。您也可以直接从 Gradio 界面下的 \"设置\" 选项卡中执行相同操作。


`OPENAI_API_KEY=<your_openai_api_key_here>`


我们建议使用 GPT-4。但是，如果问题被充分拆分，该工具也可以使用 GPT-3。


### 使用 yAgents 创建和执行工具
yAgents 可以轻松创建和执行人工智能工具。以下是此过程的简要概述：
1. 创建工具: 要创建工具，请向 yAgents 提供自然语言提示。提示应清楚地描述工具的目的和功能。例如：
`创建一个返回第 n 个质数的工具`


2. 将工具加载到工具包中: 只需向yAgents提供一个命令即可将工具加载到yAgents中。例如:
`将您刚刚创建的工具加载到您的工具包中`

3. 执行工具: 要运行工具或代理，只需向yAgents提供一个包括工具名称和任何必需参数的命令即可。例如:
`生成第50个质数`

您可以在[这里](https://www.youtube.com/watch?v=KA5hCM3RaWE)观看其工作视频。

随着您对yAgents的熟悉程度增加，您可以创建更高级的工具和代理来自动化您的工作，增强您的生产力。

更多信息，请参见[yAgents的Github](https://github.com/yeagerai/yeagerai-agent)或我们的[文档](https://yeagerai.gitbook.io/docs/general/welcome-to-yeager.ai)



