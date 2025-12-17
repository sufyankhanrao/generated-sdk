from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_4_exception import ErrorResponseError4Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.month_range_1 import MonthRange1
from reportingapi.models.signed_deals_summary_month_request import SignedDealsSummaryMonthRequest
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

signed_deals_controller = client.signed_deals
body = SignedDealsSummaryMonthRequest(
    independent_sales_channel_codes=[
        'MTBCON',
        'MTBNEW'
    ],
    month_range=MonthRange1(
        start_month='2022-01',
        end_month='2022-06'
    )
)

v_correlation_id = '3fcb1437-4e52-4946-9ae1-e618351b6d16'

try:
    result = signed_deals_controller.post_signed_deals_summary_month(
        body,
        v_correlation_id=v_correlation_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseError4Exception as e: 
    print(e)
except APIException as e: 
    print(e)

