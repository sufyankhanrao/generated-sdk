from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.ach_sec_code_3_enum import AchSecCode3Enum
from fortisapi.models.v_1_tokens_ticket_request import V1TokensTicketRequest

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
body = V1TokensTicketRequest(
    location_id='11e95f8ec39de8fbdb0a4f1a',
    ticket='12345678',
    account_holder_name='John Smith',
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
    account_number='545454545454545',
    terms_agree=True,
    terms_agree_ip='192.168.0.10',
    title='Test CC Account'
)

try:
    result = tokens_controller.create_a_new_ticket_token(body)

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

