
# OAuth 2 Bearer token



Documentation for accessing and setting credentials for httpBearer.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| AccessToken | `str` | The OAuth 2.0 Access Token to use for API requests. | `access_token` |



**Note:** Auth credentials can be set using `BearerAuthCredentials` object, passed in as named parameter `bearer_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from oa2tester.http.auth.o_auth_2 import BearerAuthCredentials
from oa2tester.oa_2_tester_client import Oa2testerClient

client = Oa2testerClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    )
)
```


