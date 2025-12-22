from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.simple_attributes import SimpleAttributes
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

simple_attributes_model_controller = client.simple_attributes_model
body = SimpleAttributes(
    string_element='string-element4',
    nonreserved='nonreserved6',
    number_element=164,
    precision=247.8,
    boolean_element=False,
    attributes_type='SimpleAttributes'
)

try:
    result = simple_attributes_model_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

