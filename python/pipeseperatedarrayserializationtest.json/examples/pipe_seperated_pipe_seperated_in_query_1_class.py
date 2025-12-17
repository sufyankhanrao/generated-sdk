from pipeseperatedarrayserialization.configuration import Environment
from pipeseperatedarrayserialization.exceptions.api_exception import APIException
from pipeseperatedarrayserialization.models.suite_code_enum import SuiteCodeEnum
from pipeseperatedarrayserialization.pipeseperatedarrayserialization_client import PipeseperatedarrayserializationClient

client = PipeseperatedarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

pipe_seperated_controller = client.pipe_seperated
dependent = [
    'ab',
    'bc',
    'cd',
    'ef'
]

try:
    result = pipe_seperated_controller.get_pipe_seperated_in_query_1(dependent)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

