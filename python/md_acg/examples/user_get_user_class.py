import sys

from mdnotesacg.configuration import Environment
from mdnotesacg.exceptions.api_exception import APIException
from mdnotesacg.exceptions.o_auth_provider_exception import OAuthProviderException
from mdnotesacg.http.auth.o_auth_2 import AuthorizationCodeAuthCredentials
from mdnotesacg.mdnotesacg_client import MdnotesacgClient
from mdnotesacg.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesacgClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_redirect_uri='OAuthRedirectUri',
        o_auth_scopes=[
            OAuthScopeEnum.READ,
            OAuthScopeEnum.WRITE
        ]
    ),
    environment=Environment.PRODUCTION
)

# obtain the o_auth_token for AuthorizationCodeAuth
try:
    auth_url = client.http_acg.get_authorization_url()
    # redirect user to this auth_url and get a code after the user consent
    code = 'extracted code'
    token = client.http_acg.fetch_token(code)
    authorization_code_auth_credentials = client.config.authorization_code_auth_credentials.clone_with(o_auth_token=token)
    config = client.config.clone_with(authorization_code_auth_credentials=authorization_code_auth_credentials)
    client = MdnotesacgClient(config=config)
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

