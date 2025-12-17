from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.fee_application_enum import FeeApplicationEnum
from payrix.models.fee_rule_type_enum import FeeRuleTypeEnum
from payrix.models.fee_rules_put_request import FeeRulesPutRequest
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

fee_rules_controller = client.fee_rules
id = 't1_frl_67ce8623bc70042ef58f400'

body = FeeRulesPutRequest(
    fee='t1_fee_67ce8623b048d0d5284a886',
    name='Fee Rule1',
    description='Fee Rule',
    mtype=FeeRuleTypeEnum.SALE,
    application=FeeApplicationEnum.BOTH,
    value='1',
    grouping='Fee Rule Group1',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = fee_rules_controller.put_fee_rules_id(
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

