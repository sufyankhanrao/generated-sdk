from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.subscription_group_update_error_response_exception import SubscriptionGroupUpdateErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.update_subscription_group import UpdateSubscriptionGroup
from advancedbilling.models.update_subscription_group_request import UpdateSubscriptionGroupRequest

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
uid = 'uid0'

body = UpdateSubscriptionGroupRequest(
    subscription_group=UpdateSubscriptionGroup(
        member_ids=[
            1,
            2,
            3
        ]
    )
)

try:
    result = subscription_groups_controller.update_subscription_group_members(
        uid,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SubscriptionGroupUpdateErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

