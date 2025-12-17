from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.exceptions.error_object_exception import ErrorObjectException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.update_m_pay_reg_status_request import UpdateMPayRegStatusRequest
from shellcardmanagementapis.models.update_m_pay_reg_status_request_m_pay_requests_items import UpdateMPayRegStatusRequestMPayRequestsItems
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

body = UpdateMPayRegStatusRequest(
    col_co_id=32,
    col_co_code=32,
    payer_id=1223,
    payer_number='CZ00000923',
    m_pay_requests=[
        UpdateMPayRegStatusRequestMPayRequestsItems(
            global_request_id='123',
            status='Rejected',
            approver_user_id='AdminUser100',
            approver_user_display_name='AdminUser100',
            reason='approved'
        )
    ]
)

try:
    result = card_controller.updatemobilepaymentregistrationstatus(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorObjectException as e: 
    print(e)
except APIException as e: 
    print(e)

