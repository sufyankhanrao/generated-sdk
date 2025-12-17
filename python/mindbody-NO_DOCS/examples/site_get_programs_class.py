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

request_limit = 62

request_offset = 100

request_online_only = False

request_program_ids = [
    91,
    92,
    93
]

request_schedule_type = RequestScheduleTypeEnum.RESOURCE

try:
    result = site_controller.get_programs(
        version,
        site_id,
        authorization=authorization,
        request_limit=request_limit,
        request_offset=request_offset,
        request_online_only=request_online_only,
        request_program_ids=request_program_ids,
        request_schedule_type=request_schedule_type
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

