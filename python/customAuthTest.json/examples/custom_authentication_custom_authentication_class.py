from customauthentication.configuration import Environment
from customauthentication.customauthentication_client import CustomauthenticationClient
from customauthentication.exceptions.api_exception import APIException
from customauthentication.models.suite_code_enum import SuiteCodeEnum

client = CustomauthenticationClient(
    access_token='accessToken',
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

custom_authentication_controller = client.custom_authentication
try:
    result = custom_authentication_controller.get_custom_authentication()
    print(result)
except APIException as e: 
    print(e)

