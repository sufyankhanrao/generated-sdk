import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_sale_date_request import UpdateSaleDateRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

request = UpdateSaleDateRequest(
    sale_id=232,
    sale_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = sale_controller.update_sale_date(
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

