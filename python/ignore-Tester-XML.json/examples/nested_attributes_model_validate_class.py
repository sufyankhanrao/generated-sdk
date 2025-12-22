from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.model_with_nested_attributes_model import ModelWithNestedAttributesModel
from testerxml.models.simple_attributes import SimpleAttributes
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

nested_attributes_model_controller = client.nested_attributes_model
body = ModelWithNestedAttributesModel(
    simple_attributes=SimpleAttributes(
        string_element='string-element6',
        nonreserved='nonreserved8',
        number_element=6,
        precision=28.62,
        boolean_element=False,
        attributes_type='SimpleAttributes'
    ),
    simple='simple6'
)

try:
    result = nested_attributes_model_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

