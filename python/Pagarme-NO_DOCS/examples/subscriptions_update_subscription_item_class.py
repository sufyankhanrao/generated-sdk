from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.update_price_bracket_request import UpdatePriceBracketRequest
from pagarmeapisdk.models.update_pricing_scheme_request import UpdatePricingSchemeRequest
from pagarmeapisdk.models.update_subscription_item_request import UpdateSubscriptionItemRequest
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

item_id = 'item_id0'

body = UpdateSubscriptionItemRequest(
    description='description4',
    status='status2',
    pricing_scheme=UpdatePricingSchemeRequest(
        scheme_type='scheme_type8',
        price_brackets=[
            UpdatePriceBracketRequest(
                start_quantity=144,
                price=174
            )
        ]
    ),
    name='name6'
)

try:
    result = subscriptions_controller.update_subscription_item(
        subscription_id,
        item_id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

