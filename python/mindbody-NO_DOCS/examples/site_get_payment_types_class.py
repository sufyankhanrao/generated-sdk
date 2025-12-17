from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

site_controller = client.site
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active = False

try:
    result = site_controller.get_payment_types(
        version,
        site_id,
        authorization=authorization,
        request_active=request_active
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

