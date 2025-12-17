from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.direction import Direction
from advancedbilling.models.invoice_date_field import InvoiceDateField
from advancedbilling.models.invoice_sort_field import InvoiceSortField

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
collect = {
    'page': 2,
    'per_page': 50,
    'direction': Direction.DESC,
    'line_items': False,
    'discounts': False,
    'taxes': False,
    'credits': False,
    'payments': False,
    'custom_fields': False,
    'refunds': False,
    'date_field': InvoiceDateField.ISSUE_DATE,
    'customer_ids': [
        1,
        2,
        3
    ],
    'number': [
        '1234',
        '1235'
    ],
    'product_ids': [
        23,
        34
    ],
    'sort': InvoiceSortField.TOTAL_AMOUNT
}
try:
    result = invoices_controller.list_invoices(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

