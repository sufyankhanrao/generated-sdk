from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.subscription_include import SubscriptionInclude

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

include = [
    SubscriptionInclude.COUPONS,
    SubscriptionInclude.SELF_SERVICE_PAGE_TOKEN
]

try:
    result = subscriptions_controller.read_subscription(
        subscription_id,
        include=include
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

