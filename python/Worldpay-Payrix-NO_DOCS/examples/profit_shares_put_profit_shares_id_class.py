from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.profit_share_type_enum import ProfitShareTypeEnum
from payrix.models.profit_shares_put_request import ProfitSharesPutRequest
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

profit_shares_controller = client.profit_shares
id = 't1_psh_67aa7fd81e45a8b5eb569yz'

body = ProfitSharesPutRequest(
    login='t1_log_67aa2de0a914190a267b672',
    entity='t1_ent_67aa5d38dbb22dc72775f72',
    forentity='t1_ent_673fa38d3e069c7ac4bdbd8',
    org='t1_org_67aa73a2d8098f2853f97ee',
    division='t1_div_67b51635da21f7399ce2af0',
    partition='t1_ptn_666834d4d504f11234578f0',
    mtype=ProfitShareTypeEnum.INCOME,
    name='LEad Capture',
    description='Webhook test2',
    amount=5000,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = profit_shares_controller.put_profit_shares_id(
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

