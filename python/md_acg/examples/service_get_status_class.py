
from mdnotesacg.configuration import Environment
from mdnotesacg.exceptions.api_exception import APIException
from mdnotesacg.http.auth.o_auth_2 import AuthorizationCodeAuthCredentials
from mdnotesacg.mdnotesacg_client import MdnotesacgClient
from mdnotesacg.models.o_auth_scope_enum import OAuthScopeEnum
from mdnotesacg.models.o_auth_token import OAuthToken

client = MdnotesacgClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_redirect_uri='OAuthRedirectUri',
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

service_controller = client.service
try:
    result = service_controller.get_status()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

