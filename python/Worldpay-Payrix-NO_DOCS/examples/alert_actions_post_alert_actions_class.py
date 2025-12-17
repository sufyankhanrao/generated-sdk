from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.alert_action_type_enum import AlertActionTypeEnum
from payrix.models.alert_actions_post_request import AlertActionsPostRequest
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.max_attempts_temp_disabled_enum import MaxAttemptsTempDisabledEnum
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

alert_actions_controller = client.alert_actions
body = AlertActionsPostRequest(
    alert='t1_alt_65fddb118236188e055d54c',
    mtype=AlertActionTypeEnum.WEB,
    options='JSON',
    value='https://test.payrix.com/apix/test/t1',
    max_attempts_temp_disabled=MaxAttemptsTempDisabledEnum.NOTTEMPORARILYDISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    header_name='Authorization',
    header_value='SecretToken123!',
    retries=3
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = alert_actions_controller.post_alert_actions(
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

