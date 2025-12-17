from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.envelope_status_enum import EnvelopeStatusEnum
from foxitesigntest.models.report import Report

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

reports_api_controller = client.reports_api
accept = 'application/vnd.ms-excel'

body = Report(
    status=EnvelopeStatusEnum.EXECUTED,
    creation_date_from='2022-01-01',
    creation_date_to='2022-04-01',
    include_fields='false'
)

try:
    result = reports_api_controller.download_report(
        accept,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

