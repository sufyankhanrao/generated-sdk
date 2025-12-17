
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.allocate_components import AllocateComponents
from advancedbilling.models.create_allocation import CreateAllocation

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

body = AllocateComponents(
    proration_upgrade_scheme='prorate-attempt-capture',
    proration_downgrade_scheme='no-prorate',
    allocations=[
        CreateAllocation(
            quantity=10,
            component_id=123,
            memo='foo'
        ),
        CreateAllocation(
            quantity=5,
            component_id=456,
            memo='bar'
        )
    ]
)

try:
    result = subscription_components_controller.allocate_components(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorListResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

