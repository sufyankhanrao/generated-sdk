from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.method_enum import MethodEnum
from payrix.models.token_payment_param import TokenPaymentParam
from payrix.models.token_put_request import TokenPutRequest
from payrix.models.token_status_enum import TokenStatusEnum
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

tokens_controller = client.tokens
id = 'p1_tok_00c82eb304b0067620c82be'

body = TokenPutRequest(
    customer='t1_cus_00c82eb304b0067620c7',
    payment=TokenPaymentParam(
        method=MethodEnum.AMEX,
        number='378734493671000',
        routing='code'
    ),
    status=TokenStatusEnum.PENDING,
    token='11c6a6d85f0a20c31e4c49e461066850',
    expiration='0123',
    name='test1',
    description='test Token',
    custom='Custom Token Processor 1',
    auth_token_customer='authToken',
    origin=2,
    entry_mode=2,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

try:
    result = tokens_controller.put_tokens_id(
        id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorFourHundredException as e: 
    print(e)
except APIException as e: 
    print(e)

