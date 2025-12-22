from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.wrapped_array_with_element_and_wrapping_name import WrappedArrayWithElementAndWrappingName
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

wrapped_and_named_array_controller = client.wrapped_and_named_array
body = WrappedArrayWithElementAndWrappingName(
    elem=[
        'elem5'
    ]
)

try:
    result = wrapped_and_named_array_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

