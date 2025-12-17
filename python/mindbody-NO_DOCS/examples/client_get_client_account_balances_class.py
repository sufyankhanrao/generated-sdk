import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request_client_ids = [
    'request.clientIds9',
    'request.clientIds0',
    'request.clientIds1'
]

site_id = '-99'

authorization = 'authorization6'

request_balance_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_class_id = 206

request_limit = 62

request_offset = 100

try:
    result = client_controller.get_client_account_balances(
        version,
        request_client_ids,
        site_id,
        authorization=authorization,
        request_balance_date=request_balance_date,
        request_class_id=request_class_id,
        request_limit=request_limit,
        request_offset=request_offset
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

