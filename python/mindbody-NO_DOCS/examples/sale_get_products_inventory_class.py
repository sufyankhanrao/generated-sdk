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

request_barcode_ids = [
    'request.barcodeIds6'
]

request_limit = 62

request_location_ids = [
    192
]

request_offset = 100

request_product_ids = [
    'request.productIds3',
    'request.productIds4'
]

try:
    result = sale_controller.get_products_inventory(
        version,
        site_id,
        authorization=authorization,
        request_barcode_ids=request_barcode_ids,
        request_limit=request_limit,
        request_location_ids=request_location_ids,
        request_offset=request_offset,
        request_product_ids=request_product_ids
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

