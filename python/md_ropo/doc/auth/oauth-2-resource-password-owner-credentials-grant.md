
# OAuth 2 Resource Password Owner Credentials Grant



Documentation for accessing and setting credentials for httpROPO.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| OAuthUsername | `str` | OAuth 2 Resource Owner Username | `o_auth_username` |
| OAuthPassword | `str` | OAuth 2 Resource Owner Password | `o_auth_password` |
| OAuthToken | `OAuthToken` | Object for storing information about the OAuth token | `o_auth_token` |
| OAuthScopes | `List[OAuthScopeEnum]` | List of scopes that apply to the OAuth token | `o_auth_scopes` |



**Note:** Auth credentials can be set using `ResourcePasswordAuthCredentials` object, passed in as named parameter `resource_password_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must initialize the client with *OAuth 2.0 Resource Owner Password Credentials Grant* credentials as shown in the following code snippet.

```python
from mdnotesropo.http.auth.o_auth_2 import ResourcePasswordAuthCredentials
from mdnotesropo.mdnotesropo_client import MdnotesropoClient
from mdnotesropo.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesropoClient(
    resource_password_auth_credentials=ResourcePasswordAuthCredentials(
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
    token = client.http_ropo.fetch_token()
    resource_password_auth_credentials = client.config.resource_password_auth_credentials.clone_with(o_auth_token=token)
    config = client.config.clone_with(resource_password_auth_credentials=resource_password_auth_credentials)
    client = MdnotesropoClient(config=config)
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
if client.http_ropo.is_token_expired():
    try:
        token = client.http_ropo.refresh_token()
        resource_password_auth_credentials = client.config.resource_password_auth_credentials.clone_with(o_auth_token=token)
        config = client.config.clone_with(resource_password_auth_credentials=resource_password_auth_credentials)
        client = MdnotesropoClient(config=config)
    except OAuthProviderException as ex:
       # handle exception
       pass
```

If a token expires, an exception will be thrown before the next endpoint call requiring authentication.

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

```python
# store token
save_token_to_database(client.config.resource_password_auth_credentials.o_auth_token)
```

### Creating a client from a stored token

To authorize a client using a stored access token, just set the access token in Configuration along with the other configuration parameters before creating the client:

```python
client = MdnotesropoClient(
    resource_password_auth_credentials=ResourcePasswordAuthCredentials(
        o_auth_token=load_token_from_database()
    )
)
```

### Complete example



```python
from mdnotesropo.mdnotesropo_client import MdnotesropoClient
from mdnotesropo.http.auth.o_auth_2 import ResourcePasswordAuthCredentials
from mdnotesropo.models.o_auth_scope_enum import OAuthScopeEnum
from mdnotesropo.exceptions.o_auth_provider_exception import OAuthProviderException
from mdnotesropo.exceptions.api_exception import APIException

from mdnotesropo.http.auth.o_auth_2 import ResourcePasswordAuthCredentials
from mdnotesropo.mdnotesropo_client import MdnotesropoClient
from mdnotesropo.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesropoClient(
    resource_password_auth_credentials=ResourcePasswordAuthCredentials(
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
    resource_password_auth_credentials = client.config.resource_password_auth_credentials.clone_with(o_auth_token=previous_token)
    config = client.config.clone_with(resource_password_auth_credentials=resource_password_auth_credentials)
    client = MdnotesropoClient(config=config)
else:
    # obtain new access token
    try:
        token = client.http_ropo.fetch_token()
        save_token_to_database(token)
        resource_password_auth_credentials = client.config.resource_password_auth_credentials.clone_with(o_auth_token=token)
        config = client.config.clone_with(resource_password_auth_credentials=resource_password_auth_credentials)
        client = MdnotesropoClient(config=config)
    except OAuthProviderException as ex:
        # handle exception
        pass
    except APIException as ex:
        # handle exception
        pass

# the client is now authorized and you can use controllers to make endpoint calls
# client will automatically refresh the token when it expires and call the token update callback
```


