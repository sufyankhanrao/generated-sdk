from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.update_if_exists_enum import UpdateIfExistsEnum
from fortisapi.models.v_1_contacts_request import V1ContactsRequest

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

contacts_controller = client.contacts
body = V1ContactsRequest(
    location_id='11e95f8ec39de8fbdb0a4f1a',
    last_name='Smith',
    account_number='54545433332',
    contact_api_id='137',
    first_name='John',
    cell_phone='3339998822',
    balance=245.36,
    company_name='Fortis Payment Systems, LLC',
    header_message='This is a sample message for you',
    date_of_birth='2021-12-01',
    email_trx_receipt=True,
    home_phone='3339998822',
    office_phone='3339998822',
    office_phone_ext='5',
    header_message_type=0,
    update_if_exists=UpdateIfExistsEnum.ENUM_1,
    contact_c_1='any',
    contact_c_2='anything',
    contact_c_3='something',
    parent_id='11e95f8ec39de8fbdb0a4f1a',
    email='email@domain.com'
)

try:
    result = contacts_controller.create_a_new_contact(body)

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

