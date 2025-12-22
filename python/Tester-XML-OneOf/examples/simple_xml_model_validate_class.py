from testerxmloneof.configuration import Environment
from testerxmloneof.exceptions.api_exception import APIException
from testerxmloneof.models.cat import Cat
from testerxmloneof.testerxmloneof_client import TesterxmloneofClient

client = TesterxmloneofClient(
    environment=Environment.TESTING
)

simple_xml_model_controller = client.simple_xml_model
body = Cat(
    meows=False
)

try:
    result = simple_xml_model_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

