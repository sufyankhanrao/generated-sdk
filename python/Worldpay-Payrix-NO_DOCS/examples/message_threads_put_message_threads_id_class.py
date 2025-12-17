from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.message_threads_put_request import MessageThreadsPutRequest
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

message_threads_controller = client.message_threads
id = 't1_mtd_67ef5bad402b6b61e701e0z'

body = MessageThreadsPutRequest(
    login='t1_mtd_67ef5bad402b6b61e701e0z',
    forlogin='t1_log_61e9b7302360fbf12999d63',
    hold='t1_hld_67ef5bad3be038935902204',
    entity_return='entityReturn',
    opposing_message_thread='t1_mtd_67ef5bad40f7e68822ac0c7',
    folder='default',
    sender='testnewmerchant',
    recipient='testnewmerchant1',
    subject='Transaction was put on hold'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = message_threads_controller.put_message_threads_id(
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

