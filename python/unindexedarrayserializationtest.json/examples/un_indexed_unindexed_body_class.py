from unindexedarrayserialization.configuration import Environment
from unindexedarrayserialization.exceptions.api_exception import APIException
from unindexedarrayserialization.models.employee import Employee
from unindexedarrayserialization.models.person import Person
from unindexedarrayserialization.models.suite_code_enum import SuiteCodeEnum
from unindexedarrayserialization.unindexedarrayserialization_client import UnindexedarrayserializationClient

client = UnindexedarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

un_indexed_controller = client.un_indexed
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
    result = un_indexed_controller.create_unindexed_body(model)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

