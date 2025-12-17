import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.request_schedule_type_enum import RequestScheduleTypeEnum

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

appointment_controller = client.appointment
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_schedule_type = RequestScheduleTypeEnum.RESOURCE

request_session_type_ids = [
    228,
    229
]

request_start_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = appointment_controller.get_active_session_times(
        version,
        site_id,
        authorization=authorization,
        request_end_time=request_end_time,
        request_limit=request_limit,
        request_offset=request_offset,
        request_schedule_type=request_schedule_type,
        request_session_type_ids=request_session_type_ids,
        request_start_time=request_start_time
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

