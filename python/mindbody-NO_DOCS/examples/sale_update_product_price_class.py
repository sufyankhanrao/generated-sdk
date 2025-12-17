from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_product_price_request import UpdateProductPriceRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

request = UpdateProductPriceRequest(
    barcode_id='BarcodeId6',
    price=195.96,
    online_price=230.48
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = sale_controller.update_product_price(
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

