
# OAuth 2 Bearer token



Documentation for accessing and setting credentials for httpBearer.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| AccessToken | `str` | The OAuth 2.0 Access Token to use for API requests. | `access_token` |



**Note:** Auth credentials can be set using `HttpBearerCredentials` object, passed in as named parameter `http_bearer_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from multiauthjwtandcustomheader.http.auth.http_bearer import HttpBearerCredentials
from multiauthjwtandcustomheader.multiauthjwtandcustomheader_client import MultiauthjwtandcustomheaderClient

client = MultiauthjwtandcustomheaderClient(
    http_bearer_credentials=HttpBearerCredentials(
        access_token='AccessToken'
    )
)
```


