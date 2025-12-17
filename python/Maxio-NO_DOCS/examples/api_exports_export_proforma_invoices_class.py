from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.single_error_response_exception import SingleErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

api_exports_controller = client.api_exports
try:
    result = api_exports_controller.export_proforma_invoices()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SingleErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

