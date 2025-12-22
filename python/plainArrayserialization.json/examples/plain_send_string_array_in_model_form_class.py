from plainarrayserialization.configuration import Environment
from plainarrayserialization.exceptions.api_exception import APIException
from plainarrayserialization.models.model import Model
from plainarrayserialization.models.suite_code_enum import SuiteCodeEnum
from plainarrayserialization.plainarrayserialization_client import PlainarrayserializationClient

client = PlainarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

plain_controller = client.plain
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
    result = plain_controller.create_send_string_array_in_model_form(body)
    print(result)
except APIException as e: 
    print(e)

