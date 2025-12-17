from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.single_string_error_response_exception import SingleStringErrorResponseException
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

coupons_controller = client.coupons
code = 'code8'

try:
    result = coupons_controller.validate_coupon(code)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SingleStringErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

