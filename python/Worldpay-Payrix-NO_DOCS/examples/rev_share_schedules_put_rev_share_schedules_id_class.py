from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.rev_share_schedule_event_enum import RevShareScheduleEventEnum
from payrix.models.rev_share_schedules_put_request import RevShareSchedulesPutRequest
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

rev_share_schedules_controller = client.rev_share_schedules
id = 't1_rsc_6800f8590a3fc6c0caed9zz'

body = RevShareSchedulesPutRequest(
    entity='t1_ent_5f9058fe8c8d21ead8f68dc',
    forentity='t1_ent_67c96d183e9b9aa6c6f190c',
    start='2025-04-17 18:17:20',
    end='2025-04-17 18:17:20',
    share=2000,
    event=RevShareScheduleEventEnum.REVSHARECARD,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = rev_share_schedules_controller.put_rev_share_schedules_id(
        id,
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

