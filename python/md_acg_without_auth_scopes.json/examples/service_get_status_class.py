
from mdnotesacgwithoutauthscopes.configuration import Environment
from mdnotesacgwithoutauthscopes.exceptions.api_exception import APIException
from mdnotesacgwithoutauthscopes.http.auth.o_auth_2 import AuthorizationCodeAuthCredentials
from mdnotesacgwithoutauthscopes.mdnotesacgwithoutauthscopes_client import MdnotesacgwithoutauthscopesClient
from mdnotesacgwithoutauthscopes.models.o_auth_token import OAuthToken

client = MdnotesacgwithoutauthscopesClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_redirect_uri='OAuthRedirectUri',
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

