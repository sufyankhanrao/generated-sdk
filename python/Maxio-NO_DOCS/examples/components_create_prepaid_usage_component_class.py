from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_prepaid_component import CreatePrepaidComponent
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.overage_pricing import OveragePricing
from advancedbilling.models.prepaid_usage_component import PrepaidUsageComponent
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

body = CreatePrepaidComponent(
    prepaid_usage_component=PrepaidUsageComponent(
        name='Minutes',
        unit_name='minutes',
        pricing_scheme=PricingScheme.PER_UNIT,
        unit_price=2,
        overage_pricing=OveragePricing(
            pricing_scheme=PricingScheme.STAIRSTEP,
            prices=[
                Price(
                    starting_quantity=1,
                    unit_price=3,
                    ending_quantity=100
                ),
                Price(
                    starting_quantity=101,
                    unit_price=5
                )
            ]
        ),
        rollover_prepaid_remainder=True,
        renew_prepaid_allocation=True,
        expiration_interval=15,
        expiration_interval_unit=IntervalUnit.DAY
    )
)

try:
    result = components_controller.create_prepaid_usage_component(
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

