from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_service_request import UpdateServiceRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

site_id = '-99'

update_services_request = [
    UpdateServiceRequest(
        barcode_id='BarcodeId8',
        price=176.98,
        online_price=211.5
    )
]

authorization = 'authorization6'

try:
    result = sale_controller.update_services(
        version,
        site_id,
        update_services_request,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

