from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.date_range_search import DateRangeSearch
from reportingapi.models.deposit_summary_merchant_request import DepositSummaryMerchantRequest
from reportingapi.models.entity_merchant_1 import EntityMerchant1
from reportingapi.models.level_11_enum import Level11Enum
from reportingapi.models.pagination_type_1 import PaginationType1
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

deposit_summary_controller = client.deposit_summary
body = DepositSummaryMerchantRequest(
    hierarchy=EntityMerchant1(
        level=Level11Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    ),
    pagination=PaginationType1(
        page_number=1,
        page_size=25
    )
)

try:
    result = deposit_summary_controller.summary_by_merchant(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseError2Exception as e: 
    print(e)
except APIException as e: 
    print(e)

