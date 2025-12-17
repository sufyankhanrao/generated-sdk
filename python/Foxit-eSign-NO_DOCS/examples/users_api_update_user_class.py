from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.user_roles_enum import UserRolesEnum
from foxitesigntest.models.user_update import UserUpdate
from foxitesigntest.models.user_update_object import UserUpdateObject

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

users_api_controller = client.users_api
user_update_object = UserUpdateObject(
    user=UserUpdate(
        party_id='54',
        first_name='eSign',
        last_name='Demo',
        user_role=UserRolesEnum.SUPER_ADMIN,
        active=False,
        address='Miami, Florida',
        department='DEV',
        title='Tech Lead'
    )
)

try:
    result = users_api_controller.update_user(user_update_object)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

