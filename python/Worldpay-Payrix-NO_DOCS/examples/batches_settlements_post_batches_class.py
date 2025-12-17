from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.batch_platform_enum import BatchPlatformEnum
from payrix.models.batch_status_enum import BatchStatusEnum
from payrix.models.batches_post_request import BatchesPostRequest
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

batches_settlements_controller = client.batches_settlements
body = BatchesPostRequest(
    merchant='t1_mer_63341144b40742676bea201',
    platform=BatchPlatformEnum.VANTIV,
    status=BatchStatusEnum.OPEN,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    ref='reference code of batch',
    client_ref='merchant\'s reference code',
    processing_id='Internal ID'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = batches_settlements_controller.post_batches(
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

