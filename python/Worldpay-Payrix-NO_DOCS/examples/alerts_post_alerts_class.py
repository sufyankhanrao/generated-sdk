from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.alerts_post_request import AlertsPostRequest
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
body = AlertsPostRequest(
    login='t1_log_61f2efc258eb7bf6d380000',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    forlogin='t1_log_61f2efc258eb7bf6d380000',
    team='t1_tem_67c202b908935b505104500',
    division='t1_div_67c56806728fbbf0bae0z00',
    partition='t1_ptn_666834d4d504f21414978f0',
    name='williamson',
    description='Used by the FrontDesk system to keep information up to date via webhook alerts'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = alerts_controller.post_alerts(
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

