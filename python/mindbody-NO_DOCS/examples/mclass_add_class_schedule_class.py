import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_class_enrollment_schedule_request import AddClassEnrollmentScheduleRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

request = AddClassEnrollmentScheduleRequest(
    class_description_id=66,
    location_id=238,
    start_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    end_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    start_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = mclass_controller.add_class_schedule(
        version,
        request,
        site_id,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

