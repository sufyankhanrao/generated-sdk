from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_discount_request import CreateDiscountRequest
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest
from pagarmeapisdk.models.create_subscription_item_request import CreateSubscriptionItemRequest
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
subscription_id = 'subscription_id0'

request = CreateSubscriptionItemRequest(
    description='description6',
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type='scheme_type8'
    ),
    id='id6',
    plan_item_id='plan_item_id6',
    discounts=[
        CreateDiscountRequest(
            value=90.66,
            discount_type='discount_type2',
            item_id='item_id4'
        )
    ],
    name='name6'
)

try:
    result = subscriptions_controller.create_subscription_item(
        subscription_id,
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

