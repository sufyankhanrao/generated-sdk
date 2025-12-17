from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.status_code_enum import StatusCodeEnum
from fortisapi.models.user_type_code_enum import UserTypeCodeEnum
from fortisapi.models.v_1_users_request import V1UsersRequest

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

users_controller = client.users
body = V1UsersRequest(
    email='email@domain.com',
    last_name='Smith',
    primary_location_id='11e95f8ec39de8fbdb0a4f1a',
    username='{user_name}',
    user_type_code=UserTypeCodeEnum.ENUM_100,
    account_number='5454545454545454',
    branding_domain_url='{branding_domain_url}',
    cell_phone='3339998822',
    company_name='Fortis Payment Systems, LLC',
    contact_id='11e95f8ec39de8fbdb0a4f1a',
    date_of_birth='2021-12-01',
    domain_id='11e95f8ec39de8fbdb0a4f1a',
    email_trx_receipt=True,
    home_phone='3339998822',
    first_name='John',
    locale='en-US',
    office_phone='3339998822',
    office_ext_phone='5',
    terms_condition_code='20220308',
    tz='America/New_York',
    user_api_key='234bas8dfn8238f923w2',
    zip='48375',
    location_id='11e95f8ec39de8fbdb0a4f1a',
    status_code=StatusCodeEnum.ENUM_1,
    api_only=False,
    is_invitation=False
)

try:
    result = users_controller.create_a_new_user(body)

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

