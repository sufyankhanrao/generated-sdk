import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

payroll_controller = client.payroll
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_id = 90

request_offset = 100

request_scheduled_service_id = 216

request_scheduled_service_type = 'request.scheduledServiceType6'

request_staff_id = 180

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = payroll_controller.get_scheduled_service_earnings(
        version,
        site_id,
        authorization=authorization,
        request_end_date_time=request_end_date_time,
        request_limit=request_limit,
        request_location_id=request_location_id,
        request_offset=request_offset,
        request_scheduled_service_id=request_scheduled_service_id,
        request_scheduled_service_type=request_scheduled_service_type,
        request_staff_id=request_staff_id,
        request_start_date_time=request_start_date_time
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

