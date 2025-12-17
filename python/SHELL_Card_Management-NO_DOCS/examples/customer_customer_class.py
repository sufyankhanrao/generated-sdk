from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.exceptions.fleetmanagement_v_1_customer_customer_403_error_exception import FleetmanagementV1CustomerCustomer403ErrorException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.customer_detail_request import CustomerDetailRequest
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    environment=Environment.SIT
)

customer_controller = client.customer
apikey = 'apikey6'

request_id = 'RequestId8'

body = CustomerDetailRequest(
    col_co_id=14,
    col_co_code=14,
    payer_id=12345,
    payer_number='GB000000123',
    account_id=0,
    account_number='GB000000124'
)

try:
    result = customer_controller.customer(
        apikey,
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except FleetmanagementV1CustomerCustomer403ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

