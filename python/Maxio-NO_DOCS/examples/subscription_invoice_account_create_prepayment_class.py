from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_prepayment import CreatePrepayment
from advancedbilling.models.create_prepayment_method import CreatePrepaymentMethod
from advancedbilling.models.create_prepayment_request import CreatePrepaymentRequest

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

body = CreatePrepaymentRequest(
    prepayment=CreatePrepayment(
        amount=100,
        details='John Doe signup for $100',
        memo='Signup for $100',
        method=CreatePrepaymentMethod.CHECK
    )
)

try:
    result = subscription_invoice_account_controller.create_prepayment(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

