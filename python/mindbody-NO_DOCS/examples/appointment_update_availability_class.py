import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.days_of_week_enum import DaysOfWeekEnum
from mindbodypublicapi.models.public_display_enum import PublicDisplayEnum
from mindbodypublicapi.models.update_availability_request import UpdateAvailabilityRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

appointment_controller = client.appointment
version = '6'

site_id = '-99'

update_availability_request = UpdateAvailabilityRequest(
    availability_ids=[
        12,
        13
    ],
    public_display=PublicDisplayEnum.HIDE,
    days_of_week=[
        DaysOfWeekEnum.SUNDAY,
        DaysOfWeekEnum.MONDAY
    ],
    program_ids=[
        40,
        41
    ],
    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

authorization = 'authorization6'

try:
    result = appointment_controller.update_availability(
        version,
        site_id,
        update_availability_request,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

