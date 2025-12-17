
# OAuth 2 Resource Owner Credentials Grant



Documentation for accessing and setting credentials for httpROPCG.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| OAuthClientId | `str` | OAuth 2 Client ID | `o_auth_client_id` |
| OAuthClientSecret | `str` | OAuth 2 Client Secret | `o_auth_client_secret` |
| OAuthUsername | `str` | OAuth 2 Resource Owner Username | `o_auth_username` |
| OAuthPassword | `str` | OAuth 2 Resource Owner Password | `o_auth_password` |
| OAuthToken | `OAuthToken` | Object for storing information about the OAuth token | `o_auth_token` |
| OAuthScopes | `List[OAuthScopeEnum]` | List of scopes that apply to the OAuth token | `o_auth_scopes` |



**Note:** Auth credentials can be set using `ResourceOwnerAuthCredentials` object, passed in as named parameter `resource_owner_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must initialize the client with *OAuth 2.0 Resource Owner Password Credentials Grant* credentials as shown in the following code snippet.

```python
from mdnotesropcg.http.auth.o_auth_2 import ResourceOwnerAuthCredentials
from mdnotesropcg.mdnotesropcg_client import MdnotesropcgClient
from mdnotesropcg.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesropcgClient(
    resource_owner_auth_credentials=ResourceOwnerAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_username='OAuthUsername',
        o_auth_password='OAuthPassword',
        o_auth_scopes=[
            OAuthScopeEnum.READ_SCOPE,
            OAuthScopeEnum.WRITE_SCOPE
        ]
    )
)
```



Your application must obtain user authorization before it can execute an endpoint call in case this SDK chooses to use *OAuth 2.0 Resource Owner Password Credentials Grant*. This authorization includes the following steps

The `fetch_token()` method will exchange the user's credentials for an *access token*. The access token is an object containing information for authorizing client requests and refreshing the token itself.

You must have initialized the client with scopes for which you need permission to access.

```python
try:
    token = client.http_ropcg.fetch_token()
    resource_owner_auth_credentials = client.config.resource_owner_auth_credentials.clone_with(o_auth_token=token)
    config = client.config.clone_with(resource_owner_auth_credentials=resource_owner_auth_credentials)
    client = MdnotesropcgClient(config=config)
except OAuthProviderException as ex:
    # handle exception
    pass
except APIException as ex:
    # handle exception
    pass
```

The client can now make authorized endpoint calls.

### Scopes

Scopes enable your application to only request access to the resources it needs while enabling users to control the amount of access they grant to your application. Available scopes are defined in the [`OAuthScopeEnum`](../../doc/models/o-auth-scope-enum.md) enumeration.

| Scope Name | Description |
|  --- | --- |
| `READ_SCOPE` | Read scope |
| `WRITE_SCOPE` | Write scope |

### Refreshing the token

An access token may expire after sometime. To extend its lifetime, you must refresh the token.

```python
if client.http_ropcg.is_token_expired():
    try:
        token = client.http_ropcg.refresh_token()
        resource_owner_auth_credentials = client.config.resource_owner_auth_credentials.clone_with(o_auth_token=token)
        config = client.config.clone_with(resource_owner_auth_credentials=resource_owner_auth_credentials)
        client = MdnotesropcgClient(config=config)
    except OAuthProviderException as ex:
       # handle exception
       pass
```

If a token expires, an exception will be thrown before the next endpoint call requiring authentication.

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

```python
# store token
save_token_to_database(client.config.resource_owner_auth_credentials.o_auth_token)
```

### Creating a client from a stored token

To authorize a client using a stored access token, just set the access token in Configuration along with the other configuration parameters before creating the client:

```python
client = MdnotesropcgClient(
    resource_owner_auth_credentials=ResourceOwnerAuthCredentials(
        o_auth_token=load_token_from_database()
    )
)
```

### Complete example



```python
from mdnotesropcg.mdnotesropcg_client import MdnotesropcgClient
from mdnotesropcg.http.auth.o_auth_2 import ResourceOwnerAuthCredentials
from mdnotesropcg.models.o_auth_scope_enum import OAuthScopeEnum
from mdnotesropcg.exceptions.o_auth_provider_exception import OAuthProviderException
from mdnotesropcg.exceptions.api_exception import APIException

from mdnotesropcg.http.auth.o_auth_2 import ResourceOwnerAuthCredentials
from mdnotesropcg.mdnotesropcg_client import MdnotesropcgClient
from mdnotesropcg.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesropcgClient(
    resource_owner_auth_credentials=ResourceOwnerAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_username='OAuthUsername',
        o_auth_password='OAuthPassword',
        o_auth_scopes=[
            OAuthScopeEnum.READ_SCOPE,
            OAuthScopeEnum.WRITE_SCOPE
        ]
    )
)
# function for storing token to database
def save_token_to_database(token):
    # code to save the token to database
    pass

# function for loading token from database
def load_token_from_database():
    # load token from database and return it (return None if no token exists)
    pass

# obtain access token, needed for client to be authorized
previous_token = load_token_from_database()
if previous_token:
    # restore previous access token
    resource_owner_auth_credentials = client.config.resource_owner_auth_credentials.clone_with(o_auth_token=previous_token)
    config = client.config.clone_with(resource_owner_auth_credentials=resource_owner_auth_credentials)
    client = MdnotesropcgClient(config=config)
else:
    # obtain new access token
    try:
        token = client.http_ropcg.fetch_token()
        save_token_to_database(token)
        resource_owner_auth_credentials = client.config.resource_owner_auth_credentials.clone_with(o_auth_token=token)
        config = client.config.clone_with(resource_owner_auth_credentials=resource_owner_auth_credentials)
        client = MdnotesropcgClient(config=config)
    except OAuthProviderException as ex:
        # handle exception
        pass
    except APIException as ex:
        # handle exception
        pass

# the client is now authorized and you can use controllers to make endpoint calls
# client will automatically refresh the token when it expires and call the token update callback
```


