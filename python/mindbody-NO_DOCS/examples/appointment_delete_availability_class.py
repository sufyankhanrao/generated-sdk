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

delete_availability_request_availability_id = 186

delete_availability_request_test = False

try:
    result = appointment_controller.delete_availability(
        version,
        site_id,
        authorization=authorization,
        delete_availability_request_availability_id=delete_availability_request_availability_id,
        delete_availability_request_test=delete_availability_request_test
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

