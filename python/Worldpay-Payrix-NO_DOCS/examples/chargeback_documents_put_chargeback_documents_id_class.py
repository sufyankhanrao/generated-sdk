from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.chargeback_document_type_enum import ChargebackDocumentTypeEnum
from payrix.models.chargebacks_documents_put_request import ChargebacksDocumentsPutRequest
from payrix.models.document_source_enum import DocumentSourceEnum
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

chargeback_documents_controller = client.chargeback_documents
id = 't1_chd_679a4a2ba49405540af4856'

body = ChargebacksDocumentsPutRequest(
    mtype=ChargebackDocumentTypeEnum.PDF,
    ref='p1_chd_67b31fca23feed2b88d8a59.pdf',
    description='Test PDF  copy.pdf',
    name='Test PDF  copy.pdf',
    document_source=DocumentSourceEnum.MERCHANT,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = chargeback_documents_controller.put_chargeback_documents_id(
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

