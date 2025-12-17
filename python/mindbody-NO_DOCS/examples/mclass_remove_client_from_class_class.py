from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.remove_client_from_class_request import RemoveClientFromClassRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

request = RemoveClientFromClassRequest(
    client_id='ClientId0',
    class_id=90,
    test=False,
    send_email=False,
    late_cancel=False,
    visit_id=92
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = mclass_controller.remove_client_from_class(
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

