from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_invoice_payment_application import CreateInvoicePaymentApplication
from advancedbilling.models.create_multi_invoice_payment import CreateMultiInvoicePayment
from advancedbilling.models.create_multi_invoice_payment_request import CreateMultiInvoicePaymentRequest
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
body = CreateMultiInvoicePaymentRequest(
    payment=CreateMultiInvoicePayment(
        amount='100.00',
        applications=[
            CreateInvoicePaymentApplication(
                invoice_uid='inv_8gk5bwkct3gqt',
                amount='50.00'
            ),
            CreateInvoicePaymentApplication(
                invoice_uid='inv_7bc6bwkct3lyt',
                amount='50.00'
            )
        ],
        memo='to pay the bills',
        details='check number 8675309',
        method=InvoicePaymentMethodType.CHECK
    )
)

try:
    result = invoices_controller.record_payment_for_multiple_invoices(
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

