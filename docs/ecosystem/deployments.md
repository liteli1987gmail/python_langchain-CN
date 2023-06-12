## 部署（Deployments）

你已经创建了一条非常酷的链，现在该怎么办？如何部署它并轻松地与世界分享？（So you've created a really cool chain - now what? How do you deploy it and make it easily shareable with the world?）

本节涵盖了几个选项。请注意，这些选项是用于快速部署原型和演示的，而不是用于生产系统。如果您需要帮助部署生产系统，请直接联系我们。（This section covers several options for that. Note that these options are meant for quick deployment of prototypes and demos, not for production systems. If you need help with the deployment of a production system, please contact us directly.）

接下来是一组设计为容易fork并修改以使用您的链的模板GitHub存储库的列表。此列表远非详尽无遗，我们在这里非常欢迎您的贡献。#（What follows is a list of template GitHub repositories designed to be easily forked and modified to use your chain. This list is far from exhaustive, and we are EXTREMELY open to contributions here.）

## Anyscale（https://www.anyscale.com/model-serving）

Anyscale是一个统一的计算平台，可通过Ray轻松地开发、部署和管理可扩展的LLM应用程序，用于生产。（Anyscale is a unified compute platform that makes it easy to develop, deploy, and manage scalable LLM applications in production using Ray.）
使用Anyscale，您可以扩展最具挑战性的基于LLM的工作负载，并在单个计算平台上开发和部署基于LLM的应用程序。（With Anyscale you can scale the most challenging LLM-based workloads and both develop and deploy LLM-based apps on a single compute platform.）

## Streamlit（https://github.com/hwchase17/langchain-streamlit-template）

此存储库用作如何在Streamlit上部署LangChain的模板。（This repo serves as a template for how to deploy a LangChain with Streamlit.）
它实现了一个聊天机器人接口。（It implements a chatbot interface.）
它还包含了如何在Streamlit平台上部署此应用程序的说明。（It also contains instructions for how to deploy this app on the Streamlit platform.）

## Gradio（在Hugging Face上）（https://github.com/hwchase17/langchain-gradio-template）

此存储库用作如何使用Gradio部署LangChain的模板。（This repo serves as a template for how deploy a LangChain with Gradio.）
它实现了一种带有“Bring-Your-Own-Token”方法的聊天机器人接口（适用于不会产生大账单的情况）。（It implements a chatbot interface with a \"Bring-Your-Own-Token\" approach (nice for not wracking up big bills).）
它还包含如何在Hugging Face平台上部署此应用程序的说明。（It also contains instructions for how to deploy this app on the Hugging Face platform.）
这受到James Weaver的[精彩示例](https://huggingface.co/JavaFXpert)的强烈影响。（This is heavily influenced by James Weaver's excellent examples.）


## [Chainlit](https://github.com/Chainlit/cookbook) Chainlit是一个库，用来说明如何使用Chainlit可视化和部署LangChain代理。 

这个库是一个说明书，解释了如何使用Chainlit创建类似于ChatGPT的用户界面。一些关键功能包括中间步骤可视化，元素管理和显示（图像，文本，旋转木马等），以及云部署。
Chainlit [文档](https://docs.chainlit.io/langchain)中介绍了与LangChain的集成。



## [Beam](https://github.com/slai-labs/get-beam/tree/main/examples/langchain-question-answering)

这个库是一个模板，用于展示如何使用[Beam](https://beam.cloud)部署LangChain。 

它实现了一个问答应用程序，并包含部署该应用程序作为无服务器REST API的指令。 

## [Vercel](https://github.com/homanp/vercel-langchain)

一个最小的例子，展示了如何使用Flask在Vercel上运行LangChain。

## [FastAPI + Vercel](https://github.com/msoedov/langcorn)

一个最小的例子，展示了如何使用FastAPI和LangCorn / Uvicorn在Vercel上运行LangChain。 

## [Kinsta](https://github.com/kinsta/hello-world-langchain)

一个最小的例子，展示了如何使用Flask将LangChain部署到[Kinsta](https://kinsta.com)。

## [Fly.io](https://github.com/fly-apps/hello-fly-langchain)

一个最小的例子，展示了如何使用Flask将LangChain部署到[Fly.io](https://fly.io/)。

## [Digitalocean App Platform](https://github.com/homanp/digitalocean-langchain)

一个最小的例子，展示了如何将LangChain部署到DigitalOcean App Platform。

## [Google Cloud Run](https://github.com/homanp/gcp-langchain)


如何在Google Cloud Run上部署LangChain的最小示例。


## [SteamShip](https://github.com/steamship-core/steamship-langchain/)这个存储库包含了Steamship的LangChain适配器，使LangChain开发人员能够快速在Steamship上部署他们的应用程序。这包括生产就绪的端点，跨依赖的水平扩展，应用程序状态的持久性存储，多租户支持等等。


This repository contains LangChain adapters for Steamship, enabling LangChain developers to rapidly deploy their apps on Steamship. This includes: production-ready endpoints, horizontal scaling across dependencies, persistent storage of app state, multi-tenancy support, etc.



## [Langchain-serve](https://github.com/jina-ai/langchain-serve)这个存储库允许用户将本地约束和代理作为RESTful、gRPC或WebSocket API提供。感谢[Jina](https://docs.jina.ai/)，可以轻松部署你的约束和代理，享受独立扩展、无服务器和自动扩展API，以及在Jina AI Cloud上的Streamlit Playground。


This repository allows users to serve local chains and agents as RESTful, gRPC, or WebSocket APIs, thanks to [Jina](https://docs.jina.ai/). Deploy your chains & agents with ease and enjoy independent scaling, serverless and autoscaling APIs, as well as a Streamlit playground on Jina AI Cloud.



## [BentoML](https://github.com/ssheng/BentoChain)这个存储库提供了一个例子，展示如何使用[BentoML](https://github.com/bentoml/BentoML)部署LangChain应用程序。BentoML是一个使机器学习应用程序容器化为标准OCI镜像的框架。BentoML还允许自动生成OpenAPI和gRPC端点。使用BentoML，您可以集成来自所有流行机器学习框架的模型，并将它们作为运行在最优硬件上的微服务独立扩展部署。


This repository provides an example of how to deploy a LangChain application with [BentoML](https://github.com/bentoml/BentoML). BentoML is a framework that enables the containerization of machine learning applications as standard OCI images. BentoML also allows for the automatic generation of OpenAPI and gRPC endpoints. With BentoML, you can integrate models from all popular ML frameworks and deploy them as microservices running on the most optimal hardware and scaling independently.



## [Databutton](https://databutton.com/home?new-data-app=true)



These templates serve as examples of how to build, deploy, and share LangChain applications using Databutton. You can create user interfaces with Streamlit, automate tasks by scheduling Python code, and store files and data in the built-in store. Examples include a Chatbot interface with conversational memory, a Personal search engine, and a starter template for LangChain apps. Deploying and sharing is just one click away.

