from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.ach_sec_code_3_enum import AchSecCode3Enum
from fortisapi.models.v_1_tokens_cc_request import V1TokensCcRequest

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

tokens_controller = client.tokens
body = V1TokensCcRequest(
    location_id='11e95f8ec39de8fbdb0a4f1a',
    account_holder_name='John Smith',
    account_number='5454545454545454',
    account_vault_api_id='accountvaultabcd',
    token_api_id='tokenabcd',
    accountvault_c_1='accountvault custom 1',
    accountvault_c_2='accountvault custom 2',
    accountvault_c_3='accountvault custom 3',
    token_c_1='token custom 1',
    token_c_2='token custom 2',
    token_c_3='token custom 3',
    ach_sec_code=AchSecCode3Enum.WEB,
    contact_id='11e95f8ec39de8fbdb0a4f1a',
    customer_id='123456',
    previous_account_vault_api_id='previousaccountvault123456',
    previous_token_api_id='previousaccountvault123456',
    previous_account_vault_id='11e95f8ec39de8fbdb0a4f1a',
    previous_token_id='11e95f8ec39de8fbdb0a4f1a',
    previous_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    terms_agree=True,
    terms_agree_ip='192.168.0.10',
    title='Test CC Account',
    exp_date='0929',
    e_serial_number='1234567890',
    e_track_data='%B5454545454545454^account holder^17041010001111A123456789012?250112000000153000000?;5454545454545454=25011011000012345678?00|DC7AB845EFA793FB3C89C5D347D36ED11CAAED0C33E150437893996BA75EB8A0F334D0DAA1B874B6C677A4EF6984B089F891D8E434ACD867B616F4D815E63DA6A86B2AF927E9919B0CFC1DA3FD276D9382672EF8AA256329|32EA4D785CA3398882AABC405017EF9C2BDA666FA007A76538DE10878601EEC36EFE1F185BB8B1C8',
    e_format='ksn',
    e_keyed_data='236D530E098D48DB3F1AA367882CC1A7D475EFCACEFF1E965F17EC1E2D42CBF611C9EB0F80F4255784BA06951BD6092AB6CD3369D3D7E022E74DDCB16F9C40599FA03355E37E6ABB06B717B207709ED8C6BC5C7B6E32BB2B2F5046551A1C88D6',
    run_avs=False,
    track_data='%B5424181111112228^FDCS TEST CARD /MASTERCARD^18121010001111123456789012?;5424181111112228=1812101100000123456?',
    ticket='12345678'
)

try:
    result = tokens_controller.create_a_new_credit_card_token(body)

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

