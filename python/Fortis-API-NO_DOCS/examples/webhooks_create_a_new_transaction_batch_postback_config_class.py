from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.format_enum import FormatEnum
from fortisapi.models.resource_12_enum import Resource12Enum
from fortisapi.models.v_1_webhooks_batch_request import V1WebhooksBatchRequest

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

webhooks_controller = client.webhooks
body = V1WebhooksBatchRequest(
    is_active=True,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    on_create=True,
    on_update=True,
    on_delete=True,
    product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    number_of_attempts=1,
    url='https://127.0.0.1/receiver',
    attempt_interval=300,
    basic_auth_username='tester',
    basic_auth_password='Test@522',
    expands='changelogs,tags',
    format=FormatEnum.APIDEFAULT,
    postback_config_id='11e95f8ec39de8fbdb0a4f1a',
    resource=Resource12Enum.CONTACT
)

try:
    result = webhooks_controller.create_a_new_transaction_batch_postback_config(body)

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

