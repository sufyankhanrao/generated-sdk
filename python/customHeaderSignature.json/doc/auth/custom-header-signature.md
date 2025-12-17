
# Custom Header Signature



Documentation for accessing and setting credentials for httpHeader.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| token | `str` | api-token for custom header auth | `token` |
| api-key | `str` | api-key for custom header auth | `api_key` |



**Note:** Auth credentials can be set using `CustomHeaderAuthenticationCredentials` object, passed in as named parameter `custom_header_authentication_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from customheadersignature.customheadersignature_client import CustomheadersignatureClient
from customheadersignature.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials

client = CustomheadersignatureClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        token='token',
        api_key='api-key'
    )
)
```


