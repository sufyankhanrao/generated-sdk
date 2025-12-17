import dateutil.parser

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.component_allocation_error_exception import ComponentAllocationErrorException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_allocation import CreateAllocation
from advancedbilling.models.preview_allocations_request import PreviewAllocationsRequest

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

body = PreviewAllocationsRequest(
    allocations=[
        CreateAllocation(
            quantity=10,
            component_id=554108,
            memo='NOW',
            proration_downgrade_scheme='prorate',
            proration_upgrade_scheme='prorate-attempt-capture',
            price_point_id=325826
        )
    ],
    effective_proration_date=dateutil.parser.parse('2023-11-01').date()
)

try:
    result = subscription_components_controller.preview_allocations(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ComponentAllocationErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

