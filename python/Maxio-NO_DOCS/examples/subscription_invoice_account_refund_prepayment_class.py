from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.refund_prepayment_base_errors_response_exception import RefundPrepaymentBaseErrorsResponseException
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

subscription_invoice_account_controller = client.subscription_invoice_account
subscription_id = 222

prepayment_id = 228

try:
    result = subscription_invoice_account_controller.refund_prepayment(
        subscription_id,
        prepayment_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except RefundPrepaymentBaseErrorsResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

