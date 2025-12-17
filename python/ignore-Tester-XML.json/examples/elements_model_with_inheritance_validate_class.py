from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.simple_elements import ModelWithInheritedElements
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

elements_model_with_inheritance_controller = client.elements_model_with_inheritance
body = ModelWithInheritedElements(
    string_element='string-element2',
    nonreserved='nonreserved4',
    number_element=150,
    precision=22.38,
    boolean_element=False,
    new_string_field='NewStringField6',
    model_type='ModelWithInheritedElements'
)

try:
    result = elements_model_with_inheritance_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

