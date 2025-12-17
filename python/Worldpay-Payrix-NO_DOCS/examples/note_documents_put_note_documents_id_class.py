from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.note_document_status_enum import NoteDocumentStatusEnum
from payrix.models.note_document_type_enum import NoteDocumentTypeEnum
from payrix.models.note_documents_document_type_enum import NoteDocumentsDocumentTypeEnum
from payrix.models.note_documents_put_request import NoteDocumentsPutRequest
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

note_documents_controller = client.note_documents
id = 't1_ntd_67eef7a7ac0627e1fce0000'

body = NoteDocumentsPutRequest(
    mtype=NoteDocumentTypeEnum.PNG,
    name='Boy1.png',
    custom='identifier',
    description='doc description1',
    status=NoteDocumentStatusEnum.PROCESSED,
    document_type=NoteDocumentsDocumentTypeEnum.VOIDCHECK,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = note_documents_controller.put_note_documents_id(
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

