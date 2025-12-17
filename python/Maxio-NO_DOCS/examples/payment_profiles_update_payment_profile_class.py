from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_string_map_response_exception import ErrorStringMapResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.card_type import CardType
from advancedbilling.models.current_vault import CurrentVault
from advancedbilling.models.update_payment_profile import UpdatePaymentProfile
from advancedbilling.models.update_payment_profile_request import UpdatePaymentProfileRequest

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
payment_profile_id = 198

body = UpdatePaymentProfileRequest(
    payment_profile=UpdatePaymentProfile(
        first_name='Graham',
        last_name='Test',
        full_number='4111111111111111',
        card_type=CardType.MASTER,
        expiration_month='04',
        expiration_year='2030',
        current_vault=CurrentVault.BOGUS,
        billing_address='456 Juniper Court',
        billing_city='Boulder',
        billing_state='CO',
        billing_zip='80302',
        billing_country='US',
        billing_address_2='billing_address_22'
    )
)

try:
    result = payment_profiles_controller.update_payment_profile(
        payment_profile_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorStringMapResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

