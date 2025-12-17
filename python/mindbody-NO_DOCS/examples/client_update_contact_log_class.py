
from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_contact_log_request import UpdateContactLogRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = UpdateContactLogRequest(
    id=178,
    test=False,
    assigned_to_staff_id=202,
    text='Text8',
    contact_name='ContactName6'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.update_contact_log(
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

