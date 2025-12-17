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
from payrix.models.accounts_account import AccountsAccount
from payrix.models.accounts_post_request import AccountsPostRequest
from payrix.models.currency_enum import CurrencyEnum
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
body = AccountsPostRequest(
    entity='t1_ent_5a1pf5a1234531155a12345',
    account=AccountsAccount(
        method=AccountMethodEnum.CHECKING,
        number='2',
        routing='1'
    ),
    primary=AccountPrimaryEnum.PRIMARY,
    mtype=AccountTypeEnum.ALL,
    status=AccountStatusEnum.READY,
    currency=CurrencyEnum.USD,
    name='Bank Account Name',
    description='Bank account description',
    expiration='0118',
    public_token='public-test-a12eeba1-1234-4567-af1g-d80cc1bfd713',
    mask='2345',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = accounts_controller.post_accounts(
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

