from pathlib import Path

from testerfilesandmultipart.utilities.file_wrapper import FileWrapper
from testerfilesandmultipart.configuration import Environment
from testerfilesandmultipart.exceptions.api_exception import APIException
from testerfilesandmultipart.testerfilesandmultipart_client import TesterfilesandmultipartClient

client = TesterfilesandmultipartClient(
    environment=Environment.PRODUCTION,
    port='80'
)

form_params_controller = client.form_params
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

file_1 = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

try:
    result = form_params_controller.send_multiple_files(
        file,
        file_1
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

