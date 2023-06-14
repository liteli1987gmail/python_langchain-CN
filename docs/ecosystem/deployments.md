# 部署


所以，你创建了一条非常酷的链 - 然后呢？如何部署它并使其与世界轻松共享？


本节介绍了几种选项。请注意，这些选项适用于原型和演示快速部署，而不适用于生产系统。如果您需要部署生产系统的帮助，请直接与我们联系。


下面是一系列的模板 GitHub 仓库列表，旨在便于分叉和修改以使用您的链。这个列表远远不全面，我们非常欢迎在这方面的贡献。


## [Anyscale](https://www.anyscale.com/model-serving)
（Anyscale）


Anyscale 是一个统一的计算平台，使用 Ray 在生产中开发、部署和管理可扩展的 LLM 应用程序非常容易。
使用 Anyscale，您可以对最具挑战性的基于 LLM 的工作负载进行扩展，并在单个计算平台上开发和部署基于 LLM 的应用程序。


## [Streamlit](https://github.com/hwchase17/langchain-streamlit-template)
（Streamlit）


该存储库作为使用 Streamlit 部署 LangChain 的模板。
它实现了一个聊天机器人界面。
还包含有关如何在 Streamlit 平台上部署此应用程序的说明。


## [Gradio（在 Hugging Face 上）](https://github.com/hwchase17/langchain-gradio-template)
（Gradio）


该存储库作为使用 Gradio 部署 LangChain 的模板。
它实现了一个聊天机器人界面，采用“自带令牌”方法（对不产生大额帐单很好）。
还包含有关如何在 Hugging Face 平台上部署此应用程序的说明。
这受到 James Weaver 的 [excellent examples](https://huggingface.co/JavaFXpert) 的很大影响。


## [Chainlit](https://github.com/Chainlit/cookbook)
（Chainlit）


这个存储库是一个介绍如何使用 Chainlit 可视化和部署 LangChain 代理的食谱。
使用 Chainlit，您可以创建类似于 ChatGPT 的用户界面。其中一些关键功能包括中间步骤可视化，元素管理和显示（图像、文本、轮播等），以及云部署。
Chainlit [doc](https://docs.chainlit.io/langchain) 对 LangChain 集成的介绍


## [Beam](https://github.com/slai-labs/get-beam/tree/main/examples/langchain-question-answering)
（Beam）


该存储库作为使用 [Beam](https://beam.cloud) 部署 LangChain 的模板。


它实现了一个问答应用程序，并包含有关如何将应用程序部署为无服务器 REST API 的说明。


## [Vercel](https://github.com/homanp/vercel-langchain)
（Vercel）


一个关于如何使用 Flask 在 Vercel 上运行 LangChain 的最小示例。


## [FastAPI + Vercel](https://github.com/msoedov/langcorn)
（FastAPI + Vercel）


一个关于如何使用 FastAPI 和 LangCorn/Uvicorn 在 Vercel 上运行 LangChain 的最小示例。


## [Kinsta](https://github.com/kinsta/hello-world-langchain)
（Kinsta）


一个关于如何使用 Flask 在 [Kinsta](https://kinsta.com) 上部署 LangChain 的最小示例。


## [Fly.io](https://github.com/fly-apps/hello-fly-langchain)
（Fly.io）


一个关于如何使用 Flask 在 [Fly.io](https://fly.io/) 上部署 LangChain 的最小示例。


## [Digitalocean App Platform](https://github.com/homanp/digitalocean-langchain)
（Digitalocean App Platform）


一个关于如何将 LangChain 部署到 DigitalOcean App Platform 的最小示例。


## [Google Cloud Run](https://github.com/homanp/gcp-langchain)
（Google Cloud Run）


一个关于如何将 LangChain 部署到 Google Cloud Run 的最小示例。


## [SteamShip](https://github.com/steamship-core/steamship-langchain/)
（SteamShip）


该存储库包含 Steamship 的 LangChain 适配器，使 LangChain 开发人员能够快速部署其应用程序。这包括：为依赖项实现就绪的端点、跨依赖项的水平扩展、应用程序状态的持久化存储、多租户支持等。


## [Langchain-serve](https://github.com/jina-ai/langchain-serve)
（Langchain-serve）


该存储库允许用户将本地链和代理作为 RESTful、gRPC 或 WebSocket API 提供，感谢 [Jina](https://docs.jina.ai/)。轻松部署您的链和代理，享受独立扩展、无服务器和自动扩展的 API，以及 Jina AI Cloud 上的 Streamlit 游乐场。


## [BentoML](https://github.com/ssheng/BentoChain)
（BentoML）


该存储库提供了使用 [BentoML](https://github.com/bentoml/BentoML) 部署 LangChain 应用程序的示例。BentoML 是一个框架，可以将机器学习应用程序容器化为标准 OCI 镜像。BentoML 还可以自动生成 OpenAPI 和 gRPC 端点。使用 BentoML，您可以集成来自所有流行 ML 框架的模型，并将它们作为运行在最优硬件上独立扩展的微服务部署。


## [Databutton](https://databutton.com/home?new-data-app=true)
（Databutton）


这些模板示例展示了使用 Databutton 构建、部署和共享 LangChain 应用程序的方法。您可以使用 Streamlit 创建用户界面，通过调度 Python 代码自动化任务，并在内置存储中存储文件和数据。示例包括具有对话记忆的聊天机器人界面、个人搜索引擎以及 LangChain 应用程序的入门模板。一键部署和共享。
