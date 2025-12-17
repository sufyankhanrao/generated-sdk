import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

appointment_controller = client.appointment
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_staff_ids = [
    23,
    24,
    25
]

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = appointment_controller.get_unavailabilities(
        version,
        site_id,
        authorization=authorization,
        request_end_date=request_end_date,
        request_limit=request_limit,
        request_offset=request_offset,
        request_staff_ids=request_staff_ids,
        request_start_date=request_start_date
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

