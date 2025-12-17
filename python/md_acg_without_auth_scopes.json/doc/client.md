
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| authorization_code_auth_credentials | [`AuthorizationCodeAuthCredentials`](auth/oauth-2-authorization-code-grant.md) | The credential object for OAuth 2 Authorization Code Grant |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
from mdnotesacgwithoutauthscopes.configuration import Environment
from mdnotesacgwithoutauthscopes.http.auth.o_auth_2 import AuthorizationCodeAuthCredentials
from mdnotesacgwithoutauthscopes.mdnotesacgwithoutauthscopes_client import MdnotesacgwithoutauthscopesClient

client = MdnotesacgwithoutauthscopesClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_redirect_uri='OAuthRedirectUri'
    ),
    environment=Environment.PRODUCTION
)
```

## Environment-Based Client Initialization

```python
from mdnotesacgwithoutauthscopes.mdnotesacgwithoutauthscopes_client import MdnotesacgwithoutauthscopesClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = MdnotesacgwithoutauthscopesClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## MdNotes-ACG-Without-Auth-Scopes Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| service | Gets ServiceController |
| user | Gets UserController |
| o_auth_authorization | Gets OAuthAuthorizationController |

