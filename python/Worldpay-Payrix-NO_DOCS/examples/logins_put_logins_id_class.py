from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.confirmed_enum import ConfirmedEnum
from payrix.models.country_enum import CountryEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.logins_put_request import LoginsPutRequest
from payrix.models.mfa_enabled_enum import MfaEnabledEnum
from payrix.models.portal_access_enum import PortalAccessEnum
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

logins_controller = client.logins
id = 't1_log_67c56806038bb4eb85a0000'

body = LoginsPutRequest(
    login='g15967a6e0d7cf6',
    partition='g157713aff9b946',
    division='t1_div_67c56806728fbbf0bae0b10',
    parent_division='t1_div_67c56806728fbbf0bae0b10',
    roles=64,
    confirmed=ConfirmedEnum.NOTCONFIRMED,
    username='user9287347954',
    password='****',
    first='John',
    last='Doe',
    email='user2118145526@example.com',
    allowed_resources='{"create":["accounts","payouts"],"read":["disbursements","disbursementResults"],"update":["accounts","payouts"],"delete":["accounts","payouts"],"totals":["disbursements","disbursementResults"]}',
    restricted_resources='{"create":["ltxns"],"read":["txnResults"],"update":["txns"],"delete":["txns"],"totals":["txns"]}',
    portal_access=PortalAccessEnum.HASACCESS,
    mfa_enabled=MfaEnabledEnum.DISABLED,
    mfa_secret='****',
    mfa_enrolled_date='2025-06-16 08:02:53',
    mfa_type='totp',
    address_1='9337 SPRING CYPRESS RD STE A413',
    address_2='Suite 403',
    city='Spring',
    state='TX',
    zip='77379',
    country=CountryEnum.USA,
    phone='1028106820',
    fax='1085069293',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = logins_controller.put_logins_id(
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

