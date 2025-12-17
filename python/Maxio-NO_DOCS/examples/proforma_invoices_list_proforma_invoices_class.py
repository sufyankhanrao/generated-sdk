from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.direction import Direction

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
collect = {
    'subscription_id': 222,
    'page': 2,
    'per_page': 50,
    'direction': Direction.DESC,
    'line_items': False,
    'discounts': False,
    'taxes': False,
    'credits': False,
    'payments': False,
    'custom_fields': False
}
try:
    result = proforma_invoices_controller.list_proforma_invoices(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

