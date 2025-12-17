from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.eid_search_req import EIDSearchReq
from shelldatareportingapis.models.eid_search_request import EIDSearchRequest
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

body = EIDSearchRequest(
    filters=EIDSearchReq(
        col_co_code=32,
        account_group_country=32,
        account_group_id=[
            '122'
        ],
        account_group_name=None,
        from_date='2017/08/30',
        to_date='2017/10/31',
        invoice_type='NAT',
        invoice_status='NEW',
        sort_by=[
            'DocumentDate ASC'
        ]
    ),
    page=1,
    page_size=10
)

try:
    result = invoice_controller.eid_search(
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

