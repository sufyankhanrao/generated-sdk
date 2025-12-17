from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.confirm_code_type_enum import ConfirmCodeTypeEnum
from payrix.models.confirm_codes_post_request import ConfirmCodesPostRequest
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

confirmation_codes_controller = client.confirmation_codes
body = ConfirmCodesPostRequest(
    login='p1_log_67dd2714959c3331228ffa3',
    mtype=ConfirmCodeTypeEnum.EMAIL,
    key='fbdf954596b341d18cb4995b70d321f3',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    email='vijay.sample@payrix.com'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = confirmation_codes_controller.post_confirm_codes(
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

