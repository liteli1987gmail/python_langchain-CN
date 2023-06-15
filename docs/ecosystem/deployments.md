# 部署



那么，你已经创建了一个非常酷的链 - 现在怎么办？如何部署它并与世界轻松共享？



本章介绍了几种选项。请注意，这些选项仅用于快速部署原型和演示，不适用于生产系统。如果您需要部署生产系统的帮助，请直接与我们联系。



以下是一份模板 GitHub 代码仓库列表，旨在易于派生和修改以使用您的链。该列表远非详尽无遗，我们非常欢迎贡献。



## [Anyscale](https://www.anyscale.com/model-serving)



Anyscale是一个统一的计算平台，使用Ray可以轻松开发、部署和管理可扩展的LLM应用程序。

在Anyscale上，您可以扩展最具挑战性的基于LLM的工作负载，并在单个计算平台上开发和部署基于LLM的应用程序。



## [Streamlit](https://github.com/hwchase17/langchain-streamlit-template)



这个仓库作为一个模板，展示了如何使用Streamlit部署LangChain。

它实现了一个聊天机器人接口。

它还包含了在Streamlit平台上部署此应用程序的说明。



## [Gradio（在Hugging Face上）](https://github.com/hwchase17/langchain-gradio-template)



这个仓库作为一个模板，展示了如何使用Gradio部署LangChain。

它实现了一个聊天机器人接口，采用“自带令牌”的方式（可避免产生大额账单）。

它还包含了在Hugging Face平台上部署此应用程序的说明。

这受到James Weaver的优秀示例的很大影响。



## [Chainlit](https://github.com/Chainlit/cookbook)



这个仓库是一个说明书，详细说明了如何使用Chainlit可视化和部署LangChain代理。

您可以使用Chainlit创建类似ChatGPT的用户界面。一些关键功能包括中间步骤可视化、元素管理和显示（图像、文本、轮播等），以及云部署。

有关与LangChain集成的Chainlit文档



## [Beam](https://github.com/slai-labs/get-beam/tree/main/examples/langchain-question-answering)



这个仓库作为一个模板，展示了如何使用Beam部署LangChain。



它实现了一个问答应用，并包含部署该应用作为无服务器REST API的说明。



## [Vercel](https://github.com/homanp/vercel-langchain)



展示如何使用Flask在Vercel上运行LangChain的最小示例。



## [FastAPI + Vercel](https://github.com/msoedov/langcorn)



展示了使用FastAPI和LangCorn/Uvicorn在Vercel上运行LangChain的最小示例。



## [Kinsta](https://github.com/kinsta/hello-world-langchain)



展示了如何使用Flask在[Kinsta](https://kinsta.com)上部署LangChain的最小示例。



## [Fly.io](https://github.com/fly-apps/hello-fly-langchain)



展示了如何使用Flask在[Fly.io](https://fly.io/)上部署LangChain的最小示例。



## [Digitalocean App Platform](https://github.com/homanp/digitalocean-langchain)



展示了如何部署LangChain到DigitalOcean App Platform的最小示例。



## [Google Cloud Run](https://github.com/homanp/gcp-langchain)



展示了如何部署LangChain到Google Cloud Run的最小示例。



## [SteamShip](https://github.com/steamship-core/steamship-langchain/)



这个仓库包含了LangChain适配器，可以让LangChain开发者快速部署他们的应用程序到SteamShip上。这包括：面向生产的端点、跨依赖项的水平扩展、应用程序状态的持久化存储、多租户支持等。



## [Langchain-serve](https://github.com/jina-ai/langchain-serve)



这个仓库允许用户将本地链和代理作为RESTful、gRPC或WebSocket API提供，感谢[Jina](https://docs.jina.ai/)。轻松部署您的链和代理，享受独立扩展、无服务器和自动缩放的API，以及Jina AI云上的Streamlit游乐场。



## [BentoML](https://github.com/ssheng/BentoChain)



这个仓库提供了使用[BentoML](https://github.com/bentoml/BentoML)部署LangChain应用程序的示例。BentoML是一个将机器学习应用程序容器化为标准OCI镜像的框架。BentoML还允许自动生成OpenAPI和gRPC端点。使用BentoML，您可以集成来自所有流行ML框架的模型，并将其部署为在最优硬件上独立扩展的微服务。



## [Databutton](https://databutton.com/home?new-data-app=true)



这些模板示例演示了如何使用Databutton构建、部署和共享LangChain应用程序。您可以使用Streamlit创建用户界面，通过调度Python代码自动化任务，并将文件和数据存储在内置存储中。示例包括具有对话内存的聊天机器人界面、个人搜索引擎以及LangChain应用程序的起始模板。轻松部署和共享，只需轻轻一点。

