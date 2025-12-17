from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.iplist_type_enum import IplistTypeEnum
from payrix.models.iplists_post_request import IplistsPostRequest
from payrix.models.version_enum import VersionEnum
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

ip_address_lists_controller = client.ip_address_lists
body = IplistsPostRequest(
    login='t1_log_61d874fe8b166d56672d0f9',
    version=VersionEnum.IPV4,
    mtype=IplistTypeEnum.WHITELIST,
    start='1.1.1.1',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    finish='1.1.1.89'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = ip_address_lists_controller.post_iplists(
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

