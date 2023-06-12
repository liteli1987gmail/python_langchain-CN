自主智能体




自主智能体是设计成更长期运行的代理。
您为它们提供一个或多个长期目标，并独立地朝着这些目标执行。
这些应用程序结合了工具使用和长期记忆。


目前，自主智能体还比较实验性，基于其他开源项目。
通过在LangChain原语中实现这些开源项目，我们可以获得LangChain的好处-轻松切换和尝试多个LLM、使用不同的向量存储作为内存、使用LangChain的工具集。
easy switching and experimenting with multiple LLMs, usage of different vectorstores as memory, 

usage of LangChain's collection of tools.



婴儿AGI（[原始仓库](https://github.com/yoheinakajima/babyagi))


- [婴儿AGI](autonomous_agents/baby_agi.ipynb): 一个实现BabyAGI作为LLM Chains的笔记本
- [具有工具的婴儿AGI](autonomous_agents/baby_agi_with_agent.ipynb): 基于上面的笔记本，这个例子将代理作为执行工具替换掉了，允许它实际执行动作。




AutoGPT（[原始仓库](https://github.com/Significant-Gravitas/Auto-GPT))
- [AutoGPT](autonomous_agents/autogpt.ipynb): 一个实现AutoGPT在LangChain原语中的笔记本
- [WebSearch Research Assistant](autonomous_agents/marathon_times.ipynb): 一个演示如何使用AutoGPT加特定工具作为可以使用Web的研究助手的笔记本。


MetaPrompt（[原始仓库](https://github.com/ngoodman/metaprompt))
- [Meta-Prompt](autonomous_agents/meta_prompt.ipynb): a notebook implementing Meta-Prompt in LangChain primitives

