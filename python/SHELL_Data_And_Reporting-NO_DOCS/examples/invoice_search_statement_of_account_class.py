from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.search_soa_req import SearchSOAReq
from shelldatareportingapis.models.search_statement_of_account_request import SearchStatementOfAccountRequest
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

body = SearchStatementOfAccountRequest(
    filters=SearchSOAReq(
        col_co_code=18,
        payer_number='NL99781417',
        invoice_number='0123456789',
        from_date='2022/05/04',
        to_date='2022/05/10',
        period=1,
        invoice_date='20170830',
        invoice_status=[
            'Due'
        ],
        sort_by=[
            1
        ]
    ),
    page=1,
    page_size=10
)

try:
    result = invoice_controller.search_statement_of_account(
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

