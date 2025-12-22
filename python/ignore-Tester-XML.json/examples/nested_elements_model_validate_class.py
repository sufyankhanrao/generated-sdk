from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.model_with_nested_elements_model import ModelWithNestedElementsModel
from testerxml.models.simple_elements import SimpleElements
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

nested_elements_model_controller = client.nested_elements_model
body = ModelWithNestedElementsModel(
    elements=SimpleElements(
        string_element='string-element0',
        nonreserved='nonreserved2',
        number_element=240,
        precision=43.76,
        boolean_element=False,
        model_type='SimpleElements'
    ),
    simple='simple6'
)

try:
    result = nested_elements_model_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

