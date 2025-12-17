
# Custom Query Parameter



Documentation for accessing and setting credentials for httpQuery.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| token | `str` | - | `token` |
| api-key | `str` | - | `api_key` |



**Note:** Auth credentials can be set using `HttpQueryCredentials` object, passed in as named parameter `http_query_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from multiplesimilarauthtypes.http.auth.http_query import HttpQueryCredentials
from multiplesimilarauthtypes.multiplesimilarauthtypes_client import MultiplesimilarauthtypesClient

client = MultiplesimilarauthtypesClient(
    http_query_credentials=HttpQueryCredentials(
        token='token',
        api_key='api-key'
    )
)
```


