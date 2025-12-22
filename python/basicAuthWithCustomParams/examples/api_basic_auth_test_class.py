from batesterwithcustomparameters.batesterwithcustomparameters_client import BatesterwithcustomparametersClient
from batesterwithcustomparameters.configuration import Environment
from batesterwithcustomparameters.exceptions.api_exception import APIException
from batesterwithcustomparameters.http.auth.basic_auth import BasicAuthCredentials
from batesterwithcustomparameters.models.suite_code_enum import SuiteCodeEnum

client = BatesterwithcustomparametersClient(
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
    print(result)
except APIException as e: 
    print(e)

