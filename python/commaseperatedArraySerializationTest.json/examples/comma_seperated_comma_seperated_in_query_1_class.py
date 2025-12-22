from commaseperatedarrayserialization.commaseperatedarrayserialization_client import CommaseperatedarrayserializationClient
from commaseperatedarrayserialization.configuration import Environment
from commaseperatedarrayserialization.exceptions.api_exception import APIException
from commaseperatedarrayserialization.models.suite_code_enum import SuiteCodeEnum

client = CommaseperatedarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

comma_seperated_controller = client.comma_seperated
dependent = [
    'ab',
    'bc',
    'cd',
    'ef'
]

try:
    result = comma_seperated_controller.get_comma_seperated_in_query_1(dependent)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

