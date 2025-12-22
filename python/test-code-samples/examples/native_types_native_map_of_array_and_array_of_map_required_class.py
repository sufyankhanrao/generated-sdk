from testcodesamples.configuration import Environment
from testcodesamples.exceptions.api_exception import APIException
from testcodesamples.testcodesamples_client import TestcodesamplesClient

client = TestcodesamplesClient(
    environment=Environment.TESTING,
    port='80',
    suites=1
)

native_types_controller = client.native_types
boolean_array_of_map = False

boolean_map_of_array = {
    'key0': [
        False
    ]
}

try:
    result = native_types_controller.native_map_of_array_and_array_of_map_required(
        boolean_array_of_map,
        boolean_map_of_array
    )
    print(result)
except APIException as e: 
    print(e)

