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
    1,
    2,
    3,
    4
]

try:
    result = pipe_seperated_controller.get_pipe_seperated_in_query(dependent)
    print(result)
except APIException as e: 
    print(e)

