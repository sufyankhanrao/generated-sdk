
# Custom Header Signature



Documentation for accessing and setting credentials for apiKey.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| APIKEY | `str` | - | `apikey` |



**Note:** Auth credentials can be set using `ApiKeyCredentials` object, passed in as named parameter `api_key_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.payrix_client import PayrixClient

client = PayrixClient(
    api_key_credentials=ApiKeyCredentials(
        apikey='APIKEY'
    )
)
```


