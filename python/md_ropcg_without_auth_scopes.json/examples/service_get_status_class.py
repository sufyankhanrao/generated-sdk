
from mdnotesropcgwithoutauthscopes.configuration import Environment
from mdnotesropcgwithoutauthscopes.exceptions.api_exception import APIException
from mdnotesropcgwithoutauthscopes.http.auth.o_auth_2 import ResourceOwnerAuthCredentials
from mdnotesropcgwithoutauthscopes.mdnotesropcgwithoutauthscopes_client import MdnotesropcgwithoutauthscopesClient
from mdnotesropcgwithoutauthscopes.models.o_auth_token import OAuthToken

client = MdnotesropcgwithoutauthscopesClient(
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
        )
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

