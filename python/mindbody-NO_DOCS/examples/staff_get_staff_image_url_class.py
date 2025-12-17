from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

staff_controller = client.staff
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_staff_id = 180

try:
    result = staff_controller.get_staff_image_url(
        version,
        site_id,
        authorization=authorization,
        request_staff_id=request_staff_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

