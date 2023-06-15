# Discord 社交平台



>[Discord](https://discord.com/) 是一个语音通话和即时消息社交平台。用户可以通过语音通话、视频通话、文字消息、媒体和文件在私人聊天或作为被称为 "服务器" 的社区中进行通信。

> 服务器是持久聊天室和语音频道的集合，可以通过邀请链接访问。

>



## 安装和设置





```bash

pip install pandas

```



按照以下步骤下载您的 `Discord` 数据：



1. 转到 **用户设置**

2. 然后转到 **隐私与安全**

3. 前往 **请求所有数据** 并点击 **请求数据** 按钮



您可能需要等待30天才能收到您的数据。您将收到一封发送至您在 Discord 注册的地址的电子邮件。该邮件将包含一个下载按钮，您可以使用该按钮下载您的个人 Discord 数据。





## 文档加载器



查看[用法示例](../modules/indexes/document_loaders/examples/discord.ipynb)。





```python

from langchain.document_loaders import DiscordChatLoader

```

