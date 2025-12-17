from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_or_update_endpoint import CreateOrUpdateEndpoint
from advancedbilling.models.create_or_update_endpoint_request import CreateOrUpdateEndpointRequest
from advancedbilling.models.webhook_subscription import WebhookSubscription

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

webhooks_controller = client.webhooks
endpoint_id = 42

body = CreateOrUpdateEndpointRequest(
    endpoint=CreateOrUpdateEndpoint(
        url='https://yout.site/webhooks/1/json.',
        webhook_subscriptions=[
            WebhookSubscription.PAYMENT_FAILURE,
            WebhookSubscription.PAYMENT_SUCCESS,
            WebhookSubscription.REFUND_FAILURE
        ]
    )
)

try:
    result = webhooks_controller.update_endpoint(
        endpoint_id,
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

