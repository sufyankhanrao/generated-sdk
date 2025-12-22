from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.simple_array_with_element_name import SimpleArrayWithElementName
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

named_elements_array_controller = client.named_elements_array
body = SimpleArrayWithElementName(
    elem=[
        'elem5'
    ]
)

try:
    result = named_elements_array_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

