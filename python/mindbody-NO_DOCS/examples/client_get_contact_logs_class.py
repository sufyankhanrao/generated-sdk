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

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_show_system_generated = False

request_staff_ids = [
    23,
    24,
    25
]

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_subtype_ids = [
    141
]

request_type_ids = [
    63
]

try:
    result = client_controller.get_contact_logs(
        version,
        request_client_id,
        site_id,
        authorization=authorization,
        request_end_date=request_end_date,
        request_limit=request_limit,
        request_offset=request_offset,
        request_show_system_generated=request_show_system_generated,
        request_staff_ids=request_staff_ids,
        request_start_date=request_start_date,
        request_subtype_ids=request_subtype_ids,
        request_type_ids=request_type_ids
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

