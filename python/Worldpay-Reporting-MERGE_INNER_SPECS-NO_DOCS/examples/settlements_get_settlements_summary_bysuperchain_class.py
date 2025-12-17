from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.card_network_2_enum import CardNetwork2Enum
from reportingapi.models.card_type_1_enum import CardType1Enum
from reportingapi.models.date_range_search import DateRangeSearch
from reportingapi.models.entity_super_chain_1 import EntitySuperChain1
from reportingapi.models.level_4_enum import Level4Enum
from reportingapi.models.pagination_type_2 import PaginationType2
from reportingapi.models.settlements_request_by_super_chain import SettlementsRequestBySuperChain
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

settlements_controller = client.settlements
body = SettlementsRequestBySuperChain(
    hierarchy=EntitySuperChain1(
        level=Level4Enum.SUPERCHAIN,
        values=[
            'SCNPCB6111',
            'SCNPCB8811'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-08-02'
    ),
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    ),
    card_type=CardType1Enum.CREDIT,
    card_networks=[
        CardNetwork2Enum.VISA,
        CardNetwork2Enum.MASTERCARD,
        CardNetwork2Enum.DISCOVER,
        CardNetwork2Enum.AMEX
    ]
)

try:
    result = settlements_controller.get_settlements_summary_bysuperchain(
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

