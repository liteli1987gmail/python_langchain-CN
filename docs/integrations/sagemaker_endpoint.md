## SageMaker Endpoint# SageMaker终端点


>[Amazon SageMaker](https://aws.amazon.com/sagemaker/) is a system that can build, train, and deploy machine learning (ML) models with fully managed infrastructure, tools, and workflows.>[Amazon SageMaker](https://aws.amazon.com/sagemaker/) 是一个可使用完全托管的基础架构、工具和工作流程来构建、训练和部署机器学习（ML）模型的系统。


We use `SageMaker` to host our model and expose it as the `SageMaker Endpoint`.我们使用`SageMaker`来托管我们的模型并将其公开为“SageMaker Endpoint”。




## Installation and Setup# 安装和设置


```bash
pip install boto3

```



For instructions on how to expose model as a `SageMaker Endpoint`, please see [here](https://www.philschmid.de/custom-inference-huggingface-sagemaker). 有关如何将模型公开为“SageMaker Endpoint”的说明，请参见[此处](https://www.philschmid.de/custom-inference-huggingface-sagemaker)。


**Note**: In order to handle batched requests, we need to adjust the return line in the `predict_fn()` function within the custom `inference.py` script:**注意** 为了处理批处理请求，我们需要调整自定义`inference.py`脚本中`predict_fn()`函数中的返回行。


Change from从


```
return {"vectors": sentence_embeddings[0].tolist()}

```



to:到


```
return {"vectors": sentence_embeddings.tolist()}

```







We have to set up following required parameters of the `SagemakerEndpoint` call:我们必须设置`SagemakerEndpoint`调用的以下必需参数：
- `endpoint_name`: The name of the endpoint from the deployed Sagemaker model.- `endpoint_name`:从部署的Sagemaker模型中的端点名称。
    Must be unique within an AWS Region.

- `credentials_profile_name`: The name of the profile in the ~/.aws/credentials or ~/.aws/config files, which- `credentials_profile_name`: `~ / .aws / credentials`或`~ / .aws / config`文件中的配置文件名称
    has either access keys or role information specified.

    If not specified, the default credential profile or, if on an EC2 instance,

    credentials from IMDS will be used.

    See [this guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).



## LLM# LLM


See a [usage example](../modules/models/llms/integrations/sagemaker.ipynb).请参见[用法示例](../modules/models/llms/integrations/sagemaker.ipynb)。


```python
from langchain import SagemakerEndpoint

from langchain.llms.sagemaker_endpoint import LLMContentHandler

```



## Text Embedding Models# 文本嵌入模型


See a [usage example](../modules/models/text_embedding/examples/sagemaker-endpoint.ipynb).请参见[用法示例](../modules/models/text_embedding/examples/sagemaker-endpoint.ipynb)。
```python

from langchain.embeddings import SagemakerEndpointEmbeddings

from langchain.llms.sagemaker_endpoint import ContentHandlerBase

```

