
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException
from advancedbilling.exceptions.proforma_bad_request_error_response_exception import ProformaBadRequestErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_subscription import CreateSubscription
from advancedbilling.models.create_subscription_request import CreateSubscriptionRequest
from advancedbilling.models.customer_attributes import CustomerAttributes

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

proforma_invoices_controller = client.proforma_invoices
body = CreateSubscriptionRequest(
    subscription=CreateSubscription(
        product_handle='gold-plan',
        customer_attributes=CustomerAttributes(
            first_name='first',
            last_name='last',
            email='flast@example.com'
        )
    )
)

try:
    result = proforma_invoices_controller.preview_signup_proforma_invoice(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ProformaBadRequestErrorResponseException as e: 
    print(e)
except ErrorArrayMapResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

