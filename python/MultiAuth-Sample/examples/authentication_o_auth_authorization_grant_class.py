import sys

from multiauthsample.configuration import Environment
from multiauthsample.exceptions.api_exception import APIException
from multiauthsample.exceptions.o_auth_provider_exception import OAuthProviderException
from multiauthsample.http.auth.o_auth_acg import OAuthACGCredentials
from multiauthsample.http.auth.o_auth_ropcg import OAuthROPCGCredentials
from multiauthsample.models.o_auth_scope_o_auth_acg_enum import OAuthScopeOAuthACGEnum
from multiauthsample.models.suite_code_enum import SuiteCodeEnum
from multiauthsample.multiauthsample_client import MultiauthsampleClient

client = MultiauthsampleClient(
    access_token='accessToken',
    o_auth_acg_credentials=OAuthACGCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_redirect_uri='OAuthRedirectUri',
        o_auth_scopes=[
            OAuthScopeOAuthACGEnum.READ_SCOPE
        ]
    ),
    o_auth_ropcg_credentials=OAuthROPCGCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_username='OAuthUsername',
        o_auth_password='OAuthPassword'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

# obtain the o_auth_token for OAuthACG
try:
    auth_url = client.o_auth_acg.get_authorization_url()
    # redirect user to this auth_url and get a code after the user consent
    code = 'extracted code'
    token = client.o_auth_acg.fetch_token(code)
    o_auth_acg_credentials = client.config.o_auth_acg_credentials.clone_with(o_auth_token=token)
    config = client.config.clone_with(o_auth_acg_credentials=o_auth_acg_credentials)
    client = MultiauthsampleClient(config=config)
except OAuthProviderException as ex:
    # handle exception
    print(ex)
    sys.exit()
except APIException as ex:
    # handle exception
    print(ex)
    sys.exit()

# obtain the o_auth_token for OAuthROPCG
try:
    token = client.o_auth_ropcg.fetch_token()
    o_auth_ropcg_credentials = client.config.o_auth_ropcg_credentials.clone_with(o_auth_token=token)
    config = client.config.clone_with(o_auth_ropcg_credentials=o_auth_ropcg_credentials)
    client = MultiauthsampleClient(config=config)
except OAuthProviderException as ex:
    # handle exception
    print(ex)
    sys.exit()
except APIException as ex:
    # handle exception
    print(ex)
    sys.exit()

authentication_controller = client.authentication
try:
    result = authentication_controller.o_auth_authorization_grant()
    print(result)
except APIException as e: 
    print(e)

