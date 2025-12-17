from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.subscription_component_allocation_error_exception import SubscriptionComponentAllocationErrorException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.credit_scheme import CreditScheme
from advancedbilling.models.credit_scheme_request import CreditSchemeRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_components_controller = client.subscription_components
subscription_id = 222

component_id = 222

allocation_id = 24

body = CreditSchemeRequest(
    credit_scheme=CreditScheme.NONE
)

try:
    result = subscription_components_controller.delete_prepaid_usage_allocation(
        subscription_id,
        component_id,
        allocation_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SubscriptionComponentAllocationErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

