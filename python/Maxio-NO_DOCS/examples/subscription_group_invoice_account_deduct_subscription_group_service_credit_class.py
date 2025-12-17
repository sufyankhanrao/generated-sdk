from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
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

subscription_group_invoice_account_controller = client.subscription_group_invoice_account
uid = 'uid0'

body = DeductServiceCreditRequest(
    deduction=DeductServiceCredit(
        amount=10,
        memo='Deduct from group account'
    )
)

try:
    result = subscription_group_invoice_account_controller.deduct_subscription_group_service_credit(
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

