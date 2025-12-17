from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_invoice_payment import CreateInvoicePayment
from advancedbilling.models.create_invoice_payment_request import CreateInvoicePaymentRequest
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType

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

body = CreateInvoicePaymentRequest(
    payment=CreateInvoicePayment(
        amount=124.33,
        memo='for John Smith',
        method=InvoicePaymentMethodType.CHECK,
        details='#0102'
    )
)

try:
    result = invoices_controller.record_payment_for_invoice(
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

