from multiauthsample.configuration import Environment
from multiauthsample.exceptions.api_exception import APIException
from multiauthsample.models.suite_code_enum import SuiteCodeEnum
from multiauthsample.multiauthsample_client import MultiauthsampleClient

client = MultiauthsampleClient(
    access_token='accessToken',
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

authentication_controller = client.authentication
try:
    result = authentication_controller.no_auth()
    print(result)
except APIException as e: 
    print(e)

