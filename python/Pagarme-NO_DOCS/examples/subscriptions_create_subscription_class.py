
from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_customer_request import CreateCustomerRequest
from pagarmeapisdk.models.create_discount_request import CreateDiscountRequest
from pagarmeapisdk.models.create_increment_request import CreateIncrementRequest
from pagarmeapisdk.models.create_phones_request import CreatePhonesRequest
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest
from pagarmeapisdk.models.create_shipping_request import CreateShippingRequest
from pagarmeapisdk.models.create_subscription_item_request import CreateSubscriptionItemRequest
from pagarmeapisdk.models.create_subscription_request import CreateSubscriptionRequest
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION
)

subscriptions_controller = client.subscriptions
body = CreateSubscriptionRequest(
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
    card=CreateCardRequest(
        mtype='credit'
    ),
    code='code4',
    payment_method='payment_method4',
    billing_type='billing_type0',
    statement_descriptor='statement_descriptor6',
    description='description4',
    currency='currency6',
    interval='interval6',
    interval_count=170,
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type='scheme_type8'
    ),
    items=[
        CreateSubscriptionItemRequest(
            description='description2',
            pricing_scheme=CreatePricingSchemeRequest(
                scheme_type='scheme_type8'
            ),
            id='id8',
            plan_item_id='plan_item_id8',
            discounts=[
                CreateDiscountRequest(
                    value=90.66,
                    discount_type='discount_type2',
                    item_id='item_id4'
                )
            ],
            name='name8'
        )
    ],
    shipping=CreateShippingRequest(
        amount=52,
        description='description6',
        recipient_name='recipient_name2',
        recipient_phone='recipient_phone6',
        address_id='address_id6',
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
        mtype='type6'
    ),
    discounts=[
        CreateDiscountRequest(
            value=90.66,
            discount_type='discount_type2',
            item_id='item_id4'
        )
    ],
    metadata={
        'key0': 'metadata7',
        'key1': 'metadata8'
    },
    increments=[
        CreateIncrementRequest(
            value=252.86,
            increment_type='increment_type6',
            item_id='item_id6'
        )
    ]
)

try:
    result = subscriptions_controller.create_subscription(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

