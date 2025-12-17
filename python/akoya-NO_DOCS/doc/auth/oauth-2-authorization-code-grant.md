
# OAuth 2 Authorization Code Grant



Documentation for accessing and setting credentials for acgAuth.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| OAuthClientId | `str` | OAuth 2 Client ID | `oauth_client_id` |
| OAuthClientSecret | `str` | OAuth 2 Client Secret | `oauth_client_secret` |
| OAuthRedirectUri | `str` | OAuth 2 Redirection endpoint or Callback Uri | `oauth_redirect_uri` |
| OAuthToken | `OauthToken` | Object for storing information about the OAuth token | `oauth_token` |
| OAuthOnTokenUpdate | `Callable[[OAuthToken], None]` | Registers a callback for token update event. | `oauth_on_token_update` |
| OAuthClockSkew | `int` | Clock skew time in seconds applied while checking the OAuth Token expiry. | `oauth_clock_skew` |



**Note:** Auth credentials can be set using `AuthorizationCodeAuthCredentials` object, passed in as named parameter `authorization_code_auth_credentials` in the client initialization.

## Usage Example

### 1\. Client Initialization

You must initialize the client with *OAuth 2.0 Authorization Code Grant* credentials as shown in the following code snippet.

```python
from akoya.akoya_client import AkoyaClient
from akoya.http.auth.oauth_2 import AuthorizationCodeAuthCredentials

client = AkoyaClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_redirect_uri='OAuthRedirectUri',
        oauth_on_token_update=(lambda oauth_token:
                                # Add the callback handler to perform operations like save to DB or file etc.
                                # It will be triggered whenever the token gets updated
                                save_token_to_database(oauth_token))
    )
)
```



Your application must obtain user authorization before it can execute an endpoint call in case this SDK chooses to use *OAuth 2.0 Authorization Code Grant*. This authorization includes the following steps

### 2\. Obtain user consent

To obtain user's consent, you must redirect the user to the authorization page.The `get_authorization_url()` method creates the URL to the authorization page.

```python
auth_url = client.acg_auth.get_authorization_url("connector", "state")
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
    token = client.acg_auth.fetch_token('code')
    authorization_code_auth_credentials = client.config.authorization_code_auth_credentials.clone_with(oauth_token=token)
    config = client.config.clone_with(authorization_code_auth_credentials=authorization_code_auth_credentials)
    client = AkoyaClient(config=config)
except OauthProviderException as ex:
    # handle exception
    pass
except ApiException as ex:
    # handle exception
    pass
```

### Adding OAuth Token Update Callback

Whenever the OAuth Token gets updated, the provided callback implementation will be executed. For instance, you may use it to store your access token whenever it gets updated.

```python
from akoya.akoya_client import AkoyaClient
from akoya.http.auth.oauth_2 import AuthorizationCodeAuthCredentials

client = AkoyaClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_redirect_uri='OAuthRedirectUri',
        oauth_on_token_update=(lambda oauth_token:
                                # Add the callback handler to perform operations like save to DB or file etc.
                                # It will be triggered whenever the token gets updated
                                save_token_to_database(oauth_token))
    )
)
```

### Revoking the token

The access token can be revoked anytime using the following code.

```python
client.acg_auth.revokeToken()
```

### Complete example



```python
from akoya.akoya_client import AkoyaClient
from akoya.http.auth.oauth_2 import AuthorizationCodeAuthCredentials
from akoya.exceptions.oauth_provider_exception import OauthProviderException

client = AkoyaClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_redirect_uri='OAuthRedirectUri'
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
    authorization_code_auth_credentials = client.config.authorization_code_auth_credentials.clone_with(oauth_token=previous_token)
    config = client.config.clone_with(authorization_code_auth_credentials=authorization_code_auth_credentials)
    client = AkoyaClient(config=config)
else:
    # redirect user to a page that handles authorization
    pass

# the client is now authorized and you can use controllers to make endpoint calls
```


