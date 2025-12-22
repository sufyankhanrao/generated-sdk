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
    1,
    2,
    3,
    4
]

try:
    result = comma_seperated_controller.get_comma_seperated_in_query(dependent)
    print(result)
except APIException as e: 
    print(e)

