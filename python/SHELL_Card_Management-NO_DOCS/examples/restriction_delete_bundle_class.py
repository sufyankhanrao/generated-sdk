from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.delete_bundle_request import DeleteBundleRequest
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

body = DeleteBundleRequest(
    bundle_id='123',
    col_co_code=86,
    col_co_id=1,
    payer_number='PH50000843',
    payer_id=853,
    account_id=854,
    account_number='PH50000844'
)

try:
    result = restriction_controller.delete_bundle(
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

