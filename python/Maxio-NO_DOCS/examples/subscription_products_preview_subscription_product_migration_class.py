
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.subscription_migration_preview_options import SubscriptionMigrationPreviewOptions
from advancedbilling.models.subscription_migration_preview_request import SubscriptionMigrationPreviewRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_products_controller = client.subscription_products
subscription_id = 222

body = SubscriptionMigrationPreviewRequest(
    migration=SubscriptionMigrationPreviewOptions(
        include_trial=False,
        include_initial_charge=False,
        include_coupons=True,
        preserve_period=False
    )
)

try:
    result = subscription_products_controller.preview_subscription_product_migration(
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

