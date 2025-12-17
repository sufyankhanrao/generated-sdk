from jwttester.configuration import Environment
from jwttester.exceptions.api_exception import APIException
from jwttester.http.auth.o_auth_2 import BearerAuthCredentials
from jwttester.jwttester_client import JwttesterClient
from jwttester.models.suite_code_enum import SuiteCodeEnum

client = JwttesterClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

client_controller = client.client
try:
    result = client_controller.get_o_auth_2_test()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

