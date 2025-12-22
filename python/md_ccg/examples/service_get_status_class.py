from mdnotesccg.configuration import Environment
from mdnotesccg.exceptions.api_exception import APIException
from mdnotesccg.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from mdnotesccg.mdnotesccg_client import MdnotesccgClient
from mdnotesccg.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesccgClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
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
    print(result)
except APIException as e: 
    print(e)

