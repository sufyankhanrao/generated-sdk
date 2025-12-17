from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.account_method_enum import AccountMethodEnum
from payrix.models.account_primary_enum import AccountPrimaryEnum
from payrix.models.account_status_enum import AccountStatusEnum
from payrix.models.account_type_enum import AccountTypeEnum
from payrix.models.accounts_put_request import AccountsPutRequest
from payrix.models.accounts_put_request_schema_properties import AccountsPutRequestSchemaProperties
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

accounts_controller = client.accounts
id = 't1_act_12a003cde5d6b2ec3d9canb'

body = AccountsPutRequest(
    account=AccountsPutRequestSchemaProperties(
        method=AccountMethodEnum.CHECKING,
        number='2',
        routing='1'
    ),
    name='Bank Account Name',
    description='Bank account description',
    primary=AccountPrimaryEnum.PRIMARY,
    mtype=AccountTypeEnum.ALL,
    status=AccountStatusEnum.READY,
    expiration='0118',
    mask='2345',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = accounts_controller.put_accounts_id(
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

