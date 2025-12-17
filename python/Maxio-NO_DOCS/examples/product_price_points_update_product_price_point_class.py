from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.update_product_price_point import UpdateProductPricePoint
from advancedbilling.models.update_product_price_point_request import UpdateProductPricePointRequest

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
product_id = 124

price_point_id = 188

body = UpdateProductPricePointRequest(
    price_point=UpdateProductPricePoint(
        handle='educational',
        price_in_cents=1250
    )
)

try:
    result = product_price_points_controller.update_product_price_point(
        product_id,
        price_point_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

