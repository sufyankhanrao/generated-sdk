from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_appointment_add_on_request import AddAppointmentAddOnRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

appointment_controller = client.appointment
version = '6'

request = AddAppointmentAddOnRequest(
    apply_payment=False,
    appointment_id=246,
    session_type_id=82,
    staff_id=188,
    test=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = appointment_controller.add_appointment_add_on(
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

