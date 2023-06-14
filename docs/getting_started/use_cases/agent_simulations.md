代理人模拟



代理人模拟涉及将一个或多个代理人彼此交互。

代理人模拟通常包含两个主要组成部分：



- 长期记忆

- 模拟环境



代理人模拟（或代理人模拟的一部分）的具体实现包括：



单代理人模拟

- 模拟环境：健身房](agent_simulations/gymnasium.ipynb)：使用Gymnasium](https://gymnasium.farama.org/)（前身为OpenAI Gym](https://github.com/openai/gym)）创建简单的代理人-环境交互循环的示例。



双代理人模拟

- CAMEL](agent_simulations/camel_role_playing.ipynb)：根据CAMEL（Communicative Agents for “Mind” Exploration of Large Scale Language Model Society）论文实现，其中两个代理人进行交流。

- Two Player D&D](agent_simulations/two_player_dnd.ipynb)：使用通用模拟器实现两个代理人的变体，模拟受欢迎的龙与地下城角色扮演游戏。

- 带工具的代理人辩论](agent_simulations/two_agent_debate_tools.ipynb)：示例演示如何使对话代理人使用工具来支持其回答。



多代理人模拟

- 多人龙与地下城](agent_simulations/multi_player_dnd.ipynb)：示例演示如何使用通用对话模拟器和自定义发言顺序来模拟多个对话代理人，以变体的方式展示流行的龙与地下城角色扮演游戏。

- 去中心化发言者选择](agent_simulations/multiagent_bidding.ipynb)：示例演示如何实现无固定发言时间表的多代理人对话。代理人通过出价进行发言选择。此示例演示了如何在虚构的总统辩论的情境中实现这一点。

- 集权发言者选择](agent_simulations/multiagent_authoritarian.ipynb)：示例演示如何实现多代理人对话，其中特权代理指示发言内容。此示例还展示了如何使特权代理确定对话何时结束。此示例演示了如何在虚构的新闻节目的情境中实现这一点。

- 模拟环境：PettingZoo](agent_simulations/petting_zoo.ipynb)：使用PettingZoo](https://pettingzoo.farama.org/)（Gymnasium](https://gymnasium.farama.org/)的多代理人版）为多个代理人创建代理人-环境交互循环的示例。

- 生成式代理人](agent_simulations/characters.ipynb)：此笔记本实现了一种基于Park等人的论文Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)的生成式代理人。

