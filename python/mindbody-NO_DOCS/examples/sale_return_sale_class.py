from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.return_sale_request import ReturnSaleRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

return_sale_request = ReturnSaleRequest(
    sale_id=6,
    return_reason='ReturnReason8'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = sale_controller.return_sale(
        version,
        return_sale_request,
        site_id,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

