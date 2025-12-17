from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.accounts import Accounts
from shelldatareportingapis.models.invoice_dates_request import InvoiceDatesRequest
from shelldatareportingapis.models.invoice_dates_request_filters import InvoiceDatesRequestFilters
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

body = InvoiceDatesRequest(
    filters=InvoiceDatesRequestFilters(
        col_co_code=0,
        col_co_id=0,
        payer_id=0,
        payer_number='string',
        accounts=[
            Accounts(
                account_id=3453,
                account_number='GB000000124'
            )
        ]
    )
)

try:
    result = invoice_controller.dates(
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

