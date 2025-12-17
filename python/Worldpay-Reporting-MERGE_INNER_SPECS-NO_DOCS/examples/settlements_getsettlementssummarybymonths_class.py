from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.monthly_tran_summary_input import MonthlyTranSummaryInput
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

settlements_controller = client.settlements
v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

body = MonthlyTranSummaryInput(
    merchant_id='4445191034215',
    chain_code='070110'
)

try:
    result = settlements_controller.getsettlementssummarybymonths(
        v_correlation_id=v_correlation_id,
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

