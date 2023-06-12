Discord（即戴斯科德）

> [Discord](https://discord.com/) 是一款语音通话和即时通讯社交平台。用户可以使用其语音通话、视频通话、文字聊天、媒体和文件等功能进行通信，可以私人聊天，也可以加入名为“服务器”的社区。
> 服务器是一个持久聊天室和语音频道的集合，可以通过邀请链接访问。


## 安装和设置


```bash
pip install pandas

```


按照以下步骤下载您的 `Discord` 数据：

1. 进入您的 **用户设置**
2. 然后进入 **隐私与安全**
3. 转到 **请求我的全部数据** 并单击 **请求数据** 按钮

您可能需要等待30天才能收到您的数据。您将收到一封发送至在Discord注册的电子邮件地址的电子邮件。该电子邮件将包含一个下载按钮，您可以使用该按钮下载您的个人Discord数据。



## 文档加载器

查看[使用示例](../modules/indexes/document_loaders/examples/discord.ipynb)。

```python

from langchain.document_loaders import DiscordChatLoader

```

