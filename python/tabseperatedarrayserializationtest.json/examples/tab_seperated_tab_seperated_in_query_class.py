from tabseperatedarrayserialization.configuration import Environment
from tabseperatedarrayserialization.exceptions.api_exception import APIException
from tabseperatedarrayserialization.models.suite_code_enum import SuiteCodeEnum
from tabseperatedarrayserialization.tabseperatedarrayserialization_client import TabseperatedarrayserializationClient

client = TabseperatedarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

tab_seperated_controller = client.tab_seperated
dependent = [
    'ab',
    'bc',
    'cd',
    'ef'
]

try:
    result = tab_seperated_controller.get_tab_seperated_in_query(dependent)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

