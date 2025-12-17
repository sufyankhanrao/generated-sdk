from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.reserve_entries_post_request import ReserveEntriesPostRequest
from payrix.models.reserve_entry_event_enum import ReserveEntryEventEnum
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

reserve_entry_controller = client.reserve_entry
body = ReserveEntriesPostRequest(
    login='t1_log_5d652e3c9bb91623e859e02',
    fund='t1_fun_5e6186054d4dbe2416bca5c',
    event=ReserveEntryEventEnum.AUTH,
    amount=15,
    entry='t1_etr_6800d1dee193517e5d6ce91',
    hold='t1_hld_67ef5bad3be038935902200',
    txn='t1_txn_67caef0a014c280a6caa5zz',
    reserve='t1_rsv_5e21064368e32ef4d38f8d4',
    entity_reserve='identifier',
    reserve_entry='identifier',
    onentity='t1_ent_00c2b1a6102ffdd33f11000',
    event_id='t1_txn_6800d1dd114238a04f4e608',
    description='description1',
    release='20160120'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = reserve_entry_controller.post_reserve_entries(
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

