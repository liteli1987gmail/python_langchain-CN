# Agent Simulations 代理人模拟



Agent simulations involve interacting one of more agents with each other. 代理人模拟涉及一个或多个代理人之间的相互作用。

Agent simulations generally involve two main components: 代理人模拟通常包括两个主要组成部分：



- Long Term Memory 长期记忆

- Simulation Environment 模拟环境



Specific implementations of agent simulations (or parts of agent simulations) include: 代理人模拟的具体实现（或代理人模拟的部分）包括：



## Simulations with One Agent 单代理人模拟

- [Simulated Environment: Gymnasium](agent_simulations/gymnasium.ipynb) 模拟环境：Gymnasium（健身房）：一个使用[Gymnasium](https://gymnasium.farama.org/)（前身为[OpenAI Gym](https://github.com/openai/gym)）创建简单的代理人-环境交互循环的示例。



## Simulations with Two Agents 双代理人模拟

- [CAMEL](agent_simulations/camel_role_playing.ipynb): 实现了《CAMEL（用于大规模语言模型社会的沟通代理人）》论文，其中两个代理人互相通信。

- [Two Player D&D](agent_simulations/two_player_dnd.ipynb): 一个示例，演示如何使用通用模拟器实现双代理人版本的流行角色扮演游戏 Dungeons & Dragons（龙与地下城）的变体。

- [Agent Debates with Tools](agent_simulations/two_agent_debate_tools.ipynb): 一个示例，演示如何使对话代理人使用工具来提供回答。



## Simulations with Multiple Agents 多代理人模拟

- [Multi-Player D&D](agent_simulations/multi_player_dnd.ipynb): 一个示例，演示如何使用通用对话模拟器来进行多个对话代理人的交互，包括自定义的发言顺序，以一个流行角色扮演游戏 Dungeons & Dragons（龙与地下城）的变体为例。

- [Decentralized Speaker Selection](agent_simulations/multiagent_bidding.ipynb): 一个示例，演示如何实现多代理人对话而无需固定的发言顺序。代理人通过投标来决定发言者。该示例以虚构的总统辩论为背景。

- [Authoritarian Speaker Selection](agent_simulations/multiagent_authoritarian.ipynb): 一个示例，演示如何实现多代理人对话，特权代理指示发言内容。此示例还展示了如何使特权代理确定对话何时终止。该示例以虚构的新闻节目为背景。

- [Simulated Environment: PettingZoo](agent_simulations/petting_zoo.ipynb): 一个示例，演示如何创建多个代理人与[PettingZoo](https://pettingzoo.farama.org/)（[Gymnasium](https://gymnasium.farama.org/)的多代理人版本）中的环境进行交互。

- [Generative Agents](agent_simulations/characters.ipynb): 该笔记本实现了基于文章[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)的生成式代理人（由Park等人撰写）。

