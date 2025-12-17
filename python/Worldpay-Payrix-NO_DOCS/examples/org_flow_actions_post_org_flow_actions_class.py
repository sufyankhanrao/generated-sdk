from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.org_flow_action_enum import OrgFlowActionEnum
from payrix.models.org_flow_actions_post_request import OrgFlowActionsPostRequest
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

org_flow_actions_controller = client.org_flow_actions
body = OrgFlowActionsPostRequest(
    org_flow='t1_ofw_67ed51ece84aae1a7d0783z',
    org='t1_org_67c89c538efe67fbf018d00',
    action=OrgFlowActionEnum.ADD
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = org_flow_actions_controller.post_org_flow_actions(
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

