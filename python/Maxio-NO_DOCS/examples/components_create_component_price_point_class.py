from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_component_price_point import CreateComponentPricePoint
from advancedbilling.models.create_component_price_point_request import CreateComponentPricePointRequest
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
component_id = 222

body = CreateComponentPricePointRequest(
    price_point=CreateComponentPricePoint(
        name='Wholesale',
        pricing_scheme=PricingScheme.STAIRSTEP,
        prices=[
            Price(
                starting_quantity='1',
                unit_price='5.00',
                ending_quantity='100'
            ),
            Price(
                starting_quantity='101',
                unit_price='4.00',
                ending_quantity=None
            )
        ],
        handle='wholesale-handle',
        use_site_exchange_rate=False
    )
)

try:
    result = components_controller.create_component_price_point(
        component_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

