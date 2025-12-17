from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.debit_card_activity_summary_request import DebitCardActivitySummaryRequest
from reportingapi.models.debit_card_network_enum import DebitCardNetworkEnum
from reportingapi.models.hierarchy import Hierarchy
from reportingapi.models.level_12_enum import Level12Enum
from reportingapi.models.search_auth_transactions_request_real_time_transaction_date_range import SearchAuthTransactionsRequestRealTimeTransactionDateRange
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

card_activity_controller = client.card_activity
v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

body = DebitCardActivitySummaryRequest(
    hierarchy=Hierarchy(
        level=Level12Enum.MERCHANT,
        values=[
            '4445000123456',
            '4445191034215'
        ],
        chain_code='AB1234'
    ),
    card_network=DebitCardNetworkEnum.WIC,
    card_number='************4353',
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    )
)

try:
    result = card_activity_controller.getcardactivitysummarybydebit(
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

