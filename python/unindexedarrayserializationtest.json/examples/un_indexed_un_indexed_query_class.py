from unindexedarrayserialization.configuration import Environment
from unindexedarrayserialization.exceptions.api_exception import APIException
from unindexedarrayserialization.models.suite_code_enum import SuiteCodeEnum
from unindexedarrayserialization.unindexedarrayserialization_client import UnindexedarrayserializationClient

client = UnindexedarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

un_indexed_controller = client.un_indexed
query_param = [
    'name',
    'field',
    'address',
    'designation'
]

try:
    result = un_indexed_controller.get_un_indexed_query(query_param)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

