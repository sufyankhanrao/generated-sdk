
# Custom Header Signature



Documentation for accessing and setting credentials for customHeader.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| token | `str` | - | `token` |
| api-key | `str` | - | `api_key` |



**Note:** Auth credentials can be set using `CustomHeaderCredentials` object, passed in as named parameter `custom_header_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from multiplesimilarauthtypes.http.auth.custom_header import CustomHeaderCredentials
from multiplesimilarauthtypes.multiplesimilarauthtypes_client import MultiplesimilarauthtypesClient

client = MultiplesimilarauthtypesClient(
    custom_header_credentials=CustomHeaderCredentials(
        token='token',
        api_key='api-key'
    )
)
```


