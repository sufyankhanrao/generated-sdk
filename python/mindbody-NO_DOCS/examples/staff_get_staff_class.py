import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

staff_controller = client.staff
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_filters = [
    'request.filters0',
    'request.filters1',
    'request.filters2'
]

request_limit = 62

request_location_id = 90

request_offset = 100

request_session_type_id = 100

request_staff_ids = [
    23,
    24,
    25
]

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = staff_controller.get_staff(
        version,
        site_id,
        authorization=authorization,
        request_filters=request_filters,
        request_limit=request_limit,
        request_location_id=request_location_id,
        request_offset=request_offset,
        request_session_type_id=request_session_type_id,
        request_staff_ids=request_staff_ids,
        request_start_date_time=request_start_date_time
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

