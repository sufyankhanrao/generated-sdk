import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_client_to_enrollment_request import AddClientToEnrollmentRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

enrollment_controller = client.enrollment
version = '6'

request = AddClientToEnrollmentRequest(
    client_id='ClientId0',
    class_schedule_id=36,
    enroll_date_forward=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    enroll_open=[
        dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ],
    test=False,
    send_email=False,
    waitlist=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = enrollment_controller.add_client_to_enrollment(
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

