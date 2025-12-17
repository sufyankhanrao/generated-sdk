import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.request_schedule_type_enum import RequestScheduleTypeEnum

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

site_controller = client.site
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_include_inactive = False

request_limit = 62

request_location_id = 90

request_location_ids = [
    192
]

request_offset = 100

request_program_ids = [
    91,
    92,
    93
]

request_resource_ids = [
    62
]

request_schedule_types = [
    RequestScheduleTypeEnum.APPOINTMENT,
    RequestScheduleTypeEnum.RESOURCE,
    RequestScheduleTypeEnum.MEDIA
]

request_session_type_ids = [
    228,
    229
]

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = site_controller.get_resources(
        version,
        site_id,
        authorization=authorization,
        request_end_date_time=request_end_date_time,
        request_include_inactive=request_include_inactive,
        request_limit=request_limit,
        request_location_id=request_location_id,
        request_location_ids=request_location_ids,
        request_offset=request_offset,
        request_program_ids=request_program_ids,
        request_resource_ids=request_resource_ids,
        request_schedule_types=request_schedule_types,
        request_session_type_ids=request_session_type_ids,
        request_start_date_time=request_start_date_time
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

