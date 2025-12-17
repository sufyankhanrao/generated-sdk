import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_appointment_request import UpdateAppointmentRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

appointment_controller = client.appointment
version = '6'

request = UpdateAppointmentRequest(
    appointment_id=246,
    end_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    execute='Execute2',
    gender_preference='GenderPreference6',
    notes='Notes8',
    partner_external_id='PartnerExternalId0'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = appointment_controller.update_appointment(
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

