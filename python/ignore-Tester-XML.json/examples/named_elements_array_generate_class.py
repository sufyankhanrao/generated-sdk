from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

named_elements_array_controller = client.named_elements_array
try:
    result = named_elements_array_controller.generate()
    print(result)
except APIException as e: 
    print(e)

