from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.invoice_download_req import InvoiceDownloadReq
from shelldatareportingapis.models.invoice_download_request import InvoiceDownloadRequest
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

body = InvoiceDownloadRequest(
    filters=InvoiceDownloadReq(
        col_co_code=18,
        payer_number='NL99781417',
        account_number=[
            'NL99781420'
        ],
        document_reference=[
            1234567890
        ],
        invoice_or_soa_number='2234556'
    )
)

try:
    result = invoice_controller.download(
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

