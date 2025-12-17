
# OAuth 2 Client Credentials Grant



Documentation for accessing and setting credentials for httpCCG.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| OAuthClientId | `str` | OAuth 2 Client ID | `o_auth_client_id` |
| OAuthClientSecret | `str` | OAuth 2 Client Secret | `o_auth_client_secret` |
| OAuthToken | `OAuthTokenModel` | Object for storing information about the OAuth token | `o_auth_token` |
| OAuthScopes | `List[OAuthScopeEnum]` | List of scopes that apply to the OAuth token | `o_auth_scopes` |
| OAuthTokenProvider | `Callable[[OAuthToken, OAuth2], OAuthToken]` | Registers a callback for oAuth Token Provider used for automatic token fetching/refreshing. | `o_auth_token_provider` |
| OAuthOnTokenUpdate | `Callable[[OAuthToken], None]` | Registers a callback for token update event. | `o_auth_on_token_update` |
| OAuthClockSkew | `int` | Clock skew time in seconds applied while checking the OAuth Token expiry. | `o_auth_clock_skew` |



**Note:** Auth credentials can be set using `ClientCredentialsAuthCredentials` object, passed in as named parameter `client_credentials_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must initialize the client with *OAuth 2.0 Client Credentials Grant* credentials as shown in the following code snippet. This will fetch the OAuth token automatically when any of the endpoints, requiring *OAuth 2.0 Client Credentials Grant* authentication, are called.

```python
from mdnotesccgmodelpostfix.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from mdnotesccgmodelpostfix.mdnotesccgmodelpostfix_client import MdnotesccgmodelpostfixClient
from mdnotesccgmodelpostfix.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesccgmodelpostfixClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_scopes=[
            OAuthScopeEnum.READ_SCOPE,
            OAuthScopeEnum.WRITE_SCOPE
        ]
    )
)
```



Your application can also manually provide an OAuthToken using the setter `o_auth_token` in `ClientCredentialsAuthCredentials` object. This function takes in an instance of OAuthToken containing information for authorizing client requests and refreshing the token itself.

You must have initialized the client with scopes for which you need permission to access.

### Scopes

Scopes enable your application to only request access to the resources it needs while enabling users to control the amount of access they grant to your application. Available scopes are defined in the [`OAuthScopeEnum`](../../doc/models/o-auth-scope-enum.md) enumeration.

| Scope Name | Description |
|  --- | --- |
| `READ_SCOPE` | Read scope |
| `WRITE_SCOPE` | Write scope |

### Adding OAuth Token Update Callback

Whenever the OAuth Token gets updated, the provided callback implementation will be executed. For instance, you may use it to store your access token whenever it gets updated.

```python
from mdnotesccgmodelpostfix.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from mdnotesccgmodelpostfix.mdnotesccgmodelpostfix_client import MdnotesccgmodelpostfixClient
from mdnotesccgmodelpostfix.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesccgmodelpostfixClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_scopes=[
            OAuthScopeEnum.READ_SCOPE,
            OAuthScopeEnum.WRITE_SCOPE
        ],
        o_auth_on_token_update=(lambda o_auth_token:
                                # Add the callback handler to perform operations like save to DB or file etc.
                                # It will be triggered whenever the token gets updated
                                save_token_to_database(o_auth_token))
    )
)
```

### Adding Custom OAuth Token Provider

To authorize a client using a stored access token, set up the `o_auth_token_provider` in `ClientCredentialsAuthCredentials` along with the other auth parameters before creating the client:

```python
from mdnotesccgmodelpostfix.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from mdnotesccgmodelpostfix.mdnotesccgmodelpostfix_client import MdnotesccgmodelpostfixClient
from mdnotesccgmodelpostfix.models.o_auth_scope_enum import OAuthScopeEnum

def _o_auth_token_provider(last_oauth_token, auth_manager):
    # Add the callback handler to provide a new OAuth token
    # It will be triggered whenever the last provided o_auth_token is null or expired
    o_auth_token = load_token_from_database()
    if o_auth_token is None:
        o_auth_token = auth_manager.fetch_token()
    return o_auth_token


client = MdnotesccgmodelpostfixClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_scopes=[
            OAuthScopeEnum.READ_SCOPE,
            OAuthScopeEnum.WRITE_SCOPE
        ],
        o_auth_token_provider=_o_auth_token_provider
    )
)
```


