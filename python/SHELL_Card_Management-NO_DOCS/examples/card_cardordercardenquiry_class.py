from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.filters_2 import Filters2
from shellcardmanagementapis.models.order_card_enquiry_req_reference_type_enum import OrderCardEnquiryReqReferenceTypeEnum
from shellcardmanagementapis.models.order_card_enquiry_request import OrderCardEnquiryRequest
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    bearer_token_credentials=BearerTokenCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SIT
)

card_controller = client.card
request_id = 'RequestId8'

body = OrderCardEnquiryRequest(
    filters=Filters2(
        account_id=70,
        account_number='NL00000063',
        col_co_code=18,
        col_co_id=18,
        col_co_country_code='NL',
        payer_id=70,
        payer_number='NL00000063',
        reference_number=25,
        reference_type=OrderCardEnquiryReqReferenceTypeEnum.ENUM_1,
        from_date='20210502',
        to_date='20210505',
        order_request_id='34edbfbf-f05e-4d8d-bcd4-9eb7aea5ea41'
    )
)

try:
    result = card_controller.cardordercardenquiry(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

