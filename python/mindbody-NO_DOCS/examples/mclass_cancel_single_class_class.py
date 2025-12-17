from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.cancel_single_class_request import CancelSingleClassRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

request = CancelSingleClassRequest(
    class_id=30,
    hide_cancel=False,
    send_client_email=False,
    send_staff_email=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = mclass_controller.cancel_single_class(
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

