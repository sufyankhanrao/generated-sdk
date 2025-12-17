from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.upsert_prepaid_configuration import UpsertPrepaidConfiguration
from advancedbilling.models.upsert_prepaid_configuration_request import UpsertPrepaidConfigurationRequest

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

body = UpsertPrepaidConfigurationRequest(
    prepaid_configuration=UpsertPrepaidConfiguration(
        initial_funding_amount_in_cents=50000,
        replenish_to_amount_in_cents=50000,
        auto_replenish=True,
        replenish_threshold_amount_in_cents=10000
    )
)

try:
    result = subscriptions_controller.update_prepaid_subscription_configuration(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

