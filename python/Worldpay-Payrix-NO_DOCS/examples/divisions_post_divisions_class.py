from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.change_management_enabled_enum import ChangeManagementEnabledEnum
from payrix.models.divisions_post_request import DivisionsPostRequest
from payrix.models.min_password_complexity_enum import MinPasswordComplexityEnum
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

divisions_controller = client.divisions
body = DivisionsPostRequest(
    login='t1_log_67e150467ee225924163f18',
    name='sampleDivision',
    email='testuse1@example.com',
    change_management_enabled=ChangeManagementEnabledEnum.DISABLED,
    min_password_length=9,
    min_password_complexity=MinPasswordComplexityEnum.ONE
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = divisions_controller.post_divisions(
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

