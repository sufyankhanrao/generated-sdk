from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.secret_locked_enum import SecretLockedEnum
from payrix.models.secret_type_enum import SecretTypeEnum
from payrix.models.secrets_platform_enum import SecretsPlatformEnum
from payrix.models.secrets_post_request import SecretsPostRequest
from payrix.payrix_client import PayrixClient

client = PayrixClient(
    api_key_credentials=ApiKeyCredentials(
        apikey='APIKEY'
    ),
    session_key_credentials=SessionKeyCredentials(
        sessionkey='SESSIONKEY'
    ),
    txn_session_key_credentials=TxnSessionKeyCredentials(
        txnsessionkey='TXNSESSIONKEY'
    ),
    environment=Environment.QA
)

secrets_controller = client.secrets
body = SecretsPostRequest(
    login='t1_log_63d2cddf694099bfb64e976',
    mtype=SecretTypeEnum.PRIVATEKEY,
    key='529c5b7ac1d02079fc162a4fe3e32a020057f4b3d7b6225eb55bf8ec65257283',
    locked=SecretLockedEnum.NOTLOCKED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    entity='g157715bca1f00z',
    org='t1_org_5fada4629c317f80bc9cb12',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='g157713aff9b946',
    platform=SecretsPlatformEnum.APPLE,
    name='Test1',
    description='description1'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = secrets_controller.post_secrets(
        body,
        request_token=request_token
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorFourHundredException as e: 
    print(e)
except APIException as e: 
    print(e)

