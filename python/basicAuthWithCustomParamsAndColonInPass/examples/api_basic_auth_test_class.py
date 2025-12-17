from batesterparamscoloninpassword.batesterparamscoloninpassword_client import BatesterparamscoloninpasswordClient
from batesterparamscoloninpassword.configuration import Environment
from batesterparamscoloninpassword.exceptions.api_exception import APIException
from batesterparamscoloninpassword.http.auth.basic_auth import BasicAuthCredentials
from batesterparamscoloninpassword.models.suite_code_enum import SuiteCodeEnum

client = BatesterparamscoloninpasswordClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='username',
        password='password'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

client_controller = client.client
try:
    result = client_controller.get_basic_auth_test()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

