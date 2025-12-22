from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.base_for_discriminator_in_attribute import BaseForDiscriminatorInAttribute
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

discriminate_using_attribute_controller = client.discriminate_using_attribute
body = BaseForDiscriminatorInAttribute(
    base_field='Base Field6',
    discriminator='Darth Vader'
)

try:
    result = discriminate_using_attribute_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

