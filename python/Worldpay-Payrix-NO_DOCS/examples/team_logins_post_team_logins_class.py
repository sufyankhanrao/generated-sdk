from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.create_enum import CreateEnum
from payrix.models.delete_enum import DeleteEnum
from payrix.models.reference_enum import ReferenceEnum
from payrix.models.team_admin_enum import TeamAdminEnum
from payrix.models.team_login_post_request import TeamLoginPostRequest
from payrix.models.team_login_read_enum import TeamLoginReadEnum
from payrix.models.update_enum import UpdateEnum
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

team_logins_controller = client.team_logins
body = TeamLoginPostRequest(
    login='t1_log_6802c54cba888f6abfd88cc',
    team='t1_tem_6621af6c10f4a29427a2d35',
    create=CreateEnum.ENUM_NONE,
    read=TeamLoginReadEnum.ENUM_NONE,
    update=UpdateEnum.ENUM_NONE,
    delete=DeleteEnum.ENUM_NONE,
    reference=ReferenceEnum.ENUM_NONE,
    team_admin=TeamAdminEnum.ENUM_NONE
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = team_logins_controller.post_team_logins(
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

