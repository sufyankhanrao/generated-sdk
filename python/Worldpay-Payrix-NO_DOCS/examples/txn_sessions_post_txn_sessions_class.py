from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.txn_sessions_configurations import TxnSessionsConfigurations
from payrix.models.txn_sessions_post_request import TxnSessionsPostRequest
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

txn_sessions_controller = client.txn_sessions
body = TxnSessionsPostRequest(
    login='t1_log_65a6bb6506be50d9406eb00',
    merchant='t1_mer_66312e43815957c6767000z',
    configurations=TxnSessionsConfigurations(
        duration=8,
        max_times_approved=2,
        max_times_use=4
    )
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = txn_sessions_controller.post_txn_sessions(
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

