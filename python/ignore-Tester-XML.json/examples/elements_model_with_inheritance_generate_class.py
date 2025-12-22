from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

elements_model_with_inheritance_controller = client.elements_model_with_inheritance
try:
    result = elements_model_with_inheritance_controller.generate()
    print(result)
except APIException as e: 
    print(e)

