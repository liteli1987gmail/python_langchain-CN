# 安装



## 官方发布



LangChain 可在 PyPi 上获取，因此可以使用以下命令轻松安装:



```

pip install langchain

```



这将安装 LangChain 的最低要求。

当与各种模型提供者、数据存储等集成时，LangChain 的价值很大。

默认情况下，不会安装执行此操作所需的依赖项。

但是，有两种其他安装 LangChain 的方法可以带来这些依赖项。



要安装常见 LLM 提供者所需的模块，请运行:



```

pip install langchain[llms]

```



要安装所有集成所需的模块，请运行:



```

pip install langchain[all]

```



请注意，如果你使用的是 `zsh`，在将方括号作为命令参数传递时，需要用引号括起来，例如:



```

pip install 'langchain[all]'

```



## 从源代码安装



如果你想从源代码安装，可以通过克隆存储库并运行以下命令来实现:



```

pip install -e .

```

