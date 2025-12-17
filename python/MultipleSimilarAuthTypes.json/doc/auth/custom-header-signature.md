
# Custom Header Signature



Documentation for accessing and setting credentials for breezeHeader.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| token | `str` | - | `token` |
| Breeze-ApiToken | `str` | - | `breeze_api_token` |
| X-Api-Key | `str` | - | `x_api_key` |



**Note:** Auth credentials can be set using `BreezeHeaderCredentials` object, passed in as named parameter `breeze_header_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from multiplesimilarauthtypes.http.auth.breeze_header import BreezeHeaderCredentials
from multiplesimilarauthtypes.multiplesimilarauthtypes_client import MultiplesimilarauthtypesClient

client = MultiplesimilarauthtypesClient(
    breeze_header_credentials=BreezeHeaderCredentials(
        token='token',
        breeze_api_token='Breeze-ApiToken',
        x_api_key='X-Api-Key'
    )
)
```


