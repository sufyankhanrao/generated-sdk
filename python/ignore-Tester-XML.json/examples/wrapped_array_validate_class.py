from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.wrapped_array_with_element_name import WrappedArrayWithElementName
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

wrapped_array_controller = client.wrapped_array
body = WrappedArrayWithElementName(
    elem=[
        'elem5'
    ]
)

try:
    result = wrapped_array_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

