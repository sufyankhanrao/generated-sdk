from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_payment import CreatePayment
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType
from advancedbilling.models.record_payment_request import RecordPaymentRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

invoices_controller = client.invoices
subscription_id = 222

body = RecordPaymentRequest(
    payment=CreatePayment(
        amount='10.0',
        memo='to pay the bills',
        payment_details='check number 8675309',
        payment_method=InvoicePaymentMethodType.CHECK
    )
)

try:
    result = invoices_controller.record_payment_for_subscription(
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

