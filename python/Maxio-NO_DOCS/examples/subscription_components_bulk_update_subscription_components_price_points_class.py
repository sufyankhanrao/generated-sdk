from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.component_price_point_error_exception import ComponentPricePointErrorException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.bulk_components_price_point_assignment import BulkComponentsPricePointAssignment
from advancedbilling.models.component_price_point_assignment import ComponentPricePointAssignment

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

body = BulkComponentsPricePointAssignment(
    components=[
        ComponentPricePointAssignment(
            component_id=997,
            price_point=1022
        ),
        ComponentPricePointAssignment(
            component_id=998,
            price_point='wholesale-handle'
        ),
        ComponentPricePointAssignment(
            component_id=999,
            price_point='_default'
        )
    ]
)

try:
    result = subscription_components_controller.bulk_update_subscription_components_price_points(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ComponentPricePointErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

