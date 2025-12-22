
from mdnotesropcg.configuration import Environment
from mdnotesropcg.exceptions.api_exception import APIException
from mdnotesropcg.http.auth.o_auth_2 import ResourceOwnerAuthCredentials
from mdnotesropcg.mdnotesropcg_client import MdnotesropcgClient
from mdnotesropcg.models.o_auth_scope_enum import OAuthScopeEnum
from mdnotesropcg.models.o_auth_token import OAuthToken

client = MdnotesropcgClient(
    resource_owner_auth_credentials=ResourceOwnerAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_username='OAuthUsername',
        o_auth_password='OAuthPassword',
        o_auth_token=OAuthToken(
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

service_controller = client.service
try:
    result = service_controller.get_status()
    print(result)
except APIException as e: 
    print(e)

