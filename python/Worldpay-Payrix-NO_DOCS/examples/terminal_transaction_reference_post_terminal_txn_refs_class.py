from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.platform_1_enum import Platform1Enum
from payrix.models.terminal_txn_ref_post_request import TerminalTxnRefPostRequest
from payrix.models.terminal_txn_ref_stage_enum import TerminalTxnRefStageEnum
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

terminal_transaction_reference_controller = client.terminal_transaction_reference
body = TerminalTxnRefPostRequest(
    terminal_txn='t1_ttx_6806cde42b47ee61cdf6ab9',
    ref='MCC000012',
    stage=TerminalTxnRefStageEnum.AUTHORIZATION,
    platform=Platform1Enum.VCORE
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = terminal_transaction_reference_controller.post_terminal_txn_refs(
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

