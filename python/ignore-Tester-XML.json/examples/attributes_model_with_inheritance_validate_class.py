from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.simple_attributes import ModelWithInheritedAttributes
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

attributes_model_with_inheritance_controller = client.attributes_model_with_inheritance
body = ModelWithInheritedAttributes(
    string_element='string-element6',
    nonreserved='nonreserved8',
    number_element=6,
    precision=28.62,
    boolean_element=False,
    new_string_field='NewStringField6',
    attributes_type='ModelWithInheritedAttributes'
)

try:
    result = attributes_model_with_inheritance_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

