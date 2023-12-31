


在生产环境中部署LLM
===========================



在当今快节奏的技术环境中，大型语言模型（LLM）的使用正在迅速扩展。因此，开发人员必须了解如何有效地在生产环境中部署这些模型。LLM界面通常分为两类：


- **案例1：利用外部LLM提供商（OpenAI、Anthropic等）**
在这种情况下，大部分的计算负载由LLM提供商处理，而LangChain简化了围绕这些服务实现业务逻辑的过程。这种方法包括提示模板化、聊天消息生成、缓存、向量嵌入式数据库创建、预处理等功能。


- **案例2：自行托管的开源模型**
另外，开发人员可以选择使用更小但功能相当的自行托管的开源LLM模型。这种方法可以大大降低将数据传输到外部LLM提供商所带来的成本、延迟和隐私问题。


无论构成产品骨干的是哪个框架，部署LLM应用程序都面临着一系列挑战。在评估服务框架时，了解权衡和关键考虑因素至关重要。


概述
=======



本指南旨在全面介绍在生产环境中部署LLM的要求，重点关注：


- `设计稳健的LLM应用程序服务 <#robust>`_

- `保持成本效益 <#cost>`_

- `确保迭代快速 <#iteration>`_



在评估服务系统时，理解这些组件至关重要。LangChain与几个旨在解决这些问题的开源项目集成在一起，为生产化LLM应用程序提供了一个稳健的框架。一些值得注意的框架包括：


- `Ray Serve <../integrations/ray_serve.html>`_

- `BentoML <https://github.com/ssheng/BentoChain>`_

- `Modal <../integrations/modal.html>`_



这些链接将提供有关每个生态系统的进一步信息，帮助您找到最适合您的LLM部署需求的解决方案。


设计稳健的LLM应用程序服务
===========================================

.. _robust:



在生产环境中部署LLM服务时，提供一个无间断的用户体验非常重要。实现全天候的服务可用性涉及创建和维护应用程序周围的多个子系统。


监控
----------



监控是在生产环境中运行的任何系统的一个重要组成部分。在LLM的上下文中，监控性能和质量指标都至关重要。


**性能指标：**这些指标提供有关模型效率和容量的见解。以下是一些关键示例：


- 每秒查询数（QPS）：衡量模型每秒处理的查询数，提供有关其利用率的见解。
- 延迟：量化从客户端发送请求到接收到响应的延迟。
- 每秒生成的标记数（TPS）：表示模型每秒可以生成的标记数。


**质量指标：**这些指标通常根据业务用例进行定制。例如，您的系统输出与基线（如先前版本）相比如何？尽管可以离线计算这些指标，但您需要记录必要的数据以便稍后使用。


容错性
---------------



您的应用程序可能会遇到错误，例如模型推断或业务逻辑代码中的异常，导致故障并中断流量。其他潜在问题可能来自运行应用程序的计算机，例如意外的硬件故障或在高需求期间丢失的Spot实例。通过增加冗余并实施针对失败副本的恢复机制，可以减轻这些风险。然而，模型副本并不是唯一可能出现故障的地方。在整个系统中的任何位置，建立对各种可能故障的弹性都是至关重要的。




零停机升级
----------------------



通常需要进行系统升级，但如果处理不当可能导致服务中断。防止升级期间的停机的一种方法是实施从旧版本到新版本的平滑过渡过程。理想情况下，将部署LLM服务的新版本，并且流量逐渐从旧版本转移到新版本，在整个过程中保持恒定的QPS。




负载均衡
--------------



负载均衡简单来说是一种技术，用于在多台计算机、服务器或其他资源之间均匀分配工作，以优化系统的利用率，最大化吞吐量，最小化响应时间，并避免任何单个资源的过载。可以把它想象成交通警察将车辆（请求）引导到不同的道路（服务器），以避免任何单个道路过于拥挤。


有几种负载均衡策略。例如，一种常见的方法是“轮询”策略，即将每个请求发送到下一个服务器，当所有服务器都收到请求后，再循环回第一个服务器。这种方法在所有服务器都具有相同能力的情况下效果很好。然而，如果某些服务器比其他服务器更强大，您可以使用“加权轮询”或“最少连接”策略，将更多请求发送到更强大的服务器，或者发送到当前处理的最少活动请求的服务器。让我们假设您运行一个LLM链。如果您的应用程序变得受欢迎，可能会有成百上千的用户同时提问。如果一个服务器忙不过来（负载高），负载均衡器会将新的请求引导到另一个负载较轻的服务器。这样，所有用户都能及时得到响应，系统保持稳定。






保持成本效益和可扩展性
============================================

.. _cost:



部署LLM服务可能是昂贵的，特别是当处理大量用户互动时。LLM提供商通常按照使用的令牌计费，因此在这些模型上进行聊天系统推理可能是昂贵的。然而，有几种策略可以帮助降低这些成本而不影响服务的质量。




自托管模型
-------------------



出现了几个较小的开源LLM模型，用于解决对LLM提供商的依赖问题。自行托管允许您在自己的机器上维护与LLM提供商模型相似的质量，同时管理成本。挑战在于在自己的机器上构建一个可靠高效的LLM服务系统。


资源管理和自动扩展
------------------------------------



应用程序中的计算逻辑需要精确的资源分配。例如，如果部分流量由OpenAI端点提供服务，另一部分流量由自托管模型提供服务，为每个部分分配适当的资源至关重要。自动扩展——根据流量调整资源分配——会极大地影响运行应用程序的成本。这种策略要在成本和响应能力之间保持平衡，确保既不会过度提供资源，也不会降低应用程序的响应能力。


利用Spot实例
------------------------



在AWS等平台上，Spot实例提供了可观的成本节约，通常价格约为按需实例的三分之一。这种折中是更高的崩溃率，因此需要一个强大的容错机制以实现有效的使用。


独立缩放
-------------------



自行托管模型时，应考虑独立缩放。例如，如果您有两个翻译模型，一个是针对法语的，另一个是针对西班牙语的，传入的请求可能需要对每个模型进行不同的缩放要求。


批处理请求
-----------------



在大型语言模型的上下文中，批处理请求可以通过更好地利用GPU资源来提高效率。GPU是并行处理器，设计用于同时处理多个任务。如果您单独发送请求给模型，GPU可能无法充分利用，因为它只在处理一个任务时工作。另一方面，通过将请求批量处理，您允许GPU同时处理多个任务，最大限度地利用其性能并提高推理速度。这不仅可以节省成本，还可以改善LLM服务的整体延迟。




总之，在扩展LLM服务时管理成本需要采用战略性的方法。利用自行托管模型、有效管理资源、使用自动扩展、使用Spot实例、独立缩放模型和批处理请求是需要考虑的关键策略。Ray Serve和BentoML等开源库专为应对这些复杂性而设计。






确保快速迭代
========================



.. _iteration:



LLM领域正在以前所未有的速度发展，不断引入新的库和模型架构。因此，避免将自己限制在针对特定框架的解决方案中非常重要。这在服务领域尤为重要，因为对基础设施的更改可能耗时、昂贵且有风险。致力于构建并不依赖于任何特定的机器学习库或框架的基础设施，而是提供一个通用、可扩展的服务层。以下是灵活性起到关键作用的一些方面：


模型组合
-----------------



部署类似LangChain的系统要求能够将不同的模型组合在一起，并通过逻辑将它们连接起来。以构建自然语言输入SQL查询引擎为例。查询LLM并获取SQL命令只是系统的一部分。您需要从连接的数据库中提取元数据，构造LLM的提示，运行引擎上的SQL查询，同时收集并将响应作为查询运行进行反馈，并向用户呈现结果。这显示了将Python中构建的各种复杂组件无缝集成到动态逻辑块链中的需求，这些组件可以一起提供服务。


云提供商
---------------



许多托管解决方案仅限于单个云提供商，这可能会限制您在当今多云世界中的选择。根据您其他基础设施组件的位置，您可能更愿意坚持您选择的云提供商。




基础设施即代码（IaC）
---------------------------



快速迭代还涉及快速可靠地重建基础设施的能力。这就是基础设施即代码（IaC）工具（如Terraform、CloudFormation或Kubernetes YAML文件）发挥作用的地方。它们使您可以使用代码文件定义基础设施，这些文件可以进行版本控制并快速部署，从而实现更快、更可靠的迭代。




持续集成/持续部署（CI/CD)
---------------------------



在快节奏的环境中，实施CI/CD流水线可以显著加快迭代过程。它们帮助自动化LLM应用程序的测试和部署，减少错误风险，并实现更快的反馈和迭代。
