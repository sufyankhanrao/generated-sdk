import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_class_description_id = 62

request_end_class_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_id = 90

request_offset = 100

request_program_ids = [
    91,
    92,
    93
]

request_staff_id = 180

request_start_class_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = mclass_controller.get_class_descriptions(
        version,
        site_id,
        authorization=authorization,
        request_class_description_id=request_class_description_id,
        request_end_class_date_time=request_end_class_date_time,
        request_limit=request_limit,
        request_location_id=request_location_id,
        request_offset=request_offset,
        request_program_ids=request_program_ids,
        request_staff_id=request_staff_id,
        request_start_class_date_time=request_start_class_date_time
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

