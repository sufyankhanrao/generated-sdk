from mdnotesccgmodelpostfix.configuration import Environment
from mdnotesccgmodelpostfix.exceptions.api_exception import APIException
from mdnotesccgmodelpostfix.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from mdnotesccgmodelpostfix.mdnotesccgmodelpostfix_client import MdnotesccgmodelpostfixClient
from mdnotesccgmodelpostfix.models.o_auth_scope_enum import OAuthScopeEnum
from mdnotesccgmodelpostfix.models.o_auth_token_model import OAuthTokenModel

client = MdnotesccgmodelpostfixClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_token=OAuthTokenModel(
            access_token='AccessToken',
            token_type='SandboxToken',
            expires_in=3600,
            refresh_token='RefreshToken'
        ),
        o_auth_scopes=[
            OAuthScopeEnum.READ_SCOPE,
            OAuthScopeEnum.WRITE_SCOPE
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

