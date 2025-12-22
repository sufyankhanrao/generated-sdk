from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

simple_elements_model_controller = client.simple_elements_model
try:
    result = simple_elements_model_controller.generate()
    print(result)
except APIException as e: 
    print(e)

