from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.statement_of_account_request import StatementOfAccountRequest
from shelldatareportingapis.models.statement_of_account_request_filters import StatementOfAccountRequestFilters
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

body = StatementOfAccountRequest(
    filters=StatementOfAccountRequestFilters(
        col_co_code=32,
        payer_id=308,
        payer_number='CZ56891709',
        include_monthly_invoice_trend=True,
        include_past_statement_of_accounts=True,
        due_or_over_due_soa_documents_only=False,
        number_of_soa_documents=10,
        include_account_invoices_summary=True
    )
)

try:
    result = invoice_controller.statement_of_account(
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

