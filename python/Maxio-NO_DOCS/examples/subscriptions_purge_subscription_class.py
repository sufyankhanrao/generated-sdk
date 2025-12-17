from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.subscription_purge_type import SubscriptionPurgeType

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

ack = 252

cascade = [
    SubscriptionPurgeType.CUSTOMER,
    SubscriptionPurgeType.PAYMENT_PROFILE
]

try:
    result = subscriptions_controller.purge_subscription(
        subscription_id,
        ack,
        cascade=cascade
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

