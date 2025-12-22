from multiauthsample.configuration import Environment
from multiauthsample.exceptions.api_exception import APIException
from multiauthsample.http.auth.api_header import ApiHeaderCredentials
from multiauthsample.http.auth.api_key import ApiKeyCredentials
from multiauthsample.models.suite_code_enum import SuiteCodeEnum
from multiauthsample.multiauthsample_client import MultiauthsampleClient

client = MultiauthsampleClient(
    access_token='accessToken',
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
    result = authentication_controller.custom_query_or_header_authentication()
    print(result)
except APIException as e: 
    print(e)

