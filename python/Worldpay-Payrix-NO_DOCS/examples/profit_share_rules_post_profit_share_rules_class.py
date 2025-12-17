from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.profit_share_rule_type_enum import ProfitShareRuleTypeEnum
from payrix.models.profit_share_rules_post_request import ProfitShareRulesPostRequest
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

profit_share_rules_controller = client.profit_share_rules
body = ProfitShareRulesPostRequest(
    profit_share='t1_psh_63de0ece4959d9de8194a4d',
    mtype=ProfitShareRuleTypeEnum.LESS,
    value='5',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='Test2',
    description='Test2',
    grouping='group1'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = profit_share_rules_controller.post_profit_share_rules(
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

