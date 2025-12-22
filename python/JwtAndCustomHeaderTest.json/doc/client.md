
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| port | `str` | *Default*: `"80"` |
| suites | `SuiteCodeEnum` | *Default*: `1` |
| environment | `Environment` | The API environment. <br> **Default: `Environment.TESTING`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| http_bearer_credentials | [`HttpBearerCredentials`](auth/oauth-2-bearer-token.md) | The credential object for OAuth 2 Bearer token |
| http_header_credentials | [`HttpHeaderCredentials`](auth/custom-header-signature.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
from multiauthjwtandcustomheader.configuration import Environment
from multiauthjwtandcustomheader.http.auth.http_bearer import HttpBearerCredentials
from multiauthjwtandcustomheader.http.auth.http_header import HttpHeaderCredentials
from multiauthjwtandcustomheader.models.suite_code_enum import SuiteCodeEnum
from multiauthjwtandcustomheader.multiauthjwtandcustomheader_client import MultiauthjwtandcustomheaderClient

client = MultiauthjwtandcustomheaderClient(
    http_bearer_credentials=HttpBearerCredentials(
        access_token='AccessToken'
    ),
    http_header_credentials=HttpHeaderCredentials(
        token='token',
        api_key='api-key'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)
```

## Environment-Based Client Initialization

```python
from multiauthjwtandcustomheader.multiauthjwtandcustomheader_client import MultiauthjwtandcustomheaderClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = MultiauthjwtandcustomheaderClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## MultiAuthJWTandCustomHeader Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| api | Gets APIController |

