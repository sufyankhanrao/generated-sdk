from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.application_enum import ApplicationEnum
from payrix.models.decision_type_enum import DecisionTypeEnum
from payrix.models.decisions_put_request import DecisionsPutRequest
from payrix.models.descision_action_enum import DescisionActionEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.period_enum import PeriodEnum
from payrix.models.target_enum import TargetEnum
from payrix.models.use_cache_enum import UseCacheEnum
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

decisions_controller = client.decisions
id = 't1_dcs_67ddb8ad653487caf88cc00'

body = DecisionsPutRequest(
    login='t1_log_61e72ab44fd39df9483aa2c',
    org='t1_org_5fada4629c317f80bc9cb12',
    entity='t1_ent_67d86dfd3442f3e2927ecbd',
    decision='t1_dcs_6789a1b36647513d66cf30a',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_000111d4d504f21414978f0',
    application=ApplicationEnum.TXN,
    level='partition',
    mtype=DecisionTypeEnum.CVV,
    target=TargetEnum.POSTAUTH,
    action=DescisionActionEnum.BLOCK,
    sequence=0,
    amount=1,
    value='1',
    period=PeriodEnum.DAYS,
    period_factor=1,
    schedule_factor=1,
    start=20160120,
    finish=20160120,
    low=1,
    high=2,
    use_cache=UseCacheEnum.DISABLED,
    cache_time=0,
    options=0,
    additional_options=0,
    error_message='Unable to accept without CVV',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = decisions_controller.put_decisions_id(
        id,
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

