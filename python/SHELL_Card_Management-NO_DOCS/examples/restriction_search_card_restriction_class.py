from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.exceptions.fleetmanagement_v_2_restriction_searchcard_401_error_exception import FleetmanagementV2RestrictionSearchcard401ErrorException
from shellcardmanagementapis.exceptions.fleetmanagement_v_2_restriction_searchcard_500_error_exception import FleetmanagementV2RestrictionSearchcard500ErrorException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
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

try:
    result = restriction_controller.search_card_restriction(
        apikey,
        request_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except FleetmanagementV2RestrictionSearchcard401ErrorException as e: 
    print(e)
except FleetmanagementV2RestrictionSearchcard500ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

