from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.messages_post_request import MessagesPostRequest
from payrix.models.messages_read_enum import MessagesReadEnum
from payrix.models.secure_enum import SecureEnum
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

messages_controller = client.messages
body = MessagesPostRequest(
    message_thread='t1_mtd_10ca1fcf172a9ac47656a21',
    secure=SecureEnum.DISPLAYED,
    read=MessagesReadEnum.UNREAD,
    message='This is a test message'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = messages_controller.post_messages(
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

