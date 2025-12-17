from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_component_price_point import CreateComponentPricePoint
from advancedbilling.models.create_component_price_points_request import CreateComponentPricePointsRequest
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
component_id = 'component_id8'

body = CreateComponentPricePointsRequest(
    price_points=[
        CreateComponentPricePoint(
            name='Wholesale',
            pricing_scheme=PricingScheme.PER_UNIT,
            prices=[
                Price(
                    starting_quantity=1,
                    unit_price=5
                )
            ],
            handle='wholesale'
        ),
        CreateComponentPricePoint(
            name='MSRP',
            pricing_scheme=PricingScheme.PER_UNIT,
            prices=[
                Price(
                    starting_quantity=1,
                    unit_price=4
                )
            ],
            handle='msrp'
        ),
        CreateComponentPricePoint(
            name='Special Pricing',
            pricing_scheme=PricingScheme.PER_UNIT,
            prices=[
                Price(
                    starting_quantity=1,
                    unit_price=5
                )
            ],
            handle='special'
        )
    ]
)

try:
    result = components_controller.bulk_create_component_price_points(
        component_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

