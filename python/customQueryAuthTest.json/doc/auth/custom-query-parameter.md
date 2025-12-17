
# Custom Query Parameter



Documentation for accessing and setting credentials for httpQuery.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| token | `str` | - | `token` |
| api-key | `str` | - | `api_key` |



**Note:** Auth credentials can be set using `CustomQueryAuthenticationCredentials` object, passed in as named parameter `custom_query_authentication_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from customqueryparameter.customqueryparameter_client import CustomqueryparameterClient
from customqueryparameter.http.auth.custom_query_authentication import CustomQueryAuthenticationCredentials

client = CustomqueryparameterClient(
    custom_query_authentication_credentials=CustomQueryAuthenticationCredentials(
        token='token',
        api_key='api-key'
    )
)
```


