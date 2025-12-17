from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.eid_download_req import EIDDownloadReq
from shelldatareportingapis.models.eid_download_request import EIDDownloadRequest
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

body = EIDDownloadRequest(
    filters=EIDDownloadReq(
        col_co_code=18,
        eid_list=[
            '1710187',
            '1734566'
        ],
        account_group_country=18,
        account_group_id_list=[
            '26685402'
        ]
    )
)

try:
    result = invoice_controller.eid_download(
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

