from mdnotesccg.configuration import Environment
from mdnotesccg.exceptions.api_exception import APIException
from mdnotesccg.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from mdnotesccg.mdnotesccg_client import MdnotesccgClient
from mdnotesccg.models.o_auth_scope_enum import OAuthScopeEnum
from mdnotesccg.models.o_auth_token import OAuthToken

client = MdnotesccgClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_token=OAuthToken(
            access_token='AccessToken',
            token_type='SandboxToken',
            expires_in=3600,
            refresh_token='RefreshToken'
        ),
        o_auth_scopes=[
            OAuthScopeEnum.READ,
            OAuthScopeEnum.WRITE
        ]
    ),
    environment=Environment.PRODUCTION
)

user_controller = client.user
try:
    result = user_controller.get_user()
    print(result)
except APIException as e: 
    print(e)

