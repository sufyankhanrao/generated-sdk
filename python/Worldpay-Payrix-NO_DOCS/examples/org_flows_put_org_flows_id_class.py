from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.org_flow_trigger_enum import OrgFlowTriggerEnum
from payrix.models.org_flows_put_request import OrgFlowsPutRequest
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

org_flows_controller = client.org_flows
id = 't1_ofw_67ed51ece84aae1a7d0000z'

body = OrgFlowsPutRequest(
    login='g1577139c2304b7',
    trigger=OrgFlowTriggerEnum.CREATE,
    forlogin='t1_log_67c203583fbd0a4437d1332',
    team='t1_tem_67c202b908935b505104500',
    division='t1_div_67c56806728fbbf0bae0b10',
    partition='t1_ptn_666834d4d504f21414978f5'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = org_flows_controller.put_org_flows_id(
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

