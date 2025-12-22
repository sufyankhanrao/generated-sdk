
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
| custom_query_authentication_credentials | [`CustomQueryAuthenticationCredentials`](auth/custom-query-parameter.md) | The credential object for Custom Query Parameter |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
from customqueryparameter.configuration import Environment
from customqueryparameter.customqueryparameter_client import CustomqueryparameterClient
from customqueryparameter.http.auth.custom_query_authentication import CustomQueryAuthenticationCredentials
from customqueryparameter.models.suite_code_enum import SuiteCodeEnum

client = CustomqueryparameterClient(
    custom_query_authentication_credentials=CustomQueryAuthenticationCredentials(
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
from customqueryparameter.customqueryparameter_client import CustomqueryparameterClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = CustomqueryparameterClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## Custom Query Parameter Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| custom_query_param_test | Gets CustomQueryParamTestController |

