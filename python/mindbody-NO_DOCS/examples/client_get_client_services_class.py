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

request_class_id = 206

request_client_associated_sites_offset = 146

request_client_ids = [
    'request.clientIds9',
    'request.clientIds0',
    'request.clientIds1'
]

request_cross_regional_lookup = False

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_ignore_cross_regional_site_limit = False

request_limit = 62

request_location_ids = [
    192
]

request_offset = 100

request_program_ids = [
    91,
    92,
    93
]

request_session_type_id = 100

request_show_active_only = False

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_use_activate_date = False

request_visit_count = 18

try:
    result = client_controller.get_client_services(
        version,
        request_client_id,
        site_id,
        authorization=authorization,
        request_class_id=request_class_id,
        request_client_associated_sites_offset=request_client_associated_sites_offset,
        request_client_ids=request_client_ids,
        request_cross_regional_lookup=request_cross_regional_lookup,
        request_end_date=request_end_date,
        request_ignore_cross_regional_site_limit=request_ignore_cross_regional_site_limit,
        request_limit=request_limit,
        request_location_ids=request_location_ids,
        request_offset=request_offset,
        request_program_ids=request_program_ids,
        request_session_type_id=request_session_type_id,
        request_show_active_only=request_show_active_only,
        request_start_date=request_start_date,
        request_use_activate_date=request_use_activate_date,
        request_visit_count=request_visit_count
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

