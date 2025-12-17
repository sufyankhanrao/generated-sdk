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

request_category_ids = [
    140,
    141
]

request_limit = 62

request_location_id = 90

request_offset = 100

request_product_ids = [
    'request.productIds3',
    'request.productIds4'
]

request_search_text = 'request.searchText0'

request_sell_online = False

request_sub_category_ids = [
    173,
    174,
    175
]

try:
    result = sale_controller.get_products(
        version,
        site_id,
        authorization=authorization,
        request_category_ids=request_category_ids,
        request_limit=request_limit,
        request_location_id=request_location_id,
        request_offset=request_offset,
        request_product_ids=request_product_ids,
        request_search_text=request_search_text,
        request_sell_online=request_sell_online,
        request_sub_category_ids=request_sub_category_ids
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

