import dateutil.parser

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

request_end_sale_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_payment_method_id = 140

request_sale_id = 32

request_start_sale_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = sale_controller.get_sales(
        version,
        site_id,
        authorization=authorization,
        request_end_sale_date_time=request_end_sale_date_time,
        request_limit=request_limit,
        request_offset=request_offset,
        request_payment_method_id=request_payment_method_id,
        request_sale_id=request_sale_id,
        request_start_sale_date_time=request_start_sale_date_time
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

