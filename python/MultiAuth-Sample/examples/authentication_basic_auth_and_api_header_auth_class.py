from multiauthsample.configuration import Environment
from multiauthsample.exceptions.api_exception import APIException
from multiauthsample.http.auth.api_header import ApiHeaderCredentials
from multiauthsample.http.auth.api_key import ApiKeyCredentials
from multiauthsample.http.auth.basic_auth import BasicAuthCredentials
from multiauthsample.models.suite_code_enum import SuiteCodeEnum
from multiauthsample.multiauthsample_client import MultiauthsampleClient

client = MultiauthsampleClient(
    access_token='accessToken',
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    api_key_credentials=ApiKeyCredentials(
        token='token',
        api_key='api-key'
    ),
    api_header_credentials=ApiHeaderCredentials(
        token='token',
        api_key='api-key'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

authentication_controller = client.authentication
try:
    result = authentication_controller.basic_auth_and_api_header_auth()
    print(result)
except APIException as e: 
    print(e)

