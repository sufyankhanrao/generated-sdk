from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.application_enum import ApplicationEnum
from payrix.models.decision_action_type_enum import DecisionActionTypeEnum
from payrix.models.decision_actions_put_request import DecisionActionsPutRequest
from payrix.models.descision_actions_action_enum import DescisionActionsActionEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.score_type_enum import ScoreTypeEnum
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

decision_actions_controller = client.decision_actions
id = 't1_dca_67ddc0163f51a4ffd1ea3d0'

body = DecisionActionsPutRequest(
    decision='t1_dcs_67ddc0163a32ae0c5c33bfc',
    action=DescisionActionsActionEnum.BLOCK,
    application=ApplicationEnum.ACCOUNT,
    score_type=ScoreTypeEnum.LOW,
    mtype=DecisionActionTypeEnum.LESS,
    field='score',
    score='20',
    data='dummy@dummy.neoncrm.com',
    message='Required',
    code='I602',
    grouping='bademail',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = decision_actions_controller.put_decision_actions_id(
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

