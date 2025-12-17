from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.bank_account_verification import BankAccountVerification
from advancedbilling.models.bank_account_verification_request import BankAccountVerificationRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

payment_profiles_controller = client.payment_profiles
bank_account_id = 252

body = BankAccountVerificationRequest(
    bank_account_verification=BankAccountVerification(
        deposit_1_in_cents=32,
        deposit_2_in_cents=45
    )
)

try:
    result = payment_profiles_controller.verify_bank_account(
        bank_account_id,
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

