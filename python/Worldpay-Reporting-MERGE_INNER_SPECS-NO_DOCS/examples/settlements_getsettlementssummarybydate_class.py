from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.daily_tran_summary_input import DailyTranSummaryInput
from reportingapi.models.field_name_16_enum import FieldName16Enum
from reportingapi.models.order_by_enum import OrderByEnum
from reportingapi.models.order_by_for_date_summary_type import OrderByForDateSummaryType
from reportingapi.models.search_auth_transactions_request_real_time_transaction_date_range import SearchAuthTransactionsRequestRealTimeTransactionDateRange
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

settlements_controller = client.settlements
body = DailyTranSummaryInput(
    sort_results_by=OrderByForDateSummaryType(
        field_name=FieldName16Enum.PROCESS_DATE,
        order_by=OrderByEnum.ASC
    ),
    merchant_id='4445000860874',
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2023-05-05',
        to_date='2023-07-24'
    )
)

try:
    result = settlements_controller.getsettlementssummarybydate(
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

