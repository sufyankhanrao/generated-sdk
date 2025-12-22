from mdnotesccgwithoutauthscopes.configuration import Environment
from mdnotesccgwithoutauthscopes.exceptions.api_exception import APIException
from mdnotesccgwithoutauthscopes.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from mdnotesccgwithoutauthscopes.mdnotesccgwithoutauthscopes_client import MdnotesccgwithoutauthscopesClient
from mdnotesccgwithoutauthscopes.models.o_auth_token import OAuthToken

client = MdnotesccgwithoutauthscopesClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_token=OAuthToken(
            access_token='AccessToken',
            token_type='SandboxToken',
            expires_in=3600,
            refresh_token='RefreshToken'
        )
    ),
    environment=Environment.PRODUCTION
)

user_controller = client.user
try:
    result = user_controller.get_user()
    print(result)
except APIException as e: 
    print(e)

