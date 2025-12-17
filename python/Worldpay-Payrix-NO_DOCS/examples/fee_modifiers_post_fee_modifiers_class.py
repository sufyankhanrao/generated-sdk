from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.fee_modifiers_post_request import FeeModifiersPostRequest
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.markup_um_enum import MarkupUmEnum
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

fee_modifiers_controller = client.fee_modifiers
body = FeeModifiersPostRequest(
    fee='t1_fee_6809dd0aa16f89a3f28ca98',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    entity='t1_ent_00c2b1a6102ffdd33f00000',
    org='t1_org_00b2ac11ed8bed97fb80000',
    fromentity='t1_ent_0088c831a31ca8841c80000',
    markup_um=MarkupUmEnum.FIXEDAMOUNT,
    markup_amount=0
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = fee_modifiers_controller.post_fee_modifiers(
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

