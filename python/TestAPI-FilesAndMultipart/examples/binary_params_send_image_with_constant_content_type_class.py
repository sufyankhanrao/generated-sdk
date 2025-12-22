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
image = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

try:
    result = binary_params_controller.send_image_with_constant_content_type(image)
    print(result)
except APIException as e: 
    print(e)

