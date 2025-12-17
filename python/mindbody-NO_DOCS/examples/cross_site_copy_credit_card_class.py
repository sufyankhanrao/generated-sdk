from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.copy_credit_card_request import CopyCreditCardRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

cross_site_controller = client.cross_site
version = '6'

request = CopyCreditCardRequest(
    source_site_id=42,
    source_client_id='SourceClientId8',
    target_site_id=26,
    target_client_id='TargetClientId8'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = cross_site_controller.copy_credit_card(
        version,
        request,
        site_id,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

