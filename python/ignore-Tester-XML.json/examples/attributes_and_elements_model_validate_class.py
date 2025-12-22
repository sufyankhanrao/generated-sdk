from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.attributes_and_elements import AttributesAndElements
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

attributes_and_elements_model_controller = client.attributes_and_elements_model
body = AttributesAndElements(
    string_attr='string-attr8',
    number_attr=70,
    string_element='string-element4',
    number_element=164
)

try:
    result = attributes_and_elements_model_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

