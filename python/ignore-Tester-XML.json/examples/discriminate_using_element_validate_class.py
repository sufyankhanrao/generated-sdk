from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.base_for_discriminator_in_element import BaseForDiscriminatorInElement
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

discriminate_using_element_controller = client.discriminate_using_element
body = BaseForDiscriminatorInElement(
    base_field='Base Field6',
    discriminator='Anakin Skywalker'
)

try:
    result = discriminate_using_element_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

