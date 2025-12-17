from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.simple_array import SimpleArray
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

elements_array_controller = client.elements_array
body = SimpleArray(
    elem=[
        'elem5'
    ]
)

try:
    result = elements_array_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

