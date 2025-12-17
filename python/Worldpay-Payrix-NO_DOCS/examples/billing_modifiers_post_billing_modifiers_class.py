from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.billing_modifiers_post_request import BillingModifiersPostRequest
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
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

billing_modifiers_controller = client.billing_modifiers
body = BillingModifiersPostRequest(
    billing='t1_bil_67d9c8a7df33cf77a3e5e4a',
    fromentity='t1_ent_67d851660b5836731a89ee3',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    entity='t1_ent_5cd987a735c33bab09e7570',
    org='t1_org_67d9c6a866e5d47dca276c3',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414970z0'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = billing_modifiers_controller.post_billing_modifiers(
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

