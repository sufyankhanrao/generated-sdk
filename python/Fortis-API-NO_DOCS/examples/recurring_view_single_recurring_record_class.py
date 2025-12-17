from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials

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

recurring_controller = client.recurring
recurring_id = '11e95f8ec39de8fbdb0a4f1a'

try:
    result = recurring_controller.view_single_recurring_record(recurring_id)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except Response401tokenException as e: 
    print(e)
except APIException as e: 
    print(e)

