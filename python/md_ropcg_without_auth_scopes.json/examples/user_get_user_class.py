import sys

from mdnotesropcgwithoutauthscopes.configuration import Environment
from mdnotesropcgwithoutauthscopes.exceptions.api_exception import APIException
from mdnotesropcgwithoutauthscopes.exceptions.o_auth_provider_exception import OAuthProviderException
from mdnotesropcgwithoutauthscopes.http.auth.o_auth_2 import ResourceOwnerAuthCredentials
from mdnotesropcgwithoutauthscopes.mdnotesropcgwithoutauthscopes_client import MdnotesropcgwithoutauthscopesClient

client = MdnotesropcgwithoutauthscopesClient(
    resource_owner_auth_credentials=ResourceOwnerAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_username='OAuthUsername',
        o_auth_password='OAuthPassword'
    ),
    environment=Environment.PRODUCTION
)

# obtain the o_auth_token for ResourceOwnerAuth
try:
    token = client.http_ropcg.fetch_token()
    resource_owner_auth_credentials = client.config.resource_owner_auth_credentials.clone_with(o_auth_token=token)
    config = client.config.clone_with(resource_owner_auth_credentials=resource_owner_auth_credentials)
    client = MdnotesropcgwithoutauthscopesClient(config=config)
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

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

