from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.add_subscription_to_a_group import AddSubscriptionToAGroup
from advancedbilling.models.group_billing import GroupBilling
from advancedbilling.models.group_settings import GroupSettings
from advancedbilling.models.group_target import GroupTarget
from advancedbilling.models.group_target_type import GroupTargetType

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
subscription_id = 222

body = AddSubscriptionToAGroup(
    group=GroupSettings(
        target=GroupTarget(
            mtype=GroupTargetType.SUBSCRIPTION,
            id=32987
        ),
        billing=GroupBilling(
            accrue=True,
            align_date=True,
            prorate=True
        )
    )
)

try:
    result = subscription_groups_controller.add_subscription_to_group(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

