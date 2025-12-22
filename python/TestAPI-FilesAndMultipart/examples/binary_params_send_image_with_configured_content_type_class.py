from pathlib import Path

from testerfilesandmultipart.utilities.file_wrapper import FileWrapper
from testerfilesandmultipart.configuration import Environment
from testerfilesandmultipart.exceptions.api_exception import APIException
from testerfilesandmultipart.testerfilesandmultipart_client import TesterfilesandmultipartClient

client = TesterfilesandmultipartClient(
    environment=Environment.PRODUCTION,
    port='80'
)

binary_params_controller = client.binary_params
collect = {
    'content_type': 'content-type8',
    'image': FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type'),
    'is_image': 'true'
}
try:
    result = binary_params_controller.send_image_with_configured_content_type(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

