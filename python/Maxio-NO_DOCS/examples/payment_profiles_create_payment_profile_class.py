from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.bank_account_holder_type import BankAccountHolderType
from advancedbilling.models.bank_account_type import BankAccountType
from advancedbilling.models.create_payment_profile import CreatePaymentProfile
from advancedbilling.models.create_payment_profile_request import CreatePaymentProfileRequest
from advancedbilling.models.payment_type import PaymentType

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
body = CreatePaymentProfileRequest(
    payment_profile=CreatePaymentProfile(
        payment_type=PaymentType.BANK_ACCOUNT,
        customer_id=123,
        bank_name='Best Bank',
        bank_routing_number='021000089',
        bank_account_number='111111111111',
        bank_account_type=BankAccountType.CHECKING,
        bank_account_holder_type=BankAccountHolderType.BUSINESS
    )
)

try:
    result = payment_profiles_controller.create_payment_profile(
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

