from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.currency_enum import CurrencyEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.payout_post_request import PayoutPostRequest
from payrix.models.payout_schedule_enum import PayoutScheduleEnum
from payrix.models.payout_um_enum import PayoutUmEnum
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

payouts_controller = client.payouts
body = PayoutPostRequest(
    account='8ccbda671ad9463f2d7cab3119010000',
    entity='p1_ent_00ce6d2c1f773f68e9cbe05',
    schedule=PayoutScheduleEnum.DAILY,
    schedule_factor=1,
    start=20250312,
    um=PayoutUmEnum.PERCENTAGE,
    amount=100,
    float=0,
    skip_off_days=SkipOffDaysEnum.DONOTSKIP,
    same_day=SameDayEnum.DISABLED,
    login='p1_log_0af4e8c7d3a625ed0f4ee1e0',
    billing='p1_bil_0078b6a1899f8d14f58d7c5',
    payout_flow='p1_pfw_000f0148a5d61a4dec3f108',
    name='Automatically generated payout schedule',
    description='payout schedule description',
    currency=CurrencyEnum.USD,
    minimum=0,
    maximum=0,
    secondary_descriptor='Wellness',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = payouts_controller.post_payouts(
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

