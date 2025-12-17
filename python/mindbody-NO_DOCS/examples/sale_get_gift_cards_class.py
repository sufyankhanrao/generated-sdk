from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_ids = [
    1,
    2
]

request_include_custom_layouts = False

request_limit = 62

request_location_id = 90

request_offset = 100

request_sold_online = False

try:
    result = sale_controller.get_gift_cards(
        version,
        site_id,
        authorization=authorization,
        request_ids=request_ids,
        request_include_custom_layouts=request_include_custom_layouts,
        request_limit=request_limit,
        request_location_id=request_location_id,
        request_offset=request_offset,
        request_sold_online=request_sold_online
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

