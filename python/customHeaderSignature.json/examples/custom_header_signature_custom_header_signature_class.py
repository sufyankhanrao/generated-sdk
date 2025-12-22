from customheadersignature.configuration import Environment
from customheadersignature.customheadersignature_client import CustomheadersignatureClient
from customheadersignature.exceptions.api_exception import APIException
from customheadersignature.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from customheadersignature.models.suite_code_enum import SuiteCodeEnum

client = CustomheadersignatureClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        token='token',
        api_key='api-key'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

custom_header_signature_controller = client.custom_header_signature
try:
    result = custom_header_signature_controller.get_custom_header_signature()
    print(result)
except APIException as e: 
    print(e)

