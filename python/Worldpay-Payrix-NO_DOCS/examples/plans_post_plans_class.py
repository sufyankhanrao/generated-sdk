from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.plan_schedule_enum import PlanScheduleEnum
from payrix.models.plan_type_enum import PlanTypeEnum
from payrix.models.plan_um_enum import PlanUmEnum
from payrix.models.plans_post_request import PlansPostRequest
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

plans_controller = client.plans
body = PlansPostRequest(
    amount=50000,
    merchant='p1_mer_000444add0403c3553f4d20',
    schedule=PlanScheduleEnum.DAILY,
    schedule_factor=1,
    um=PlanUmEnum.ACTUAL,
    mtype=PlanTypeEnum.RECURRING,
    billing='p1_bil_00cee36329ead6ae6d31e43',
    order='S1 - 1000 - LAST',
    txn_description='Payment Plan',
    description='Payment',
    max_failures=2,
    name='Lind - Wyman Subscription Plan weekly',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = plans_controller.post_plans(
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

