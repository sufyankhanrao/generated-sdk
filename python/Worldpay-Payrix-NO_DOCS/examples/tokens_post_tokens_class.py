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
from payrix.models.token_post_request import TokenPostRequest
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
body = TokenPostRequest(
    customer='t1_cus_00c82eb304b0067620c7',
    payment=TokenPaymentParam(
        method=MethodEnum.AMEX,
        number='378734493671000',
        routing='code'
    ),
    status=TokenStatusEnum.PENDING,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    expiration='0123',
    name='test',
    description='test Token',
    custom='Custom Token Processor 2',
    auth_token_customer='authToken',
    origin=2,
    entry_mode=2,
    omnitoken='123'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = tokens_controller.post_tokens(
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

