from customqueryparameter.configuration import Environment
from customqueryparameter.customqueryparameter_client import CustomqueryparameterClient
from customqueryparameter.exceptions.api_exception import APIException
from customqueryparameter.models.suite_code_enum import SuiteCodeEnum

client = CustomqueryparameterClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

custom_query_param_test_controller = client.custom_query_param_test
try:
    result = custom_query_param_test_controller.get_custom_query_param_skipped_authentication()
    print(result)
except APIException as e: 
    print(e)

