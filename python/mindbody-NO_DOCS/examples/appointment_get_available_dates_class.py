import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

appointment_controller = client.appointment
version = '6'

request_session_type_id = 100

site_id = '-99'

authorization = 'authorization6'

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_location_id = 90

request_staff_id = 180

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = appointment_controller.get_available_dates(
        version,
        request_session_type_id,
        site_id,
        authorization=authorization,
        request_end_date=request_end_date,
        request_location_id=request_location_id,
        request_staff_id=request_staff_id,
        request_start_date=request_start_date
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

