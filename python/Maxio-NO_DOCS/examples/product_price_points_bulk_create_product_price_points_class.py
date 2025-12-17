from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.bulk_create_product_price_points_request import BulkCreateProductPricePointsRequest
from advancedbilling.models.create_product_price_point import CreateProductPricePoint
from advancedbilling.models.interval_unit import IntervalUnit

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

product_price_points_controller = client.product_price_points
product_id = 202

body = BulkCreateProductPricePointsRequest(
    price_points=[
        CreateProductPricePoint(
            name='Educational',
            price_in_cents=1000,
            interval=1,
            interval_unit=IntervalUnit.MONTH,
            handle='educational',
            trial_price_in_cents=4900,
            trial_interval=1,
            trial_interval_unit=IntervalUnit.MONTH,
            trial_type='payment_expected',
            initial_charge_in_cents=120000,
            initial_charge_after_trial=False,
            expiration_interval=12,
            expiration_interval_unit=IntervalUnit.MONTH
        ),
        CreateProductPricePoint(
            name='More Educational',
            price_in_cents=2000,
            interval=1,
            interval_unit=IntervalUnit.MONTH,
            handle='more-educational',
            trial_price_in_cents=4900,
            trial_interval=1,
            trial_interval_unit=IntervalUnit.MONTH,
            trial_type='payment_expected',
            initial_charge_in_cents=120000,
            initial_charge_after_trial=False,
            expiration_interval=12,
            expiration_interval_unit=IntervalUnit.MONTH
        )
    ]
)

try:
    result = product_price_points_controller.bulk_create_product_price_points(
        product_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

