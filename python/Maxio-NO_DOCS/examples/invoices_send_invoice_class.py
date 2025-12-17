from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.send_invoice_request import SendInvoiceRequest

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

body = SendInvoiceRequest(
    recipient_emails=[
        'user0@example.com'
    ],
    cc_recipient_emails=[
        'user1@example.com'
    ],
    bcc_recipient_emails=[
        'user2@example.com'
    ]
)

try:
    result = invoices_controller.send_invoice(
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

