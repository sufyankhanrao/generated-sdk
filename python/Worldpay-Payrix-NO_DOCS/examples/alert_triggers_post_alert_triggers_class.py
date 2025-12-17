from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.alert_trigger_event_enum import AlertTriggerEventEnum
from payrix.models.alert_triggers_post_request import AlertTriggersPostRequest
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.resource_enum import ResourceEnum
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

alert_triggers_controller = client.alert_triggers
body = AlertTriggersPostRequest(
    alert='t1_alt_67d489a72e5e8fdec85a910',
    event=AlertTriggerEventEnum.DELETE,
    resource=ResourceEnum.MERCHANTS,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='name of alertTrigger',
    description='description of alertTrigger'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = alert_triggers_controller.post_alert_triggers(
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

