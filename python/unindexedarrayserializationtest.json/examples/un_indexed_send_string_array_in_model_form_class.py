from unindexedarrayserialization.configuration import Environment
from unindexedarrayserialization.exceptions.api_exception import APIException
from unindexedarrayserialization.models.model import Model
from unindexedarrayserialization.models.suite_code_enum import SuiteCodeEnum
from unindexedarrayserialization.unindexedarrayserialization_client import UnindexedarrayserializationClient

client = UnindexedarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

un_indexed_controller = client.un_indexed
body = Model(
    name='farhan',
    dependents=[
        'name',
        'field',
        'address',
        'designation'
    ]
)

try:
    result = un_indexed_controller.create_send_string_array_in_model_form(body)
    print(result)
except APIException as e: 
    print(e)

