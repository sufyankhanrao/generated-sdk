
# Custom Header Signature



Documentation for accessing and setting credentials for API-Key.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| API-Key | `str` | API Key Authentication | `api_key` |



**Note:** Auth credentials can be set using `CustomHeaderAuthenticationCredentials` object, passed in as named parameter `custom_header_authentication_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from mindbodypublicapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        api_key='API-Key'
    )
)
```


