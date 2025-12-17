from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.month_range import MonthRange
from reportingapi.models.monthly_tran_summary_input_chain import MonthlyTranSummaryInputCHAIN
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

settlements_controller = client.settlements
body = MonthlyTranSummaryInputCHAIN(
    chain_code='111186',
    date_range=MonthRange(
        start_month='2023-03',
        end_month='2023-06'
    )
)

try:
    result = settlements_controller.getsettlementssummarybymonth(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseError2Exception as e: 
    print(e)
except APIException as e: 
    print(e)

