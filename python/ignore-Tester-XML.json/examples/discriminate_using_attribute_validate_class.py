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
    print(result)
except APIException as e: 
    print(e)

