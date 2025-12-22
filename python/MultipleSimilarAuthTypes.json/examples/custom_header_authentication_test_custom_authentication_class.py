from multiplesimilarauthtypes.configuration import Environment
from multiplesimilarauthtypes.exceptions.api_exception import APIException
from multiplesimilarauthtypes.http.auth.breeze_header import BreezeHeaderCredentials
from multiplesimilarauthtypes.http.auth.custom_header import CustomHeaderCredentials
from multiplesimilarauthtypes.models.suite_code_enum import SuiteCodeEnum
from multiplesimilarauthtypes.multiplesimilarauthtypes_client import MultiplesimilarauthtypesClient

client = MultiplesimilarauthtypesClient(
    breeze_header_credentials=BreezeHeaderCredentials(
        token='token',
        breeze_api_token='Breeze-ApiToken',
        x_api_key='X-Api-Key'
    ),
    custom_header_credentials=CustomHeaderCredentials(
        token='token',
        api_key='api-key'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

custom_header_authentication_controller = client.custom_header_authentication
try:
    result = custom_header_authentication_controller.get_test_custom_authentication()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

