from pathlib import Path

from retriestester.utilities.file_wrapper import FileWrapper
from retriestester.configuration import Environment
from retriestester.exceptions.api_exception import APIException
from retriestester.retriestester_client import RetriestesterClient

client = RetriestesterClient(
    environment=Environment.TESTING
)

client_controller = client.client
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

try:
    result = client_controller.retry_send_file(file)
    print(result)
except APIException as e: 
    print(e)

