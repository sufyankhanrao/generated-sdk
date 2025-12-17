from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.renewal_preview_component import RenewalPreviewComponent
from advancedbilling.models.renewal_preview_request import RenewalPreviewRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_status_controller = client.subscription_status
subscription_id = 222

body = RenewalPreviewRequest(
    components=[
        RenewalPreviewComponent(
            component_id=10708,
            quantity=10000
        ),
        RenewalPreviewComponent(
            component_id='handle:small-instance-hours',
            quantity=10000,
            price_point_id=8712
        ),
        RenewalPreviewComponent(
            component_id='handle:large-instance-hours',
            quantity=100,
            price_point_id='handle:startup-pricing'
        )
    ]
)

try:
    result = subscription_status_controller.preview_renewal(
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

