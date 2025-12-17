from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.budle_details_request import BudleDetailsRequest
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    environment=Environment.SIT
)

restriction_controller = client.restriction
apikey = 'apikey6'

request_id = 'RequestId8'

body = BudleDetailsRequest(
    col_co_code=32,
    payer_number='CZ00000927',
    account_number='CZ00000927',
    bundle_id='1060'
)

try:
    result = restriction_controller.bundledetails(
        apikey,
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

