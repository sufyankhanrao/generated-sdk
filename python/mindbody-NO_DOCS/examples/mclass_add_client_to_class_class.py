from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_client_to_class_request import AddClientToClassRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

request = AddClientToClassRequest(
    client_id='ClientId0',
    class_id=90,
    test=False,
    require_payment=False,
    waitlist=False,
    send_email=False,
    waitlist_entry_id=54
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = mclass_controller.add_client_to_class(
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

