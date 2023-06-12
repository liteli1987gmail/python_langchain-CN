## 安装（Installation）


## 官方发布（Official Releases）


LangChain可在PyPi中获得，因此很容易安装（so to it is easily installable with:）


```
pip install langchain

```



这将安装LangChain的最小要求。（That will install the bare minimum requirements of LangChain.）
当与各种模型提供商、数据库等集成时，LangChain的很多价值就会显现出来。（A lot of the value of LangChain comes when integrating it with various model providers, datastores, etc.）
默认情况下，不会安装执行这些操作所需的依赖项。（By default, the dependencies needed to do that are NOT installed.）
但是，还有两种其他方式可以安装LangChain，这样可以引入这些依赖项。（However, there are two other ways to install LangChain that do bring in those dependencies.）


要安装所需的常见LLM提供商模块，请运行:（To install modules needed for the common LLM providers, run:）


```
pip install langchain[llms]

```



要安装所有集成所需的模块，请运行:（To install all modules needed for all integrations, run:）


```
pip install langchain[all]

```



请注意，如果您使用`zsh`，则需要引用方括号，将它们作为命令的参数传递。例如:（Note that if you are using `zsh`, you'll need to quote square brackets when passing them as an argument to a command. For example:）


```
pip install 'langchain[all]'

```



## 从源代码安装（Installing from source）


如果您想从源代码安装，您可以克隆该存储库并运行:（If you want to install from source, you can do so by cloning the repo and running:）


```

pip install -e .

```

