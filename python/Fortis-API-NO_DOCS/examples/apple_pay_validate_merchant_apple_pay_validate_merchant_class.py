from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.v_1_wallet_provider_apple_pay_validate_merchant_request import V1WalletProviderApplePayValidateMerchantRequest

client = FortisapiClient(
    user_id_credentials=UserIdCredentials(
        user_id='user-id'
    ),
    user_api_key_credentials=UserApiKeyCredentials(
        user_api_key='user-api-key'
    ),
    developer_id_credentials=DeveloperIdCredentials(
        developer_id='developer-id'
    ),
    environment=Environment.SANDBOX
)

apple_pay_validate_merchant_controller = client.apple_pay_validate_merchant
body = V1WalletProviderApplePayValidateMerchantRequest(
    url='https://apple-pay-gateway-cert.apple.com/paymentservices/startSession',
    merchant_id='abc1234',
    domain_name='website.domain.com',
    display_name='Sandwich Market'
)

try:
    result = apple_pay_validate_merchant_controller.apple_pay_validate_merchant(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except Response401tokenException as e: 
    print(e)
except Response412Exception as e: 
    print(e)
except APIException as e: 
    print(e)

