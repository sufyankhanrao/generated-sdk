from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.invoice_search_request import InvoiceSearchRequest
from shelldatareportingapis.models.invoice_search_request_filters import InvoiceSearchRequestFilters
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

body = InvoiceSearchRequest(
    filters=InvoiceSearchRequestFilters(
        col_co_id=14,
        payer_id=78,
        payer_number='DE26688478',
        invoice_id=4013059,
        invoice_number='0123456789',
        from_date='20170830',
        to_date='20171031',
        invoice_date='20171031',
        summary_document_id=1616729,
        summary_document_number='1283899/289261063/2019',
        statement_of_account_id='DE26702892',
        so_a_reference_number='1283899',
        period=1,
        invoice_status='Due',
        invoiced_on_behalf_of='DE',
        include_e_invoice_details=False,
        mtype='Original'
    ),
    page_size=50,
    page=1
)

try:
    result = invoice_controller.invoice_search(
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

