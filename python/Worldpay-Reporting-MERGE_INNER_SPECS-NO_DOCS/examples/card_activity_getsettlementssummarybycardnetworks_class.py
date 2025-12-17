from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.card_network_2_enum import CardNetwork2Enum
from reportingapi.models.credit_card_activity_summary_request import CreditCardActivitySummaryRequest
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
body = CreditCardActivitySummaryRequest(
    hierarchy=Hierarchy(
        level=Level12Enum.CHAIN,
        values=[
            'AB1234',
            '111217'
        ]
    ),
    card_network=CardNetwork2Enum.MASTERCARD,
    card_number='634527',
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2019-07-27',
        to_date='2019-09-13'
    )
)

try:
    result = card_activity_controller.getsettlementssummarybycardnetworks(
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

