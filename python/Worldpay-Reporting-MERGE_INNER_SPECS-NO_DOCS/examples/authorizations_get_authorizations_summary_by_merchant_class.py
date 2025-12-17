from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.auth_transactions_summary_request_by_merchant import AuthTransactionsSummaryRequestByMerchant
from reportingapi.models.date_range_search import DateRangeSearch
from reportingapi.models.entity_merchant import EntityMerchant
from reportingapi.models.level_11_enum import Level11Enum
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

authorizations_controller = client.authorizations
body = AuthTransactionsSummaryRequestByMerchant(
    hierarchy=EntityMerchant(
        level=Level11Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    )
)

try:
    result = authorizations_controller.get_authorizations_summary_by_merchant(
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

