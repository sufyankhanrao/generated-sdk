import jsonpickle

from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.non_inherit_enabled_any import NonInheritEnabledAny

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = NonInheritEnabledAny(
    email='user@example.com',
    additional_properties={
        'stringProperty': jsonpickle.decode('"Some text"'),
        'numberProperty': jsonpickle.decode('123'),
        'booleanProperty': jsonpickle.decode('true'),
        'objectProperty': jsonpickle.decode('{"key":"value"}'),
        'arrayProperty': jsonpickle.decode('[10,20,30]'),
        'parentStringType': jsonpickle.decode('{"name":"Test User","type":"CompSame","company":"OpenAI","additionalProperty1":"Additional Info 1","additionalProperty2":"Additional Info 2"}')
    }
)

try:
    result = body_controller.upload_non_inherit_enabled_any(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

