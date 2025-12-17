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

request_client_id = 222

request_limit = 62

request_location_id = 90

request_offset = 100

request_sale_id = 32

request_status = 'request.status2'

request_transaction_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_transaction_id = 200

request_transaction_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = sale_controller.get_transactions(
        version,
        site_id,
        authorization=authorization,
        request_client_id=request_client_id,
        request_limit=request_limit,
        request_location_id=request_location_id,
        request_offset=request_offset,
        request_sale_id=request_sale_id,
        request_status=request_status,
        request_transaction_end_date_time=request_transaction_end_date_time,
        request_transaction_id=request_transaction_id,
        request_transaction_start_date_time=request_transaction_start_date_time
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

