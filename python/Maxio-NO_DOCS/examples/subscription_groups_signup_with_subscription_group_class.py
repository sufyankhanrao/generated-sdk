from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.subscription_group_signup_error_response_exception import SubscriptionGroupSignupErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.subscription_group_signup import SubscriptionGroupSignup
from advancedbilling.models.subscription_group_signup_item import SubscriptionGroupSignupItem
from advancedbilling.models.subscription_group_signup_request import SubscriptionGroupSignupRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_groups_controller = client.subscription_groups
body = SubscriptionGroupSignupRequest(
    subscription_group=SubscriptionGroupSignup(
        subscriptions=[
            SubscriptionGroupSignupItem(
                product_id=11,
                primary=True
            ),
            SubscriptionGroupSignupItem(
                product_id=12
            ),
            SubscriptionGroupSignupItem(
                product_id=13
            )
        ],
        payment_profile_id=123,
        payer_id=123
    )
)

try:
    result = subscription_groups_controller.signup_with_subscription_group(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SubscriptionGroupSignupErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

