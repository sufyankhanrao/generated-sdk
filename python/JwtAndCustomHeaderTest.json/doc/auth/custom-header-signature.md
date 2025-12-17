
# Custom Header Signature



Documentation for accessing and setting credentials for httpHeader.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| token | `str` | - | `token` |
| api-key | `str` | - | `api_key` |



**Note:** Auth credentials can be set using `HttpHeaderCredentials` object, passed in as named parameter `http_header_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from multiauthjwtandcustomheader.http.auth.http_header import HttpHeaderCredentials
from multiauthjwtandcustomheader.multiauthjwtandcustomheader_client import MultiauthjwtandcustomheaderClient

client = MultiauthjwtandcustomheaderClient(
    http_header_credentials=HttpHeaderCredentials(
        token='token',
        api_key='api-key'
    )
)
```


