from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_ebb_component import CreateEBBComponent
from advancedbilling.models.ebb_component import EBBComponent
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

components_controller = client.components
product_family_id = 140

body = CreateEBBComponent(
    event_based_component=EBBComponent(
        name='Component Name',
        unit_name='string',
        pricing_scheme=PricingScheme.PER_UNIT,
        event_based_billing_metric_id=123,
        description='string',
        handle='some_handle',
        taxable=True,
        prices=[
            Price(
                starting_quantity=1,
                unit_price='0.49'
            )
        ]
    )
)

try:
    result = components_controller.create_event_based_component(
        product_family_id,
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

