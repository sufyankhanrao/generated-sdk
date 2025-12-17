from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.auto_cascade_disabled_enum import AutoCascadeDisabledEnum
from payrix.models.auto_cascade_owner_enum import AutoCascadeOwnerEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.teams_put_request import TeamsPutRequest
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

teams_controller = client.teams
id = 't1_tem_680155b5a6467e4911aa0z0'

body = TeamsPutRequest(
    login='t1_log_6801559c6218199cb0820df',
    name='merchant-team-t1_mer_680155985dbaab55256ecb0',
    description='Esmeralda McCullough Team',
    auto_cascade_disabled=AutoCascadeDisabledEnum.DISABLED,
    auto_cascade_owner=AutoCascadeOwnerEnum.OFF,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = teams_controller.put_teams_id(
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

