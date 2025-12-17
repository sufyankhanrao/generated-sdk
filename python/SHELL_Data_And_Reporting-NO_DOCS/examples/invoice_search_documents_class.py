from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.search_doc_req import SearchDocReq
from shelldatareportingapis.models.search_documents_request import SearchDocumentsRequest
from shelldatareportingapis.shell_data_reporting_ap_is_client import ShellDataReportingApIsClient

client = ShellDataReportingApIsClient(
    bearer_token_credentials=BearerTokenCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SIT
)

invoice_controller = client.invoice
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = SearchDocumentsRequest(
    filters=SearchDocReq(
        payer_number='DE00000096',
        col_co_code=14,
        account_number='DE00000096',
        account_number_list=[
            'DE00000123',
            'DE00000225'
        ],
        invoice_number='1234567',
        invoice_number_list=[
            '6400013693',
            '9421000010'
        ],
        invoice_status='NEW',
        issuing_date_from='2023/05/01',
        issuing_date_to='2023/06/30',
        due_date_from='2023/05/04',
        due_date_to='2023/06/30',
        gross_amount='1000',
        gross_amount_operator='LT',
        document_type='SOA',
        vat_issuer_country='DE',
        sorty_by=[
            'InvoiceNumber ASC',
            'InvoiceDate DESC'
        ]
    ),
    page='1',
    page_size='50'
)

try:
    result = invoice_controller.search_documents(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorObjectException as e: 
    print(e)
except APIException as e: 
    print(e)

