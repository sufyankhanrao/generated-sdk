from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.user_creation import UserCreation
from foxitesigntest.models.user_creation_object import UserCreationObject
from foxitesigntest.models.user_roles_enum import UserRolesEnum

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

users_api_controller = client.users_api
user_creation_object = UserCreationObject(
    user=UserCreation(
        first_name='eSign',
        last_name='Demo',
        email_id='esigndemo@foxitsoftware.com',
        user_role=UserRolesEnum.ADMIN,
        active=True,
        send_mail_for_password_reset=True,
        allow_advanced_email_validation=True,
        address='Miami, Florida',
        department='DEV',
        title='Tech Lead',
        login_password='TXxgjjezFLAqnR'
    )
)

try:
    result = users_api_controller.create_user(user_creation_object)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

