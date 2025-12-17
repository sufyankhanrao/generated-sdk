from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.alerts_put_request import AlertsPutRequest
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

alerts_controller = client.alerts
id = 't1_alt_67d1a66d3af03677cdc7db0'

body = AlertsPutRequest(
    login='t1_log_61f2efc258eb7bf6d380000',
    forlogin='t1_log_61f2efc258eb7bf6d380000',
    team='t1_tem_67c202b908935b505104500',
    division='t1_div_67c56806728fbbf0bae0z00',
    partition='t1_ptn_666834d4d504f21414978f0',
    name='williamson',
    description='Used by the FrontDesk system to keep information up to date via webhook alerts',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = alerts_controller.put_alerts_id(
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

