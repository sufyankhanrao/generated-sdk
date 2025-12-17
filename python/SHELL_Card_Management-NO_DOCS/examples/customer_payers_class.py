from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.exceptions.fleetmanagement_v_1_customer_payers_400_error_exception import FleetmanagementV1CustomerPayers400ErrorException
from shellcardmanagementapis.exceptions.fleetmanagement_v_1_customer_payers_404_error_exception import FleetmanagementV1CustomerPayers404ErrorException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.payer_request import PayerRequest
from shellcardmanagementapis.models.payers import Payers
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

body = PayerRequest(
    payers=[
        Payers(
            col_co_id=14,
            col_co_code=14,
            payer_id=12345,
            payer_number='string',
            payer_name='ABC company',
            payer_group_id=456
        )
    ],
    return_basic_details_only=False,
    include_addresses=False,
    include_bonus_parameters=False,
    current_page=1,
    page_size=15
)

try:
    result = customer_controller.payers(
        apikey,
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except FleetmanagementV1CustomerPayers400ErrorException as e: 
    print(e)
except FleetmanagementV1CustomerPayers404ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

