import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request_client_id = 'request.clientId2'

site_id = '-99'

authorization = 'authorization6'

request_client_associated_sites_offset = 146

request_cross_regional_lookup = False

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = client_controller.get_client_schedule(
        version,
        request_client_id,
        site_id,
        authorization=authorization,
        request_client_associated_sites_offset=request_client_associated_sites_offset,
        request_cross_regional_lookup=request_cross_regional_lookup,
        request_end_date=request_end_date,
        request_limit=request_limit,
        request_offset=request_offset,
        request_start_date=request_start_date
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

