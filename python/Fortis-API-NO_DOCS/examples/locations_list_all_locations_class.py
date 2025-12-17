from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.filter_by import FilterBy
from fortisapi.models.operator_1_enum import Operator1Enum
from fortisapi.models.operator_enum import OperatorEnum
from fortisapi.models.order_19 import Order19
from fortisapi.models.page import Page

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

locations_controller = client.locations
page = Page(
    number=1,
    size=50
)

order = [
    Order19(
        key='first_name',
        operator=OperatorEnum.ASC
    )
]

filter_by = [
    FilterBy(
        key='first_name',
        operator=Operator1Enum.ENUM_1,
        value='Fred'
    )
]

try:
    result = locations_controller.list_all_locations(
        page=page,
        order=order,
        filter_by=filter_by
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except Response401tokenException as e: 
    print(e)
except APIException as e: 
    print(e)

