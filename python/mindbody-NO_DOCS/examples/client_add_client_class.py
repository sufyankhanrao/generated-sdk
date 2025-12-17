
from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.action_1_enum import Action1Enum
from mindbodypublicapi.models.add_client_request import AddClientRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = AddClientRequest(
    first_name='FirstName8',
    last_name='LastName8',
    account_balance=60.74,
    action=Action1Enum.ADDED,
    active=False,
    address_line_1='AddressLine12',
    address_line_2='AddressLine26'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.add_client(
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

