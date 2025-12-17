from oa2tester.configuration import Environment
from oa2tester.exceptions.api_exception import APIException
from oa2tester.http.auth.o_auth_2 import BearerAuthCredentials
from oa2tester.models.suite_code_enum import SuiteCodeEnum
from oa2tester.oa_2_tester_client import Oa2testerClient

client = Oa2testerClient(
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

