from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.entity_reserves_post_request import EntityReservesPostRequest
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

entity_reserves_controller = client.entity_reserves
body = EntityReservesPostRequest(
    login='t1_log_5f2d5e3e67a6fb5b3521361',
    fund='t1_fun_5f20126254c14a171b8d2d0',
    total=0,
    name='EntityReserve1',
    description='EntityReserve'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = entity_reserves_controller.post_entity_reserves(
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

