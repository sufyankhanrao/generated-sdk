from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.aggregation_schedule_enum import AggregationScheduleEnum
from payrix.models.aggregation_status_enum import AggregationStatusEnum
from payrix.models.aggregation_type_enum import AggregationTypeEnum
from payrix.models.aggregations_put_request import AggregationsPutRequest
from payrix.models.default_enum import DefaultEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.level_enum import LevelEnum
from payrix.models.resource_enum import ResourceEnum
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

aggregations_controller = client.aggregations
id = 't1_agg_67b339d00940f0d12b000b7'

body = AggregationsPutRequest(
    login='t1_log_67b5002a5de3b716ad97e07',
    entity='t1_ent_676057654c1b7452e4884f0',
    forlogin='t1_log_67b5002a5de3b716ad97e07',
    org='t1_org_67b736ad7d05922343246cf',
    team='teamBoarding',
    division='t1_div_67b51635da21f7399ce2af1',
    partition='t1_ptn_666834d4d504f11234578f5',
    mtype=AggregationTypeEnum.MERCHANTTXNFAILEDALL,
    level=LevelEnum.MERCHANT,
    name='Default merchantTxnFailedAll',
    description='Automatically created aggregation',
    resource=ResourceEnum.TXNS,
    search='status[equals]=2&created[like]={{"expand": [{"type": "date","value": "-1 days","format": "Y-m-d","relativeTimestamp":":effective:"}]}}%',
    totals='sum[0]=total&count[0]=id&groups[0]=merchant&groups[1]=type&groups[2][payment][0]=method',
    degrouping='groups[0]=merchant&groups[1][payment][0]=method',
    status=AggregationStatusEnum.READY,
    schedule=AggregationScheduleEnum.DAYS,
    schedule_factor=1,
    start=202502200000,
    default=DefaultEnum.AUTOMATICALLYCREATED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

search_filter = 'created[equals]=2025-01-01'

try:
    result = aggregations_controller.put_aggregations_id(
        id,
        body,
        request_token=request_token,
        search_filter=search_filter
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorFourHundredException as e: 
    print(e)
except APIException as e: 
    print(e)

