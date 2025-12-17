from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

site_id = '-99'

authorization = 'authorization6'

client_id = 'clientId6'

try:
    result = client_controller.get_direct_debit_info(
        version,
        site_id,
        authorization=authorization,
        client_id=client_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

