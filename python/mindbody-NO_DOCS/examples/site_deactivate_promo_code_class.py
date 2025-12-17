from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.deactivate_promo_code_request import DeactivatePromoCodeRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

site_controller = client.site
version = '6'

request = DeactivatePromoCodeRequest(
    promotion_id=42
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = site_controller.deactivate_promo_code(
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

