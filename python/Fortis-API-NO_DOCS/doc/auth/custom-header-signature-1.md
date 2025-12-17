
# Custom Header Signature



Documentation for accessing and setting credentials for user-api-key.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| user-api-key | `str` | User API Key | `user_api_key` |



**Note:** Auth credentials can be set using `UserApiKeyCredentials` object, passed in as named parameter `user_api_key_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials

client = FortisapiClient(
    user_api_key_credentials=UserApiKeyCredentials(
        user_api_key='user-api-key'
    )
)
```


