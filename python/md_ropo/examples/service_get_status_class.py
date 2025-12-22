from mdnotesropo.configuration import Environment
from mdnotesropo.exceptions.api_exception import APIException
from mdnotesropo.http.auth.o_auth_2 import ResourcePasswordAuthCredentials
from mdnotesropo.mdnotesropo_client import MdnotesropoClient
from mdnotesropo.models.o_auth_scope_enum import OAuthScopeEnum
from mdnotesropo.models.o_auth_token import OAuthToken

client = MdnotesropoClient(
    resource_password_auth_credentials=ResourcePasswordAuthCredentials(
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

