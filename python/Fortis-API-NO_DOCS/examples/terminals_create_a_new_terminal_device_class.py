from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.communication_type_enum import CommunicationTypeEnum
from fortisapi.models.terminal_manufacturer_code_enum import TerminalManufacturerCodeEnum
from fortisapi.models.v_1_terminals_request import V1TerminalsRequest

client = FortisapiClient(
    user_id_credentials=UserIdCredentials(
        user_id='user-id'
    ),
    user_api_key_credentials=UserApiKeyCredentials(
        user_api_key='user-api-key'
    ),
    developer_id_credentials=DeveloperIdCredentials(
        developer_id='developer-id'
    ),
    environment=Environment.SANDBOX
)

terminals_controller = client.terminals
body = V1TerminalsRequest(
    location_id='11e95f8ec39de8fbdb0a4f1a',
    terminal_application_id='11e95f8ec39de8fbdb0a4f1a',
    terminal_manufacturer_code=TerminalManufacturerCodeEnum.ENUM_1,
    title='My terminal',
    serial_number='1234567890',
    debit=False,
    emv=False,
    cashback_enable=False,
    print_enable=False,
    sig_capture_enable=False,
    default_product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    terminal_cvm_id='11e95f8ec39de8fbdb0a4f1a',
    mac_address='3D:F2:C9:A6:B3:4F',
    local_ip_address='192.168.0.10',
    port=10009,
    terminal_number='973456789012367',
    header_line_1='line 1 sample',
    header_line_2='line 2 sample',
    header_line_3='line 3 sample',
    header_line_4='line 4 sample',
    header_line_5='line 5 sample',
    trailer_line_1='trailer 1 sample',
    trailer_line_2='trailer 2 sample',
    trailer_line_3='trailer 3 sample',
    trailer_line_4='trailer 4 sample',
    trailer_line_5='trailer 5 sample',
    default_checkin='2021-12-01',
    default_checkout='2021-12-01',
    default_room_rate=56,
    default_room_number='303',
    is_provisioned=False,
    tip_enable=False,
    validated_decryption=False,
    communication_type=CommunicationTypeEnum.HTTP,
    active=True
)

try:
    result = terminals_controller.create_a_new_terminal_device(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except Response401tokenException as e: 
    print(e)
except Response412Exception as e: 
    print(e)
except APIException as e: 
    print(e)

