from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.update_card_request import UpdateCardRequest
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

card_id = 'card_id4'

request = UpdateCardRequest(
    holder_name='holder_name2',
    exp_month=10,
    exp_year=30,
    billing_address=CreateAddressRequest(
        street='street8',
        number='number4',
        zip_code='zip_code2',
        neighborhood='neighborhood4',
        city='city2',
        state='state6',
        country='country2',
        complement='complement6',
        line_1='line_18',
        line_2='line_26'
    ),
    metadata={
        'key0': 'metadata3'
    },
    label='label6'
)

try:
    result = customers_controller.update_card(
        customer_id,
        card_id,
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

