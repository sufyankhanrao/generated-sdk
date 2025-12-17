from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_customer_request import CreateCustomerRequest
from pagarmeapisdk.models.create_phones_request import CreatePhonesRequest
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
request = CreateCustomerRequest(
    name='Tony Stark',
    email='email0',
    document='document0',
    mtype='type4',
    address=CreateAddressRequest(
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
    ),
    metadata={
        'key0': 'metadata3'
    },
    phones=CreatePhonesRequest(),
    code='code4'
)

try:
    result = customers_controller.create_customer(request)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

