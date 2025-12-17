from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.level_enum import LevelEnum
from payrix.models.release_enum import ReleaseEnum
from payrix.models.reserves_put_request import ReservesPutRequest
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

reserves_controller = client.reserves
id = 't1_rsv_66f27fca06f8a777998c000'

body = ReservesPutRequest(
    login='t1_log_611e6ca320fae7afab2f256',
    org='t1_org_5fada4629c317f80bc9cb00',
    division='t1_div_67b51635da21f7399ce2az0',
    partition='t1_ptn_000834d4d504f11234578f0',
    level=LevelEnum.MERCHANT,
    entity='t1_ent_5f9058fe8c8d21ead8f68dc',
    hold='t1_hld_66f27fca0236545c4f125d2',
    name='Additional Underwriting Review Required',
    description='Will release the reserve once all information is verified.',
    percent=10000,
    release=ReleaseEnum.NEVER,
    release_factor=1,
    start=20160120,
    finish=20160120,
    max=0,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = reserves_controller.put_reserves_id(
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

