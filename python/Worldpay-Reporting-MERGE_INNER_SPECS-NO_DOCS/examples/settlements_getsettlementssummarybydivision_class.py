from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.date_range_search import DateRangeSearch
from reportingapi.models.entity_parent_type_division_2 import EntityParentTypeDivision2
from reportingapi.models.level_5_enum import Level5Enum
from reportingapi.models.pagination_type_2 import PaginationType2
from reportingapi.models.settlements_request_by_division import SettlementsRequestByDIVISION
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

settlements_controller = client.settlements
body = SettlementsRequestByDIVISION(
    hierarchy=EntityParentTypeDivision2(
        level=Level5Enum.CHAIN,
        values=[
            'AB1234',
            '111217'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    ),
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    )
)

try:
    result = settlements_controller.getsettlementssummarybydivision(
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

