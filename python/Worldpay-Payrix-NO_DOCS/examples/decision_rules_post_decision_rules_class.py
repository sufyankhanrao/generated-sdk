from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.decision_rule_type_enum import DecisionRuleTypeEnum
from payrix.models.decision_rules_post_request import DecisionRulesPostRequest
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

decision_rules_controller = client.decision_rules
body = DecisionRulesPostRequest(
    decision='t1_dcs_67d97ed1a0fc6848c89d537',
    mtype=DecisionRuleTypeEnum.TYPE,
    value=8,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='DecisionRule11',
    description='Rule Description',
    grouping='portalgroup_2'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = decision_rules_controller.post_decision_rules(
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

