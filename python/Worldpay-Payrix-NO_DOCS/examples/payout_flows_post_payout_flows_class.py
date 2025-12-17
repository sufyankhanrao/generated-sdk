from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.currency_enum import CurrencyEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.payout_flow_schedule_enum import PayoutFlowScheduleEnum
from payrix.models.payout_flow_trigger_enum import PayoutFlowTriggerEnum
from payrix.models.payout_flow_um_enum import PayoutFlowUmEnum
from payrix.models.payout_flows_post_request import PayoutFlowsPostRequest
from payrix.models.payout_inactive_enum import PayoutInactiveEnum
from payrix.models.same_day_enum import SameDayEnum
from payrix.models.skip_off_days_enum import SkipOffDaysEnum
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

payout_flows_controller = client.payout_flows
body = PayoutFlowsPostRequest(
    login='t1_log_673245a79517f80bf2e7738',
    trigger=PayoutFlowTriggerEnum.BOARD,
    schedule=PayoutFlowScheduleEnum.WEEKS,
    schedule_factor=1,
    um=PayoutFlowUmEnum.PERCENT,
    amount=10000,
    payout_inactive=PayoutInactiveEnum.INACTIVE,
    skip_off_days=SkipOffDaysEnum.DONOTSKIP,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    payout_login='payoutLogin',
    org='t1_org_67b8f82d4f96c5a520ef5c8',
    entity='p1_ent_00ce6d2c1f773f68e9cbe00',
    billing='t1_bil_67d9c8a7df33cf77a3e5e0z',
    start=20160120,
    minimum=5000,
    secondary_descriptor='Wellness',
    currency=CurrencyEnum.USD,
    same_day=SameDayEnum.DISABLED
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = payout_flows_controller.post_payout_flows(
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

