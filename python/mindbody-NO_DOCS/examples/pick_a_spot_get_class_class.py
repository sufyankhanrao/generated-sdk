from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

pick_a_spot_controller = client.pick_a_spot
version = '6'

class_id = 'classId0'

site_id = '-99'

authorization = 'authorization6'

try:
    result = pick_a_spot_controller.get_class(
        version,
        class_id,
        site_id,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

