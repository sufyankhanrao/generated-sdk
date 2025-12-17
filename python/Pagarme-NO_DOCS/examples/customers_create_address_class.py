from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION
)

customers_controller = client.customers
customer_id = 'customer_id8'

request = CreateAddressRequest(
    street='street6',
    number='number4',
    zip_code='zip_code0',
    neighborhood='neighborhood2',
    city='city6',
    state='state2',
    country='country0',
    complement='complement2',
    line_1='line_10',
    line_2='line_24'
)

try:
    result = customers_controller.create_address(
        customer_id,
        request
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

