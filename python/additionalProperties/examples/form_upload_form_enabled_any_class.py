import jsonpickle

from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.any_of_additional_properties import AnyOfAdditionalProperties
from additionalpropertiestester.models.complex_model_with_string_additional_properties import ComplexModelWithStringAdditionalProperties
from additionalpropertiestester.models.non_inherit_enabled_any import NonInheritEnabledAny

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

form_controller = client.form
non_inherit_enabled_any = NonInheritEnabledAny(
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

any_of_additional_properties = AnyOfAdditionalProperties(
    required_property=ComplexModelWithStringAdditionalProperties(
        name='Complex Model',
        age='35',
        additional_properties={
            'additionalProp': 'string'
        }
    ),
    additional_properties={
        'additionalProperty': ComplexModelWithStringAdditionalProperties(
            name='Additional Property',
            age='30',
            additional_properties={
                'additionalProp1': 'string1'
            }
        )
    }
)

try:
    result = form_controller.upload_form_enabled_any(
        non_inherit_enabled_any,
        any_of_additional_properties
    )
    print(result)
except APIException as e: 
    print(e)

