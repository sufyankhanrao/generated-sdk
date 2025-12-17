from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_product_request import UpdateProductRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

site_id = '-99'

update_products_requests = [
    UpdateProductRequest(
        barcode_id='BarcodeId2',
        price=47.22,
        online_price=81.74
    ),
    UpdateProductRequest(
        barcode_id='BarcodeId2',
        price=47.22,
        online_price=81.74
    )
]

authorization = 'authorization6'

try:
    result = sale_controller.update_products(
        version,
        site_id,
        update_products_requests,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

