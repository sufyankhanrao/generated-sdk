
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_invoice import CreateInvoice
from advancedbilling.models.create_invoice_item import CreateInvoiceItem
from advancedbilling.models.create_invoice_request import CreateInvoiceRequest

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

body = CreateInvoiceRequest(
    invoice=CreateInvoice(
        line_items=[
            CreateInvoiceItem(
                title='A Product',
                quantity=12,
                unit_price='150.00'
            )
        ]
    )
)

try:
    result = invoices_controller.create_invoice(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorArrayMapResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

