
# OAuth 2 Authorization Code Grant



Documentation for accessing and setting credentials for httpACG.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| OAuthClientId | `str` | OAuth 2 Client ID | `o_auth_client_id` |
| OAuthClientSecret | `str` | OAuth 2 Client Secret | `o_auth_client_secret` |
| OAuthRedirectUri | `str` | OAuth 2 Redirection endpoint or Callback Uri | `o_auth_redirect_uri` |
| OAuthToken | `OAuthToken` | Object for storing information about the OAuth token | `o_auth_token` |



**Note:** Auth credentials can be set using `AuthorizationCodeAuthCredentials` object, passed in as named parameter `authorization_code_auth_credentials` in the client initialization.

## Usage Example

### 1\. Client Initialization

You must initialize the client with *OAuth 2.0 Authorization Code Grant* credentials as shown in the following code snippet.

```python
from mdnotesacgwithoutauthscopes.http.auth.o_auth_2 import AuthorizationCodeAuthCredentials
from mdnotesacgwithoutauthscopes.mdnotesacgwithoutauthscopes_client import MdnotesacgwithoutauthscopesClient

client = MdnotesacgwithoutauthscopesClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_redirect_uri='OAuthRedirectUri'
    )
)
```



Your application must obtain user authorization before it can execute an endpoint call in case this SDK chooses to use *OAuth 2.0 Authorization Code Grant*. This authorization includes the following steps

### 2\. Obtain user consent

To obtain user's consent, you must redirect the user to the authorization page.The `get_authorization_url()` method creates the URL to the authorization page.

```python
auth_url = client.http_acg.get_authorization_url()
```

### 3\. Handle the OAuth server response

Once the user responds to the consent request, the OAuth 2.0 server responds to your application's access request by redirecting the user to the redirect URI specified set in `Configuration`.

If the user approves the request, the authorization code will be sent as the `code` query string:

```
https://example.com/oauth/callback?code=XXXXXXXXXXXXXXXXXXXXXXXXX
```

If the user does not approve the request, the response contains an `error` query string:

```
https://example.com/oauth/callback?error=access_denied
```

### 4\. Authorize the client using the code

After the server receives the code, it can exchange this for an *access token*. The access token is an object containing information for authorizing client requests and refreshing the token itself.

```python
try:
    token = client.http_acg.fetch_token('code')
    authorization_code_auth_credentials = client.config.authorization_code_auth_credentials.clone_with(o_auth_token=token)
    config = client.config.clone_with(authorization_code_auth_credentials=authorization_code_auth_credentials)
    client = MdnotesacgwithoutauthscopesClient(config=config)
except OAuthProviderException as ex:
    # handle exception
    pass
except APIException as ex:
    # handle exception
    pass
```

### Refreshing the token

An access token may expire after sometime. To extend its lifetime, you must refresh the token.

```python
if client.http_acg.is_token_expired():
    try:
        token = client.http_acg.refresh_token()
        authorization_code_auth_credentials = client.config.authorization_code_auth_credentials.clone_with(o_auth_token=token)
        config = client.config.clone_with(authorization_code_auth_credentials=authorization_code_auth_credentials)
        client = MdnotesacgwithoutauthscopesClient(config=config)
    except OAuthProviderException as ex:
       # handle exception
       pass
```

If a token expires, an exception will be thrown before the next endpoint call requiring authentication.

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

```python
# store token
save_token_to_database(client.config.authorization_code_auth_credentials.o_auth_token)
```

### Creating a client from a stored token

To authorize a client using a stored access token, just set the access token in Configuration along with the other configuration parameters before creating the client:

```python
client = MdnotesacgwithoutauthscopesClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        o_auth_token=load_token_from_database()
    )
)
```

### Complete example



```python
from mdnotesacgwithoutauthscopes.mdnotesacgwithoutauthscopes_client import MdnotesacgwithoutauthscopesClient
from mdnotesacgwithoutauthscopes.http.auth.o_auth_2 import AuthorizationCodeAuthCredentials
from mdnotesacgwithoutauthscopes.exceptions.o_auth_provider_exception import OAuthProviderException

client = MdnotesacgwithoutauthscopesClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_redirect_uri='OAuthRedirectUri'
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
    authorization_code_auth_credentials = client.config.authorization_code_auth_credentials.clone_with(o_auth_token=previous_token)
    config = client.config.clone_with(authorization_code_auth_credentials=authorization_code_auth_credentials)
    client = MdnotesacgwithoutauthscopesClient(config=config)
else:
    # redirect user to a page that handles authorization
    pass

# the client is now authorized and you can use controllers to make endpoint calls
```


