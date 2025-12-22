from jsonvaluetester.configuration import Environment
from jsonvaluetester.exceptions.api_exception import APIException
from jsonvaluetester.jsonvaluetester_client import JsonvaluetesterClient
from jsonvaluetester.models.schema_container import SchemaContainer

client = JsonvaluetesterClient(
    environment=Environment.TESTING
)

json_obj_controller = client.json_obj
body = SchemaContainer(
    name='a name',
    id='definition-123',
    schema={"key1":"val1","key2":"val2"}
)

try:
    result = json_obj_controller.send_schemain_model(body)
    print(result)
except APIException as e: 
    print(e)

