
# Custom Header Signature



Documentation for accessing and setting credentials for ApiKey.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| X-API-Key | `str` | API key for authentication | `x_api_key` |



**Note:** Auth credentials can be set using `ApiKeyCredentials` object, passed in as named parameter `api_key_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from webhooksandcallbacksapi.http.auth.api_key import ApiKeyCredentials
from webhooksandcallbacksapi.webhooksandcallbacksapi_client import WebhooksandcallbacksapiClient

client = WebhooksandcallbacksapiClient(
    api_key_credentials=ApiKeyCredentials(
        x_api_key='X-API-Key'
    )
)
```


