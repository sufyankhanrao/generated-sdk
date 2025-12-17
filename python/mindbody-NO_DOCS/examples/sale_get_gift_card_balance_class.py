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

barcode_id = 'barcodeId6'

try:
    result = sale_controller.get_gift_card_balance(
        version,
        site_id,
        authorization=authorization,
        barcode_id=barcode_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

