安装



官方发布



LangChain可在PyPi上获得，因此可以轻松安装:



```

pip install langchain

```



这将安装LangChain的最低要求。

当与各种模型提供程序、数据存储等集成时，LangChain的价值很大。

默认情况下，不会安装执行此操作所需的依赖项。

然而，有两种其他方式可以安装LangChain来引入这些依赖项。



要安装常见LLM提供程序所需的模块，请运行:



```

pip install langchainllms]

```



要安装所有集成所需的模块，请运行:



```

pip install langchainall]

```



请注意，如果您使用的是`zsh`，在将方括号作为参数传递给命令时，您需要将它们引用起来，例如:



```

pip install 'langchainall]'

```



从源代码安装



如果您想从源代码安装，可以通过克隆存储库并运行以下命令来完成:



```

pip install -e .

```

