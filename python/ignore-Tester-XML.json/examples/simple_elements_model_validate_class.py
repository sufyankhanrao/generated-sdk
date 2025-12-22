from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.simple_elements import SimpleElements
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

simple_elements_model_controller = client.simple_elements_model
body = SimpleElements(
    string_element='string-element4',
    nonreserved='nonreserved6',
    number_element=164,
    precision=247.8,
    boolean_element=False,
    model_type='SimpleElements'
)

try:
    result = simple_elements_model_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

