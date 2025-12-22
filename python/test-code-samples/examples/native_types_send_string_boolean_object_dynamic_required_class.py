import jsonpickle

from testcodesamples.configuration import Environment
from testcodesamples.exceptions.api_exception import APIException
from testcodesamples.testcodesamples_client import TestcodesamplesClient

client = TestcodesamplesClient(
    environment=Environment.TESTING,
    port='80',
    suites=1
)

native_types_controller = client.native_types
string_var = 'stringVar8'

boolean_var = False

object_var = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

dynamic_var = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

try:
    result = native_types_controller.send_string_boolean_object_dynamic_required(
        string_var,
        boolean_var,
        object_var,
        dynamic_var
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

