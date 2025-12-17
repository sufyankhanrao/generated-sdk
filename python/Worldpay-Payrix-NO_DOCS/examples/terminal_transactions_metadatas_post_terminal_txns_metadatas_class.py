from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.field_enum import FieldEnum
from payrix.models.terminal_txn_metadata_type_enum import TerminalTxnMetadataTypeEnum
from payrix.models.terminal_txns_metadatas_post_request import TerminalTxnsMetadatasPostRequest
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

terminal_transactions_metadatas_controller = client.terminal_transactions_metadatas
body = TerminalTxnsMetadatasPostRequest(
    terminal_txn='t1_ttx_6806cde42b47ee61cdf6ab9',
    mtype=TerminalTxnMetadataTypeEnum.DISCRETIONARY,
    field=FieldEnum.DISCRETIONARY1,
    value='0421'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = terminal_transactions_metadatas_controller.post_terminal_txns_metadatas(
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

