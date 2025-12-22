from multiauthsample.configuration import Environment
from multiauthsample.exceptions.api_exception import APIException
from multiauthsample.http.auth.o_auth_ccg import OAuthCCGCredentials
from multiauthsample.models.o_auth_token import OAuthToken
from multiauthsample.models.suite_code_enum import SuiteCodeEnum
from multiauthsample.multiauthsample_client import MultiauthsampleClient

client = MultiauthsampleClient(
    access_token='accessToken',
    o_auth_ccg_credentials=OAuthCCGCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_token=OAuthToken(
            access_token='AccessToken',
            token_type='SandboxToken',
            expires_in=3600,
            refresh_token='RefreshToken'
        )
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

authentication_controller = client.authentication
try:
    result = authentication_controller.o_auth_client_credentials_grant()
    print(result)
except APIException as e: 
    print(e)

