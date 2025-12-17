from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_pricing_option_request import UpdatePricingOptionRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

pricing_option_controller = client.pricing_option
version = '6'

request = UpdatePricingOptionRequest(
    product_id=16.72,
    name='Name6',
    price=195.96,
    online_price=230.48,
    count=242,
    sell_online=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = pricing_option_controller.update_pricing_option(
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

