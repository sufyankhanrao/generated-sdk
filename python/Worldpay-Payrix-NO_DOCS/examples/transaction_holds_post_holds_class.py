from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.hold_source_enum import HoldSourceEnum
from payrix.models.holds_post_request import HoldsPostRequest
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.release_action_enum import ReleaseActionEnum
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

transaction_holds_controller = client.transaction_holds
body = HoldsPostRequest(
    login='t1_hld_0000fc11df8e4c00000e00c',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    verification_ref='t1_xyz_12345eb00f0cf1bfc00be0f',
    released='2025-01-31 08:42:16',
    reviewed='2025-01-31 08:42:16',
    release_action=ReleaseActionEnum.CANCELLED,
    hold_source=HoldSourceEnum.API_DECISION,
    hold_source_id='5a9bba34-38eb-489e-abd8-765e18562a08',
    delayed_funding_start_date='2025-01-31 08:42:16',
    delayed_funding_end_date='2025-01-31 08:42:16',
    analyst='name',
    claimed='2025-01-31 08:42:16'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = transaction_holds_controller.post_holds(
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

