from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

discriminate_using_element_controller = client.discriminate_using_element
try:
    result = discriminate_using_element_controller.generate()
    print(result)
except APIException as e: 
    print(e)

