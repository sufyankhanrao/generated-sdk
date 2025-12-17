from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.exceptions.fleetmanagement_v_1_user_loggedinuser_400_error_exception import FleetmanagementV1UserLoggedinuser400ErrorException
from shellcardmanagementapis.exceptions.fleetmanagement_v_1_user_loggedinuser_401_error_exception import FleetmanagementV1UserLoggedinuser401ErrorException
from shellcardmanagementapis.exceptions.fleetmanagement_v_1_user_loggedinuser_403_error_exception import FleetmanagementV1UserLoggedinuser403ErrorException
from shellcardmanagementapis.exceptions.fleetmanagement_v_1_user_loggedinuser_404_error_exception import FleetmanagementV1UserLoggedinuser404ErrorException
from shellcardmanagementapis.exceptions.fleetmanagement_v_1_user_loggedinuser_500_error_exception import FleetmanagementV1UserLoggedinuser500ErrorException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.fleetmanagement_v_1_user_loggedinuser_request import FleetmanagementV1UserLoggedinuserRequest
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

body = FleetmanagementV1UserLoggedinuserRequest(
    include_payer_group=False,
    include_eid_details=False,
    requested_api_name='Name of the API',
    payer_id=123456,
    payer_number='GB00123456'
)

try:
    result = customer_controller.loggedinuser(
        apikey,
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except FleetmanagementV1UserLoggedinuser400ErrorException as e: 
    print(e)
except FleetmanagementV1UserLoggedinuser401ErrorException as e: 
    print(e)
except FleetmanagementV1UserLoggedinuser403ErrorException as e: 
    print(e)
except FleetmanagementV1UserLoggedinuser404ErrorException as e: 
    print(e)
except FleetmanagementV1UserLoggedinuser500ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

