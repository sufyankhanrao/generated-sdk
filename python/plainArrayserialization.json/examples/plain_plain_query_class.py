from plainarrayserialization.configuration import Environment
from plainarrayserialization.exceptions.api_exception import APIException
from plainarrayserialization.models.suite_code_enum import SuiteCodeEnum
from plainarrayserialization.plainarrayserialization_client import PlainarrayserializationClient

client = PlainarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

plain_controller = client.plain
query_param = [
    'name',
    'field',
    'address',
    'designation'
]

try:
    result = plain_controller.get_plain_query(query_param)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

