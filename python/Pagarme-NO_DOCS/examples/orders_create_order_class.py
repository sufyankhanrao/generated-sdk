
from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_customer_request import CreateCustomerRequest
from pagarmeapisdk.models.create_order_item_request import CreateOrderItemRequest
from pagarmeapisdk.models.create_order_request import CreateOrderRequest
from pagarmeapisdk.models.create_payment_request import CreatePaymentRequest
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

orders_controller = client.orders
body = CreateOrderRequest(
    items=[
        CreateOrderItemRequest(
            amount=164,
            description='description2',
            quantity=22,
            category='category6'
        )
    ],
    customer=CreateCustomerRequest(
        name='Tony Stark',
        email='email6',
        document='document6',
        mtype='type0',
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
        code='code8'
    ),
    payments=[
        CreatePaymentRequest(
            payment_method='payment_method8'
        )
    ],
    code='code4',
    closed=True
)

try:
    result = orders_controller.create_order(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

