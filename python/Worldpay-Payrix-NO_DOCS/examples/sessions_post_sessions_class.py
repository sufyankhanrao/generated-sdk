from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.password import PasswordCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.http.auth.username import UsernameCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.mfa_authenticated_enum import MfaAuthenticatedEnum
from payrix.models.session_public_enum import SessionPublicEnum
from payrix.models.sessions_post_request import SessionsPostRequest
from payrix.models.token_enum import TokenEnum
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
    username_credentials=UsernameCredentials(
        username='USERNAME'
    ),
    password_credentials=PasswordCredentials(
        password='PASSWORD'
    ),
    environment=Environment.QA
)

sessions_controller = client.sessions
body = SessionsPostRequest(
    public=SessionPublicEnum.PUBLICACCESS,
    token=TokenEnum.AUTHTOKENDISABLED,
    mfa_authenticated=MfaAuthenticatedEnum.MFADISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    login='p1_log_00a4d56d1b5c98e8694ae28'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = sessions_controller.post_sessions(
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

