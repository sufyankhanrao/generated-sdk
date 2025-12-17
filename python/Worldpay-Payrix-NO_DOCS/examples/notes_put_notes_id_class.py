from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.note_type_enum import NoteTypeEnum
from payrix.models.notes_put_request import NotesPutRequest
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

notes_controller = client.notes
id = 'p1_not_00c7145c4daae43427e0d91'

body = NotesPutRequest(
    login='p1_log_00c59f2b74896e4086c2fe6',
    txn='t1_txn_67ea9ac271f195a95059550',
    terminal_txn='identifier',
    hold='t1_hld_67e08f086e275ddcc8820e1',
    entity='p1_ent_00c1ff2d61b43ffab63cec5',
    mtype=NoteTypeEnum.NOTE,
    data='amexSales',
    note='Raised HT limit',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = notes_controller.put_notes_id(
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

