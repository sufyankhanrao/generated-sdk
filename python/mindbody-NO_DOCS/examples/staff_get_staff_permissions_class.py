from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

staff_controller = client.staff
version = '6'

request_staff_id = 180

site_id = '-99'

authorization = 'authorization6'

try:
    result = staff_controller.get_staff_permissions(
        version,
        request_staff_id,
        site_id,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

