import sys

from mdnotesropcg.configuration import Environment
from mdnotesropcg.exceptions.api_exception import APIException
from mdnotesropcg.exceptions.o_auth_provider_exception import OAuthProviderException
from mdnotesropcg.http.auth.o_auth_2 import ResourceOwnerAuthCredentials
from mdnotesropcg.mdnotesropcg_client import MdnotesropcgClient
from mdnotesropcg.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesropcgClient(
    resource_owner_auth_credentials=ResourceOwnerAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_username='OAuthUsername',
        o_auth_password='OAuthPassword',
        o_auth_scopes=[
            OAuthScopeEnum.READ_SCOPE,
            OAuthScopeEnum.WRITE_SCOPE
        ]
    ),
    environment=Environment.PRODUCTION
)

# obtain the o_auth_token for ResourceOwnerAuth
try:
    token = client.http_ropcg.fetch_token()
    resource_owner_auth_credentials = client.config.resource_owner_auth_credentials.clone_with(o_auth_token=token)
    config = client.config.clone_with(resource_owner_auth_credentials=resource_owner_auth_credentials)
    client = MdnotesropcgClient(config=config)
except OAuthProviderException as ex:
    # handle exception
    print(ex)
    sys.exit()
except APIException as ex:
    # handle exception
    print(ex)
    sys.exit()

user_controller = client.user
try:
    result = user_controller.get_user()
    print(result)
except APIException as e: 
    print(e)

