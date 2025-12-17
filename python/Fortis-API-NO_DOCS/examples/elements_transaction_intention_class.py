from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.ach_sec_code_enum import AchSecCodeEnum
from fortisapi.models.action_enum import ActionEnum
from fortisapi.models.v_1_elements_transaction_intention_request import V1ElementsTransactionIntentionRequest

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

elements_controller = client.elements
body = V1ElementsTransactionIntentionRequest(
    action=ActionEnum.SALE,
    digital_wallets_only=False,
    amount=1099,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    contact_id='11e95f8ec39de8fbdb0a4f1a',
    ach_sec_code=AchSecCodeEnum.WEB
)

try:
    result = elements_controller.transaction_intention(body)

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

