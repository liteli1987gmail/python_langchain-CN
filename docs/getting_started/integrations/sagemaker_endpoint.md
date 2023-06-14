SageMaker终端点

>Amazon SageMaker](https://aws.amazon.com/sagemaker/)是一个可以使用完全托管的基础设施、工具和工作流构建、训练和部署机器学习（ML）模型的系统。

我们使用`SageMaker`来托管我们的模型，并将其作为`SageMaker终端点`暴露出来。


安装和设置

```bash

pip install boto3
```


有关如何将模型暴露为`SageMaker终端点`的说明，请参见此处](https://www.philschmid.de/custom-inference-huggingface-sagemaker)。

**注意**：为了处理批量请求，我们需要调整自定义`inference.py`脚本中的`predict_fn()`函数中的返回行：

从

```

return {"vectors": sentence_embeddings0].tolist()}
```


到：

```

return {"vectors": sentence_embeddings.tolist()}
```




我们必须设置`SagemakerEndpoint`调用的以下必需参数：
- `endpoint_name`：部署的Sagemaker模型的端点名称。
在AWS区域内必须唯一。
- `credentials_profile_name`：~/.aws/credentials或~/.aws/config文件中的配置文件名称，其中
指定了访问密钥或角色信息。
如果未指定，则将使用默认凭据配置文件，如果在EC2实例上，则使用IMDS中的凭据。
请参阅此指南](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)。


LLM

请参阅使用示例](../modules/models/llms/integrations/sagemaker.ipynb)。

```python

from langchain import SagemakerEndpoint

from langchain.llms.sagemaker_endpoint import LLMContentHandler

```


文本嵌入模型

请参阅使用示例](../modules/models/text_embedding/examples/sagemaker-endpoint.ipynb)。
```python

from langchain.embeddings import SagemakerEndpointEmbeddings

from langchain.llms.sagemaker_endpoint import ContentHandlerBase

```

