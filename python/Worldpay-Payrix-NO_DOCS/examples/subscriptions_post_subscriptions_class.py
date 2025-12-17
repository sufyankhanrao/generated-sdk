from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.subscription_origin_enum import SubscriptionOriginEnum
from payrix.models.subscriptions_post_request import SubscriptionsPostRequest
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
body = SubscriptionsPostRequest(
    plan='t1_pln_680064c9e9920768c5f7156',
    start=20250416,
    origin=SubscriptionOriginEnum.ECOMMERCE,
    authentication='Authentication token',
    failures=0,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    statement_entity='paying entity',
    first_txn='t1_txn_680064d333e8a4e6cc85903',
    finish=20250416,
    tax=0,
    descriptor='Subscription Descriptor',
    txn_description='subscription1',
    order='t183l8nsmsiq',
    authentication_id='Authentication reference ID',
    max_failures=0
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = subscriptions_controller.post_subscriptions(
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

