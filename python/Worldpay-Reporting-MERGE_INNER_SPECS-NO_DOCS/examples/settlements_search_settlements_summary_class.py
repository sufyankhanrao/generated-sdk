from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_3_exception import ErrorResponseError3Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.month_range import MonthRange
from reportingapi.models.net_settled_amount_card_type_request import NetSettledAmountCardTypeRequest
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

settlements_controller = client.settlements
body = NetSettledAmountCardTypeRequest(
    independent_sales_channel_codes=[
        'MTBCON',
        'MTBNEW'
    ],
    month_range=MonthRange(
        start_month='2022-01',
        end_month='2022-06'
    ),
    messaging_types=[
        'PIN',
        'SIG'
    ],
    card_present=True
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

try:
    result = settlements_controller.search_settlements_summary(
        body,
        v_correlation_id=v_correlation_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseError3Exception as e: 
    print(e)
except APIException as e: 
    print(e)

