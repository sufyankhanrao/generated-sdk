import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_appointment_request import AddAppointmentRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

appointment_controller = client.appointment
version = '6'

request = AddAppointmentRequest(
    client_id='ClientId0',
    location_id=238,
    session_type_id=82,
    staff_id=188,
    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    apply_payment=False,
    duration=224,
    execute='Execute2',
    end_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    gender_preference='GenderPreference6'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = appointment_controller.add_appointment(
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

