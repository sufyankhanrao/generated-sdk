from plainarrayserialization.configuration import Environment
from plainarrayserialization.exceptions.api_exception import APIException
from plainarrayserialization.models.employee import Employee
from plainarrayserialization.models.person import Person
from plainarrayserialization.models.suite_code_enum import SuiteCodeEnum
from plainarrayserialization.plainarrayserialization_client import PlainarrayserializationClient

client = PlainarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

plain_controller = client.plain
model = Employee(
    age=15,
    dependents=[
        Person(
            name='rehan',
            field='front-end'
        ),
        Person(
            name='Gill',
            field='back-end'
        )
    ]
)

try:
    result = plain_controller.create_plain_form(model)
    print(result)
except APIException as e: 
    print(e)

