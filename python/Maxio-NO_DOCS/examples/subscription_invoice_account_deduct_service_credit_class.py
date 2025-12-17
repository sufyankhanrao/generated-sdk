from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.deduct_service_credit import DeductServiceCredit
from advancedbilling.models.deduct_service_credit_request import DeductServiceCreditRequest

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

body = DeductServiceCreditRequest(
    deduction=DeductServiceCredit(
        amount='1',
        memo='Deduction'
    )
)

try:
    result = subscription_invoice_account_controller.deduct_service_credit(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

