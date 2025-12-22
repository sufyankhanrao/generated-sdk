from multiauthsample.configuration import Environment
from multiauthsample.exceptions.api_exception import APIException
from multiauthsample.http.auth.o_auth_bearer_token import OAuthBearerTokenCredentials
from multiauthsample.http.auth.o_auth_ccg import OAuthCCGCredentials
from multiauthsample.models.suite_code_enum import SuiteCodeEnum
from multiauthsample.multiauthsample_client import MultiauthsampleClient

client = MultiauthsampleClient(
    access_token='accessToken',
    o_auth_ccg_credentials=OAuthCCGCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    o_auth_bearer_token_credentials=OAuthBearerTokenCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

authentication_controller = client.authentication
try:
    result = authentication_controller.o_auth_grant_types_or_combinations()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

