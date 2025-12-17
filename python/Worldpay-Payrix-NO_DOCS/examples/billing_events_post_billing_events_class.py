from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.billing_event_enum import BillingEventEnum
from payrix.models.billing_events_post_request import BillingEventsPostRequest
from payrix.models.deduct_from_balance_enum import DeductFromBalanceEnum
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

billing_events_controller = client.billing_events
body = BillingEventsPostRequest(
    billing='t1_bil_67d9cfac37cb75f7c8e0597',
    event=BillingEventEnum.FEES,
    deduct_from_balance=DeductFromBalanceEnum.DONOTDEDUCT,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    event_schedule='record ID'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = billing_events_controller.post_billing_events(
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

