from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

request_location_id = 90

site_id = '-99'

authorization = 'authorization6'

request_consumer_id = 120

request_contract_ids = [
    39,
    40
]

request_limit = 62

request_offset = 100

request_promo_code = 'request.promoCode0'

request_sold_online = False

try:
    result = sale_controller.get_contracts(
        version,
        request_location_id,
        site_id,
        authorization=authorization,
        request_consumer_id=request_consumer_id,
        request_contract_ids=request_contract_ids,
        request_limit=request_limit,
        request_offset=request_offset,
        request_promo_code=request_promo_code,
        request_sold_online=request_sold_online
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

