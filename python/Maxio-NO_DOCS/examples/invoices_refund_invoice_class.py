from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.refund_invoice import RefundInvoice
from advancedbilling.models.refund_invoice_request import RefundInvoiceRequest

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
uid = 'uid0'

body = RefundInvoiceRequest(
    refund=RefundInvoice(
        amount='100.00',
        memo='Refund for Basic Plan renewal',
        payment_id=12345,
        external=False,
        apply_credit=False,
        void_invoice=True
    )
)

try:
    result = invoices_controller.refund_invoice(
        uid,
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

