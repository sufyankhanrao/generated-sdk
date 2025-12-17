from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_client_direct_debit_info_request import AddClientDirectDebitInfoRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = AddClientDirectDebitInfoRequest(
    test=False,
    client_id='ClientId0',
    name_on_account='NameOnAccount0',
    routing_number='RoutingNumber6',
    account_number='AccountNumber0'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.add_client_direct_debit_info(
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

