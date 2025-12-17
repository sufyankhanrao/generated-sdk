from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.subscription_group_create_error_response_exception import SubscriptionGroupCreateErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_subscription_group import CreateSubscriptionGroup
from advancedbilling.models.create_subscription_group_request import CreateSubscriptionGroupRequest

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
body = CreateSubscriptionGroupRequest(
    subscription_group=CreateSubscriptionGroup(
        subscription_id=1,
        member_ids=[
            2,
            3,
            4
        ]
    )
)

try:
    result = subscription_groups_controller.create_subscription_group(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SubscriptionGroupCreateErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

