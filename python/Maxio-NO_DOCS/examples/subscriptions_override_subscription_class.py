import dateutil.parser

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.single_error_response_exception import SingleErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.override_subscription import OverrideSubscription
from advancedbilling.models.override_subscription_request import OverrideSubscriptionRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscriptions_controller = client.subscriptions
subscription_id = 222

body = OverrideSubscriptionRequest(
    subscription=OverrideSubscription(
        activated_at=dateutil.parser.parse('1999-12-01T10:28:34-05:00'),
        canceled_at=dateutil.parser.parse('2000-12-31T10:28:34-05:00'),
        cancellation_message='Original cancellation in 2000',
        expires_at=dateutil.parser.parse('2001-07-15T10:28:34-05:00')
    )
)

try:
    result = subscriptions_controller.override_subscription(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SingleErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

