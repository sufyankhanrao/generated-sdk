from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.subscription_origin_enum import SubscriptionOriginEnum
from payrix.models.subscriptions_put_request import SubscriptionsPutRequest
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

subscriptions_controller = client.subscriptions
id = 't1_sbn_680064d2db9dbdc8d3e9a0z'

body = SubscriptionsPutRequest(
    plan='t1_pln_680064c9e9920768c5f7156',
    statement_entity='paying entity',
    first_txn='t1_txn_680064d333e8a4e6cc85903',
    start=20250416,
    finish=20250416,
    tax=0,
    descriptor='Subscription Descriptor',
    txn_description='subscription1',
    order='t183l8nsmsiq',
    origin=SubscriptionOriginEnum.ECOMMERCE,
    authentication='Authentication token',
    authentication_id='Authentication reference ID',
    failures=0,
    max_failures=0,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = subscriptions_controller.put_subscriptions_id(
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

