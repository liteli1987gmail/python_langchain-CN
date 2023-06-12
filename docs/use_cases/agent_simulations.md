代理模拟


代理模拟涉及与其他代理相互作用。
代理模拟通常涉及两个主要组件。


- 长期记忆
- 模拟环境


代理模拟（或代理模拟的部分）的具体实现包括。


单代理模拟
- [模拟环境:体育馆](agent_simulations/gymnasium.ipynb):是使用[Gymnasium](https//gymnasium.farama.org/)（以前的[OpenAI Gym](https//github.com/openai/gym)）创建简单的代理-环境交互循环的示例。


双代理模拟
- [CAMEL](agent_simulations/camel_role_playing.ipynb):是CAMEL（用于“Mind”探索大规模语言模型社区的交际代理）论文的实现，在其中两个代理相互沟通。
- [两人D&D](agent_simulations/two_player_dnd.ipynb):是如何使用通用模拟器进行两个代理实现流行的Dungeons & Dragons角色扮演游戏的变体的示例。
- [代理辩论工具](agent_simulations/two_agent_debate_tools.ipynb):是一种示例，可以使对话代理使用工具来通知他们的回答。


多代理模拟
- [Multi-Player D&D](agent_simulations/multi_player_dnd.ipynb): an example of how to use a generic dialogue simulator for multiple dialogue agents with a custom speaker-ordering, illustrated with a variant of the popular Dungeons & Dragons role playing game.

- {去中心化演讲者选择}（agent_simulations / multiagent_bidding.ipynb）:一个示例，展示了如何在没有固定发言时间表的多代理对话中实现多代理对话。相反，代理商通过输出发言要求来决定谁发言。此示例演示了如何在虚构的总统辩论的背景下执行此操作。
- {专制演讲者选择}（agent_simulations / multiagent_authoritarian.ipynb）:一个示例，展示了如何实现多代理对话，其中特权代理指示谁说什么。这个例子还展示了如何使特权代理确定谈话何时终止。此示例演示了如何在虚构的新闻节目的背景下执行此操作。
- [模拟环境:PettingZoo]（agent_simulations / petting_zoo.ipynb）:一个示例，展示如何使用[PettingZoo]（https://pettingzoo.farama.org/）（[Gymnasium]的多代理版本 的多个代理与环境交互循环。（https://gymnasium.farama.org/）。
- [Generative Agents](agent_simulations/characters.ipynb): This notebook implements a generative agent based on the paper [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) by Park, et. al.

