# SpreedlySpreedly（https://docs.spreedly.com/）是一个允许您安全存储信用卡并将其用于与任意数量的支付网关和第三方API进行交易的服务。它通过同时提供卡片令牌化/保险库服务和网关和接收器集成服务来实现这一点。由Spreedly令牌化的付款方式存储在`Spreedly`,中，允许您独立存储卡片，然后根据您的业务要求将该卡传递给不同的终端点。


>[Spreedly](https://docs.spreedly.com/) is a service that allows you to securely store credit cards and use them to transact against any number of payment gateways and third party APIs. It does this by simultaneously providing a card tokenization/vault service as well as a gateway and receiver integration service. Payment methods tokenized by Spreedly are stored at `Spreedly`, allowing you to independently store a card and then pass that card to different end points based on your business requirements.

 

## 安装和设置参见[设置说明](../modules/indexes/document_loaders/examples/spreedly.ipynb)。


See [setup instructions](../modules/indexes/document_loaders/examples/spreedly.ipynb).



## 文档装载器参见[使用示例](../modules/indexes/document_loaders/examples/spreedly.ipynb)。


See a [usage example](../modules/indexes/document_loaders/examples/spreedly.ipynb).



```python

from langchain.document_loaders import SpreedlyLoader

```

