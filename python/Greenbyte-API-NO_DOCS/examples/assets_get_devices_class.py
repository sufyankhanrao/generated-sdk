from greenbyteapi.configuration import Environment
from greenbyteapi.exceptions.api_exception import APIException
from greenbyteapi.exceptions.problem_details_exception import ProblemDetailsException
from greenbyteapi.greenbyteapi_client import GreenbyteapiClient
from greenbyteapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials

client = GreenbyteapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        x_api_key='X-Api-Key'
    ),
    environment=Environment.PRODUCTION,
    customer='intro'
)

assets_controller = client.assets
device_type_ids = [
    1,
    2,
    3
]

site_ids = [
    1,
    2,
    3
]

parent_ids = [
    1,
    2,
    3
]

page_size = 50

page = 1

use_utc = False

try:
    result = assets_controller.get_devices(
        device_type_ids=device_type_ids,
        site_ids=site_ids,
        parent_ids=parent_ids,
        page_size=page_size,
        page=page,
        use_utc=use_utc
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ProblemDetailsException as e: 
    print(e)
except APIException as e: 
    print(e)

